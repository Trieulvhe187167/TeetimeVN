# modules/courses.py

from pathlib import Path
import sqlite3
import re
import json
import os
from datetime import datetime
from flask import Blueprint, render_template, g, request, current_app, session, redirect, url_for, flash, jsonify
from flask_babel import _
from werkzeug.utils import secure_filename

# Determine the path to the SQLite database
script_path  = Path(__file__).resolve()
project_root = script_path.parent.parent
DB_PATH      = project_root / "data" / "teetimevn_dev.db"

# File upload settings
UPLOAD_FOLDER = 'static/media/reviews'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

# Fallback country labels by language
COUNTRY_LABELS = {
    'en': 'Vietnam',
    'vi': 'Việt Nam',
    'zh-CN': '越南',
    'zh-TW': '越南',
    'ja': 'ベトナム',
    'ko': '베트남'
}

def get_db():
    """Open a database connection if not already open."""
    if not DB_PATH.is_file():
        raise FileNotFoundError(f"Database not found: {DB_PATH}")
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(_=None):
    """Close the database connection at the end of request."""
    db = g.pop("db", None)
    if db:
        db.close()

def fetch_i18n(db, cid, lang):
    """
    Fetch the i18n record for a given course ID and language.
    Falls back to English or Simplified Chinese if not available.
    """
    for code in (lang, 'en', 'zh-CN'):
        row = db.execute(
            "SELECT * FROM golf_course_i18n WHERE course_id=? AND lang=?",
            (cid, code)
        ).fetchone()
        if row:
            return row
    return None

def extract_city(addr: str, lang: str) -> str:
    """
    Extract city name from a full address string, handling
    different language conventions.
    """
    addr = addr.strip()
    if ',' in addr:
        parts = [p.strip() for p in addr.split(',')]
        return parts[1] if len(parts) > 1 else parts[0]

    # Chinese (Simplified / Traditional)
    if lang in ('zh-CN', 'zh-TW'):
        country = COUNTRY_LABELS.get(lang, '')
        tokens = re.findall(r'.+?(?:省|市|区|县)', addr)
        if tokens:
            city_tok = tokens[0]
            if country and city_tok.startswith(country):
                city_tok = city_tok[len(country):]
            return city_tok
        return addr

    # Japanese
    if lang == 'ja':
        tokens = addr.split()
        for tok in tokens:
            if tok.endswith(('市', '県')):
                return tok
        return tokens[-2] if len(tokens) >= 2 else tokens[-1]

    # Korean
    if lang == 'ko':
        tokens = addr.split()
        for tok in tokens:
            if tok.endswith(('시', '군', '도')):
                return tok
        return tokens[-2] if len(tokens) >= 2 else tokens[-1]

    # Default: return full string
    return addr

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_course_slug(course_id):
    """Helper function để lấy slug của course"""
    db = get_db()
    course = db.execute(
        "SELECT slug FROM golf_course WHERE id = ?", (course_id,)
    ).fetchone()
    return course['slug'] if course else ''

