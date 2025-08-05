# file: modules/auth.py

import sqlite3
from flask_babel import _
from flask import (
    Blueprint, render_template, request, redirect, url_for,
    flash, session, current_app
)
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadSignature
from modules.courses import get_db, close_db
from functools import wraps

auth_bp = Blueprint('auth', __name__, url_prefix='/<lang>/auth')


# ---------- Helper: Generate & Confirm Token for Password Reset ----------
def generate_confirmation_token(email):
    """
    Generate a time-limited token (mặc định 30 phút) chứa email của user.
    """
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    return serializer.dumps(email, salt='password-reset-salt')


def confirm_token(token, expiration=1800):
    """
    Xác thực token còn hiệu lực (max_age = expiration). 
    Trả về email nếu hợp lệ, ngược lại trả về None.
    """
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    try:
        email = serializer.loads(
            token,
            salt='password-reset-salt',
            max_age=expiration
        )
    except (SignatureExpired, BadSignature):
        return None
    return email


# ---------- Helper: Send Email via Flask-Mail (deferred import) ----------
def send_email(to, subject, template, **kwargs):
    """
    Gửi email sử dụng Flask-Mail.
      - to: địa chỉ nhận email
      - subject: tiêu đề email
      - template: đường dẫn đến template HTML trong thư mục 'templates/'
      - kwargs: biến context để render template
    """
    # Import mail ở đây để tránh circular import với app.py
    from app import mail
    from flask_mail import Message

    msg = Message(subject, recipients=[to])
    msg.html = render_template(template, **kwargs)
    mail.send(msg)


# ---------- Route: Login (cho phép GET + POST) ----------
# modules/auth.py

# modules/auth.py

@auth_bp.route('/login/', methods=['POST'])
def login(lang):
    """
    Xử lý POST request khi user submit form login.
    Nếu login thành công => flash("Logged in successfully!", "login-success") + redirect về index hoặc next_url.
    Nếu login thất bại => flash("Invalid username or password", "login-error") + redirect về index.
    """
    username = request.form.get('username')
    raw_password = request.form.get('password')
    db = get_db()
    user = db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()

    if user and check_password_hash(user['password_hash'], raw_password):
        session.clear()
        session['user_id'] = user['id']
        session['username'] = user['username']
        session['role'] = user['role']
        # Đăng nhập thành công: category là "login-success"
        flash(_("Logged in successfully!"), "login-success")
        
        # Kiểm tra nếu có next_url thì redirect về đó
        next_url = session.pop('next_url', None)
        if next_url:
            return redirect(next_url)
    else:
        # Đăng nhập thất bại: category là "login-error"
        flash(_("Invalid username or password"), "login-error")

    return redirect(url_for('index', lang=lang))



# ---------- Route: Register (cho phép GET + POST) ----------
@auth_bp.route('/register/', methods=['GET', 'POST'])
def register(lang):
    """
    Nếu GET, chuyển về trang Home.
    Nếu POST, xử lý form đăng ký:
      - Lấy email, username, password, phone, fullname, role.
      - Kiểm tra user/email có tồn tại chưa.
      - Nếu trùng, flash lỗi, redirect về Home.
      - Nếu hợp lệ, hash password, chèn vào DB, flash success, redirect về Home.
    """
    if request.method == 'GET':
        return redirect(url_for('index', lang=lang))

    # POST: xử lý đăng ký
    email = request.form.get('email')
    username = request.form.get('username')
    raw_password = request.form.get('password')
    phone = request.form.get('phone')
    fullname = request.form.get('fullname')
    role = request.form.get('role', 'user')

    db = get_db()
    existing = db.execute(
        "SELECT id FROM users WHERE email = ? OR username = ?",
        (email, username)
    ).fetchone()
    if existing:
        flash(_("Email or username already exists."), "danger")
        return redirect(url_for('index', lang=lang))

    pw_hash = generate_password_hash(raw_password)
    db.execute(
        "INSERT INTO users (email, phone, username, password_hash, role, fullname) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        (email, phone, username, pw_hash, role, fullname)
    )
    db.commit()
    flash(_("Registration successful! You can now log in."), "success")
    return redirect(url_for('index', lang=lang))


