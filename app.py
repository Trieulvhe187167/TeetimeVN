from flask import Flask, redirect, request, url_for, render_template, send_from_directory
from flask_babel import Babel
from flask_mail import Mail
from modules.courses import courses_bp, extract_city, COUNTRY_LABELS
from modules.admin import admin_bp
from modules.booking import booking_bp
from modules.auth import auth_bp
import os
import sqlite3

# Khởi tạo Mail ở cấp module, để có thể import từ modules khác
mail = Mail()

SUPPORTED_URL_LANGS = ["zh-CN", "zh-TW", "en", "vi", "ja", "ko"]
DEFAULT_LANG = "en"

def url_to_locale(code: str) -> str:
    return code.replace("-", "_")

def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'change-me')

    # ---------- Cấu hình Flask-Mail ----------
    # Ví dụ: nếu bạn dùng Gmail, cần set đúng biến môi trường:
    #   MAIL_USERNAME: địa chỉ Gmail hoặc App Password
    #   MAIL_PASSWORD: App Password
    app.config['MAIL_SERVER'] = "smtp.gmail.com"
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = "levantrieu170604@gmail.com"
    app.config['MAIL_PASSWORD'] = "jskfdqalznzuulhp"
    app.config['MAIL_DEFAULT_SENDER'] = "levantrieu170604@gmail.com"


    # Khởi tạo Mail với app
    mail.init_app(app)

    # ---------- Cấu hình Babel ----------
    app.config.update(
        BABEL_DEFAULT_LOCALE=url_to_locale(DEFAULT_LANG),
        BABEL_TRANSLATION_DIRECTORIES="translations"
    )

    @app.context_processor
    def inject_utils():
        parts = request.path.split("/", 2)
        current = parts[1] if len(parts) > 1 else DEFAULT_LANG
        if current not in SUPPORTED_URL_LANGS:
            current = DEFAULT_LANG

        def switch_lang(new_lang):
            p = request.path.split("/", 2)
            if len(p) > 1 and p[1] in SUPPORTED_URL_LANGS:
                p[1] = new_lang
            else:
                p.insert(1, new_lang)
            return "/".join(p)

        return dict(
            switch_lang=switch_lang,
            lang=current,
            supported_langs=SUPPORTED_URL_LANGS
        )

    def select_locale():
        parts = request.path.split("/", 2)
        prefix = parts[1] if len(parts) > 1 else DEFAULT_LANG
        if prefix not in SUPPORTED_URL_LANGS:
            prefix = DEFAULT_LANG
        return url_to_locale(prefix)

    Babel(app, locale_selector=select_locale)

    # Đăng ký blueprint
    app.register_blueprint(auth_bp)
    app.register_blueprint(courses_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(booking_bp)

    @app.route("/")
    def root():
        best = request.accept_languages.best_match(SUPPORTED_URL_LANGS)
        lang = best if best in SUPPORTED_URL_LANGS else DEFAULT_LANG
        return redirect(f"/{lang}/")

    @app.route("/<lang>/")
    def index(lang):
        if lang not in SUPPORTED_URL_LANGS:
            lang = DEFAULT_LANG

        discount = request.args.get('discount', type=int)
        location = request.args.get('location', type=str)
        rating = request.args.get('rating', type=float)

        db_path = os.path.join(app.root_path, "data", "teetimevn_dev.db")
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row

        seo = conn.execute(
            "SELECT * FROM static_page_i18n WHERE page_id = ? AND lang = ?",
            ('home', lang)
        ).fetchone()

        query = "SELECT DISTINCT gc.id, gc.slug FROM golf_course gc"
        conds, params = [], []

        if location:
            query += " JOIN golf_course_i18n gci ON gc.id = gci.course_id"
            conds.append("gci.address LIKE ?")
            params.append(f"%{location}%")

        if discount:
            query += " JOIN course_price cp ON gc.id = cp.course_id"
            conds.append("(100 - (cp.discount_price_vnd * 100.0 / cp.rack_price_vnd)) >= ?")
            params.append(discount)

        if rating:
            query += " JOIN course_evaluation ce ON gc.id = ce.course_id"
            avg_expr = "(ce.design_layout + ce.turf_maintenance + ce.facilities_services + ce.landscape_environment + ce.playability_access) / 5.0"
            conds.append(f"{avg_expr} >= ?")
            params.append(rating)

        if conds:
            query += " WHERE " + " AND ".join(conds)

        query += " ORDER BY gc.id"
        rows = conn.execute(query, params).fetchall()

        courses = []
        for r in rows:
            text = conn.execute(
                "SELECT name, address FROM golf_course_i18n WHERE course_id = ? AND lang = ?",
                (r['id'], lang)
            ).fetchone()

            avg = conn.execute(
                "SELECT ROUND((design_layout + turf_maintenance + facilities_services + landscape_environment + playability_access) / 5.0, 1) AS avg_rating FROM course_evaluation WHERE course_id = ?",
                (r['id'],)
            ).fetchone()

            if text:
                courses.append({
                    'slug': r['slug'],
                    'name': text['name'],
                    'address': text['address'],
                    'avg_rating': avg['avg_rating'] if avg and avg['avg_rating'] else None
                })

        loc_rows = conn.execute(
            "SELECT DISTINCT address FROM golf_course_i18n WHERE lang = ?", (lang,)
        ).fetchall()
        locations = {
            extract_city(r['address'], lang)
            for r in loc_rows if r['address'].strip()
        }

        conn.close()
        return render_template(
            "index.html",
            lang=lang,
            seo=seo,
            courses=courses,
            locations=sorted(locations),
            banner=True
        )

    @app.route("/sitemap.xml")
    def sitemap():
        db_path = os.path.join(app.root_path, "data", "teetimevn_dev.db")
        conn = sqlite3.connect(db_path)
        rows = conn.execute("SELECT slug FROM golf_course").fetchall()
        conn.close()

        slugs = [row[0] for row in rows]
        base = request.url_root.rstrip('/')
        urls = []

        for slug in slugs:
            for lang in SUPPORTED_URL_LANGS:
                urls.append((lang, f"{base}/{lang}/courses/{slug}/"))

        return render_template(
            "sitemap.xml",
            urls=urls,
            DEFAULT_LANG=DEFAULT_LANG,
            supported_langs=SUPPORTED_URL_LANGS
        ), 200, {'Content-Type': 'application/xml'}

    @app.route("/robots.txt")
    def robots():
        return send_from_directory(app.static_folder, "robots.txt")

    @app.route("/debug-seo/<lang>")
    def debug_seo(lang):
        if lang not in SUPPORTED_URL_LANGS:
            return "⛔ Unsupported language", 400

        db_path = os.path.join(app.root_path, "data", "teetimevn_dev.db")
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row

        row = conn.execute(
            "SELECT * FROM static_page_i18n WHERE page_id = ? AND lang = ?",
            ("home", lang)
        ).fetchone()
        conn.close()

        if not row:
            return f"⚠️ No SEO record found for lang = '{lang}'"

        return f"""
        <h1>SEO for page_id = 'home' ({lang})</h1>
        <ul>
          <li><strong>Title:</strong> {row['title']}</li>
          <li><strong>Description:</strong> {row['description']}</li>
          <li><strong>Keywords:</strong> {row['keywords']}</li>
        </ul>
        """

    return app

if __name__ == "__main__":
    create_app().run(debug=True)