def create_bp():
    bp = Blueprint('courses', __name__, url_prefix='/<lang>/courses')

    @bp.before_app_request
    def before():
        get_db()

    @bp.teardown_app_request
    def after(exc):
        close_db()

    @bp.route('/')
    def course_list(lang):
        db = get_db()
        discount = request.args.get('discount', type=int)
        location = request.args.get('location', type=str)
        rating   = request.args.get('rating', type=float)

        # Build base query
        query = 'SELECT DISTINCT gc.id, gc.slug FROM golf_course gc'
        conds, params = [], []

        # Filter by location
        if location:
            query += ' JOIN golf_course_i18n gci ON gc.id = gci.course_id'
            conds.append('gci.address LIKE ?')
            params.append(f'%{location}%')

        # Filter by discount percentage
        if discount:
            query += ' JOIN course_price cp ON gc.id = cp.course_id'
            conds.append('(100 - (cp.discount_price_vnd * 100.0 / cp.rack_price_vnd)) >= ?')
            params.append(discount)

        # Filter by average rating
        if rating:
            query += ' JOIN course_evaluation ce ON gc.id = ce.course_id'
            avg_expr = '(ce.design_layout + ce.turf_maintenance + ce.facilities_services + ce.landscape_environment + ce.playability_access) / 5.0'
            conds.append(f'{avg_expr} >= ?')
            params.append(rating)

        if conds:
            query += ' WHERE ' + ' AND '.join(conds)
        query += ' ORDER BY gc.id'

        rows = db.execute(query, params).fetchall()

        # Prepare list of courses with localized name, address and avg rating
        courses = []
        for r in rows:
            rec = fetch_i18n(db, r['id'], lang)
            name = rec['name'] if rec else r['slug']
            address = rec['address'] if rec else ''
            avg_row = db.execute("""
                SELECT ROUND(AVG(design_layout + turf_maintenance + facilities_services + landscape_environment + playability_access)/5.0, 1) AS avg_rating
                FROM course_evaluation WHERE course_id=?
            """, (r['id'],)).fetchone()
            avg_rating = avg_row['avg_rating'] if avg_row and avg_row['avg_rating'] else None
            courses.append({
                'slug': r['slug'],
                'name': name,
                'address': address,
                'avg_rating': avg_rating
            })

        # Extract distinct city list for filter dropdown
        loc_rows = db.execute(
            "SELECT address FROM golf_course_i18n WHERE lang=?", (lang,)
        ).fetchall()
        locations = { extract_city(r['address'], lang) for r in loc_rows }

        return render_template(
            'courses.html',
            lang=lang,
            rows=courses,
            locations=sorted(locations)
        )

    @bp.route('/<slug>/')
    def course_detail(lang, slug):
        db = get_db()
        course = db.execute('SELECT * FROM golf_course WHERE slug=?', (slug,)).fetchone()
        if not course:
            return '404 Not Found', 404

        # Fetch localized text
        text = fetch_i18n(db, course['id'], lang)

        # Fetch price tiers
        prices = db.execute('SELECT * FROM course_price WHERE course_id=?', (course['id'],)).fetchall()

        # Embed map iframe URL if any
        embed = course['maps_url'] or ''
        lat, lng = course['lat'], course['lng']
        map_link = f'https://www.google.com/maps/search/?api=1&query={lat},{lng}'

        # Load gallery images
        gallery_dir = Path(current_app.static_folder) / 'media' / slug / 'gallery'
        images = []
        if gallery_dir.is_dir():
            images = sorted([
                fn.name for fn in gallery_dir.iterdir()
                if fn.suffix.lower() in ('.jpg', '.jpeg', '.png', '.gif')
            ])

        # Fetch evaluation scores
        evaluation = db.execute(
            'SELECT * FROM course_evaluation WHERE course_id=?', (course['id'],)
        ).fetchone()

        # Get the latest exchange rates from fx_rate table
        fx_rate_rows = db.execute('SELECT currency, rate_to_vnd FROM fx_rate').fetchall()
        fx_rates = {row['currency']: row['rate_to_vnd'] for row in fx_rate_rows}

        # Generate time slots every 30 minutes from 05:30 to 18:00
        time_slots = []
        h, m = 5, 30
        while h < 18 or (h == 18 and m == 0):
            time_slots.append(f"{h:02d}:{m:02d}")
            m += 30
            if m == 60:
                m = 0
                h += 1

        # Define additional amenities for booking form
        amenities = [
            ('rent_clubs', _('Rent golf clubs')),
            ('caddy',      _('Caddy')),
            ('cart',       _('Golf cart')),
        ]

        # Compute discounted prices by tier: weekday, weekend, twilight
        tier_prices = {}
        for p in prices:
            key = p['tier_type'].lower()   # expecting 'weekday','weekend','twilight'
            orig     = p['rack_price_vnd'] or 0
            disc_txt = p['discount_note'] or '0%'
            disc_num = float(disc_txt.replace('%','').replace('-',''))
            disc_rate= disc_num / 100
            tier_prices[key] = int(orig * (1 - disc_rate))

        # Static service prices (VND)
        service_prices = {
            'rent_clubs': 1200000,
            'caddy':      500000,
            'cart':       700000,
            'insurance':  100000
        }

        # Get today's date for booking form
        today_date = datetime.now().strftime('%Y-%m-%d')

        # ========== PHẦN MỚI: XỬ LÝ REVIEWS ==========
        # Get reviews với pagination
        page = request.args.get('page', 1, type=int)
        per_page = 10
        
        # Query reviews với thông tin user
        reviews_query = db.execute("""
            SELECT r.*, u.username, u.fullname,
                   datetime(r.created_at) as created_at_display
            FROM reviews r
            JOIN users u ON r.user_id = u.id
            WHERE r.course_id = ?
            ORDER BY r.created_at DESC
            LIMIT ? OFFSET ?
        """, (course['id'], per_page, (page - 1) * per_page)).fetchall()
        
        # Đếm tổng số reviews
        total_reviews_row = db.execute(
            "SELECT COUNT(*) as count FROM reviews WHERE course_id = ?", 
            (course['id'],)
        ).fetchone()
        total_reviews = total_reviews_row['count'] if total_reviews_row else 0
        
        # Tính điểm trung bình
        avg_rating_row = db.execute(
            "SELECT AVG(rating) as avg FROM reviews WHERE course_id = ?",
            (course['id'],)
        ).fetchone()
        avg_rating = avg_rating_row['avg'] if avg_rating_row and avg_rating_row['avg'] else 0
        
        # Phân bố đánh giá theo sao
        rating_distribution = {}
        for i in range(1, 6):
            count_row = db.execute(
                "SELECT COUNT(*) as count FROM reviews WHERE course_id = ? AND rating = ?",
                (course['id'], i)
            ).fetchone()
            rating_distribution[i] = count_row['count'] if count_row else 0
        
        # Kiểm tra xem user hiện tại có thể review không
        can_review = False
        user_found_helpful_ids = []
        
        if session.get('user_id'):
            # Kiểm tra đã có booking và đã hoàn thành chưa
            has_booking = db.execute("""
                SELECT id FROM bookings 
                WHERE user_id = ? AND course_id = ? 
                AND status IN ('confirmed', 'completed')
                LIMIT 1
            """, (session['user_id'], course['id'])).fetchone()
            
            # Kiểm tra đã review chưa
            existing_review = db.execute(
                "SELECT id FROM reviews WHERE user_id = ? AND course_id = ?",
                (session['user_id'], course['id'])
            ).fetchone()
            
            can_review = has_booking and not existing_review
            
            # Lấy danh sách review_id mà user đã mark helpful
            helpful_rows = db.execute(
                "SELECT review_id FROM review_helpful WHERE user_id = ?",
                (session['user_id'],)
            ).fetchall()
            user_found_helpful_ids = [row['review_id'] for row in helpful_rows]
        
        # Format reviews để hiển thị
        reviews = []
        for review in reviews_query:
            review_dict = dict(review)
            review_dict['user_name'] = review['fullname'] or review['username']
            review_dict['user_found_helpful'] = review['id'] in user_found_helpful_ids
            
            # Format date cho hiển thị
            if review['created_at_display']:
                try:
                    # Parse string date và format lại
                    dt = datetime.strptime(review['created_at_display'].split(' ')[0], '%Y-%m-%d')
                    review_dict['created_at_display'] = dt.strftime('%d/%m/%Y')
                except:
                    review_dict['created_at_display'] = review['created_at_display'].split(' ')[0]
            
            # Parse JSON images nếu có
            if review['images']:
                try:
                    review_dict['images'] = json.loads(review['images'])
                except:
                    review_dict['images'] = []
            else:
                review_dict['images'] = []
                
            # Kiểm tra verified booking
            verified = db.execute("""
                SELECT id FROM bookings 
                WHERE user_id = ? AND course_id = ? 
                AND status IN ('confirmed', 'completed')
                LIMIT 1
            """, (review['user_id'], course['id'])).fetchone()
            review_dict['verified_booking'] = bool(verified)
            
            reviews.append(review_dict)
        
        # Tính số trang
        total_pages = (total_reviews + per_page - 1) // per_page

        return render_template(
            'course_detail.html',
            lang=lang,
            course=course,
            text=text,
            prices=prices,
            evaluation=evaluation,
            embed=embed,
            map_link=map_link,
            images=images,
            fx_rates=fx_rates,
            time_slots=time_slots,
            amenities=amenities,
            tier_prices=tier_prices,
            service_prices=service_prices,
            today_date=today_date,
            # Thêm các biến cho reviews
            reviews=reviews,
            total_reviews=total_reviews,
            avg_rating=avg_rating,
            rating_distribution=rating_distribution,
            can_review=can_review,
            current_page=page,
            total_pages=total_pages
        )

    @bp.route('/<slug>/add_review', methods=['POST'])
    def add_review(lang, slug):
        """Thêm hoặc cập nhật review cho course"""
        if not session.get('user_id'):
            flash(_('Please login to write a review'), 'error')
            return redirect(url_for('courses.course_detail', lang=lang, slug=slug))
        
        if session.get('role') == 'admin':
            flash(_('Administrators cannot write reviews'), 'error')
            return redirect(url_for('courses.course_detail', lang=lang, slug=slug))
        
        db = get_db()
        
        # Get course by slug
        course = db.execute('SELECT id FROM golf_course WHERE slug=?', (slug,)).fetchone()
        if not course:
            flash(_('Course not found'), 'error')
            return redirect(url_for('courses.course_list', lang=lang))
        
        course_id = course['id']
        user_id = session['user_id']
        
        # Get form data
        rating = request.form.get('rating')
        comment = request.form.get('comment')
        review_id = request.form.get('review_id')
        
        if not all([rating, comment]):
            flash(_('Please fill in all required fields'), 'error')
            return redirect(url_for('courses.course_detail', lang=lang, slug=slug))
        
        # Validate rating
        try:
            rating = int(rating)
            if rating < 1 or rating > 5:
                raise ValueError
        except (ValueError, TypeError):
            flash(_('Please provide a valid rating (1-5 stars)'), 'error')
            return redirect(url_for('courses.course_detail', lang=lang, slug=slug))
        
        # Kiểm tra user đã có booking chưa (chỉ khi tạo mới)
        if not review_id:
            has_booking = db.execute("""
                SELECT id FROM bookings 
                WHERE user_id = ? AND course_id = ? 
                AND status IN ('confirmed', 'completed')
                LIMIT 1
            """, (user_id, course_id)).fetchone()
            
            if not has_booking:
                flash(_('You need to book and play at this course before writing a review'), 'error')
                return redirect(url_for('courses.course_detail', lang=lang, slug=slug))
            
            # Kiểm tra đã review chưa
            existing_review = db.execute(
                "SELECT id FROM reviews WHERE user_id = ? AND course_id = ?",
                (user_id, course_id)
            ).fetchone()
            
            if existing_review:
                flash(_('You have already reviewed this course'), 'error')
                return redirect(url_for('courses.course_detail', lang=lang, slug=slug))
        
        # Xử lý upload ảnh
        images = []
        upload_folder = os.path.join(current_app.root_path, UPLOAD_FOLDER)
        
        # Tạo thư mục nếu chưa tồn tại
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        
        if 'images' in request.files:
            files = request.files.getlist('images')
            for file in files[:5]:  # Giới hạn 5 ảnh
                if file and file.filename and allowed_file(file.filename):
                    # Kiểm tra kích thước file
                    file.seek(0, os.SEEK_END)
                    file_size = file.tell()
                    file.seek(0)
                    
                    if file_size <= MAX_FILE_SIZE:
                        filename = secure_filename(file.filename)
                        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                        filename = f"{user_id}_{timestamp}_{filename}"
                        filepath = os.path.join(upload_folder, filename)
                        file.save(filepath)
                        images.append(filename)
        
        try:
            if review_id:
                # Update existing review
                existing = db.execute(
                    "SELECT * FROM reviews WHERE id = ? AND user_id = ?",
                    (review_id, user_id)
                ).fetchone()
                
                if existing:
                    # Xóa ảnh cũ nếu có ảnh mới
                    if images and existing['images']:
                        old_images = json.loads(existing['images'])
                        for old_img in old_images:
                            try:
                                os.remove(os.path.join(upload_folder, old_img))
                            except:
                                pass
                    
                    db.execute("""
                        UPDATE reviews 
                        SET rating = ?, comment = ?, images = ?, updated_at = datetime('now')
                        WHERE id = ? AND user_id = ?
                    """, (rating, comment, json.dumps(images) if images else existing['images'], 
                          review_id, user_id))
                else:
                    flash(_('Review not found'), 'error')
                    return redirect(url_for('courses.course_detail', lang=lang, slug=slug))
            else:
                # Create new review
                db.execute("""
                    INSERT INTO reviews (course_id, user_id, rating, comment, images, created_at)
                    VALUES (?, ?, ?, ?, ?, datetime('now'))
                """, (course_id, user_id, rating, comment, 
                      json.dumps(images) if images else None))
            
            db.commit()
            flash(_('Review submitted successfully!'), 'success')
            
        except Exception as e:
            db.rollback()
            flash(_('An error occurred while saving your review'), 'error')
            print(f"Review error: {e}")
        
        # Redirect về course detail với anchor
        return redirect(url_for('courses.course_detail', lang=lang, slug=slug) + '#reviews')

    # API routes for review functionality
    @bp.route('/api/review/<int:review_id>')
    def get_review(lang, review_id):
        """API để lấy thông tin review"""
        db = get_db()
        review = db.execute(
            "SELECT * FROM reviews WHERE id = ?", (review_id,)
        ).fetchone()
        
        if not review:
            return jsonify({'error': 'Review not found'}), 404
        
        return jsonify({
            'id': review['id'],
            'rating': review['rating'],
            'comment': review['comment'],
            'images': json.loads(review['images']) if review['images'] else []
        })

    @bp.route('/api/review/<int:review_id>', methods=['DELETE'])
    def delete_review(lang, review_id):
        """API để xóa review"""
        if not session.get('user_id'):
            return jsonify({'success': False, 'message': 'Login required'}), 401
        
        db = get_db()
        review = db.execute(
            "SELECT * FROM reviews WHERE id = ? AND user_id = ?",
            (review_id, session['user_id'])
        ).fetchone()
        
        if not review:
            return jsonify({'success': False, 'message': 'Review not found'}), 404
        
        try:
            # Xóa ảnh nếu có
            if review['images']:
                upload_folder = os.path.join(current_app.root_path, UPLOAD_FOLDER)
                images = json.loads(review['images'])
                for img in images:
                    try:
                        os.remove(os.path.join(upload_folder, img))
                    except:
                        pass
            
            # Xóa review
            db.execute("DELETE FROM reviews WHERE id = ?", (review_id,))
            
            # Xóa helpful votes
            db.execute("DELETE FROM review_helpful WHERE review_id = ?", (review_id,))
            
            db.commit()
            return jsonify({'success': True})
            
        except Exception as e:
            db.rollback()
            print(f"Delete review error: {e}")
            return jsonify({'success': False, 'message': 'Error deleting review'}), 500

    @bp.route('/api/review/<int:review_id>/helpful', methods=['POST'])
    def toggle_helpful(lang, review_id):
        """API để đánh dấu review hữu ích"""
        if not session.get('user_id'):
            return jsonify({'success': False, 'message': 'Login required'}), 401
        
        db = get_db()
        
        # Kiểm tra review tồn tại
        review = db.execute(
            "SELECT * FROM reviews WHERE id = ?", (review_id,)
        ).fetchone()
        
        if not review:
            return jsonify({'success': False, 'message': 'Review not found'}), 404
        
        try:
            # Kiểm tra đã vote chưa
            existing = db.execute(
                "SELECT * FROM review_helpful WHERE review_id = ? AND user_id = ?",
                (review_id, session['user_id'])
            ).fetchone()
            
            if existing:
                # Remove vote
                db.execute(
                    "DELETE FROM review_helpful WHERE review_id = ? AND user_id = ?",
                    (review_id, session['user_id'])
                )
                db.execute(
                    "UPDATE reviews SET helpful_count = helpful_count - 1 WHERE id = ?",
                    (review_id,)
                )
                is_helpful = False
            else:
                # Add vote
                db.execute(
                    "INSERT INTO review_helpful (review_id, user_id) VALUES (?, ?)",
                    (review_id, session['user_id'])
                )
                db.execute(
                    "UPDATE reviews SET helpful_count = helpful_count + 1 WHERE id = ?",
                    (review_id,)
                )
                is_helpful = True
            
            db.commit()
            
            # Lấy count mới
            updated = db.execute(
                "SELECT helpful_count FROM reviews WHERE id = ?", (review_id,)
            ).fetchone()
            
            return jsonify({
                'success': True,
                'helpful_count': updated['helpful_count'],
                'is_helpful': is_helpful
            })
            
        except Exception as e:
            db.rollback()
            print(f"Toggle helpful error: {e}")
            return jsonify({'success': False, 'message': 'Error updating helpful'}), 500

    return bp

courses_bp = create_bp()