# ---------- Route: Logout ----------
@auth_bp.route('/logout/')
def logout(lang):
    """
    Xóa session và redirect về Home.
    """
    session.clear()
    flash(_("You have been logged out."), "info")
    return redirect(url_for('index', lang=lang))


# ---------- Decorator: Admin-Only Access ----------
def admin_required(f):
    """
    Decorator để hạn chế một số route chỉ cho admin truy cập.
    Nếu session['role'] != 'admin', flash cảnh báo và redirect về courses list.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('role') != 'admin':
            flash("You do not have permission to access this page.", "warning")
            return redirect(url_for('courses.course_list', lang=kwargs.get('lang')))
        return f(*args, **kwargs)
    return decorated_function


# ---------- Route: Forgot Password (Request Reset) ----------
@auth_bp.route('/forgot-password/', methods=['GET', 'POST'])
def forgot_password(lang):
    """
    Nếu GET, redirect về Home.
    Nếu POST, lấy email người dùng:
      - Nếu không có email, flash warning.
      - Nếu email không tồn tại trong DB, flash danger.
      - Nếu tồn tại, tạo token, gửi email chứa link reset, flash info.
    Cuối cùng redirect về trang login (vì login GET sẽ redirect về Home).
    """
    if request.method == 'GET':
        return redirect(url_for('index', lang=lang))

    # POST: xử lý quên mật khẩu
    email = request.form.get('email')
    if not email:
        flash("Please enter your email address.", "warning")
        return redirect(url_for('auth.forgot_password', lang=lang))

    db = get_db()
    user = db.execute(
        "SELECT * FROM users WHERE email = ?", (email,)
    ).fetchone()
    if not user:
        flash("Email not found.", "danger")
        return redirect(url_for('auth.forgot_password', lang=lang))

    token = generate_confirmation_token(email)
    reset_url = url_for('auth.reset_password', token=token, lang=lang, _external=True)

    subject = "[TEEtimeVN] Password Reset Request"
    send_email(
        email,
        subject,
        'auth/email/password_reset_email.html',
        user=user,
        reset_url=reset_url
    )

    flash("A password reset link has been sent to your email.", "info")
    # Sau khi gửi link, redirect về login (nhưng login GET sẽ đưa về Home)
    return redirect(url_for('auth.login', lang=lang))


# ---------- Route: Reset Password (Via Token) ----------
@auth_bp.route('/reset-password/<token>/', methods=['GET', 'POST'])
def reset_password(lang, token):
    """
    GET: Hiển thị form đặt mật khẩu mới (nếu token hợp lệ), nếu không hợp lệ flash danger và redirect về forgot-password.
    POST: Xác thực password mới, cập nhật vào DB, flash success, redirect về login.
    """
    email = confirm_token(token)
    if not email:
        flash("The password reset link is invalid or has expired. Please try again.", "danger")
        return redirect(url_for('auth.forgot_password', lang=lang))

    if request.method == 'POST':
        new_password = request.form.get('password')
        confirm_pw = request.form.get('confirm_password')
        if not new_password or not confirm_pw:
            flash("Please fill out all fields.", "warning")
            return redirect(url_for('auth.reset_password', token=token, lang=lang))
        if new_password != confirm_pw:
            flash("Passwords do not match.", "danger")
            return redirect(url_for('auth.reset_password', token=token, lang=lang))

        pw_hash = generate_password_hash(new_password)
        db = get_db()
        db.execute(
            "UPDATE users SET password_hash = ?, updated_at = CURRENT_TIMESTAMP WHERE email = ?",
            (pw_hash, email)
        )
        db.commit()
        flash("Your password has been reset successfully. Please log in.", "success")
        return redirect(url_for('auth.login', lang=lang))

    # GET: Render form reset_password.html
    return render_template('auth/reset_password.html', token=token, lang=lang)


# ---------- Example Admin-Only Route ----------
@auth_bp.route('/admin-dashboard/')
@admin_required
def admin_dashboard(lang):
    """
    Ví dụ route chỉ admin mới truy cập được.
    """
    return render_template('auth/admin_dashboard.html', lang=lang)
