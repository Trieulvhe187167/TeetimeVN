# modules/booking.py

from flask import Blueprint, render_template, request, flash, redirect, url_for, g, session
from flask_babel import _
import sqlite3
from datetime import datetime
from modules.courses import get_db, close_db
from functools import wraps

booking_bp = Blueprint('booking', __name__, url_prefix='/<lang>/booking')

# Import mail từ app
def send_booking_email(booking_data):
    """Gửi email thông báo booking mới cho admin"""
    from app import mail
    from flask_mail import Message
    
    # Chuẩn bị nội dung email
    subject = f"[TEEtimeVN] New Booking - {booking_data['course_name']}"
    
    # Tạo HTML content cho email
    html_body = f"""
    <h2>New Booking Received</h2>
    <hr>
    <h3>Customer Information:</h3>
    <ul>
        <li><strong>Name:</strong> {booking_data['fullname']}</li>
        <li><strong>Username:</strong> {booking_data['username']}</li>
        <li><strong>Email:</strong> {booking_data['email']}</li>
        <li><strong>Phone:</strong> {booking_data['phone']}</li>
    </ul>
    
    <h3>Booking Details:</h3>
    <ul>
        <li><strong>Course:</strong> {booking_data['course_name']}</li>
        <li><strong>Play Date:</strong> {booking_data['play_date']}</li>
        <li><strong>Tee Time:</strong> {booking_data['play_time']}</li>
        <li><strong>Number of Players:</strong> {booking_data['players']}</li>
    </ul>
    
    <h3>Services:</h3>
    <ul>
        <li><strong>Caddy:</strong> {'Yes' if booking_data.get('caddy') else 'No'}</li>
        <li><strong>Golf Cart:</strong> {'Yes' if booking_data.get('cart') else 'No'}</li>
        <li><strong>Rent Clubs:</strong> {'Yes' if booking_data.get('rent_clubs') else 'No'}</li>
    </ul>
    
    <h3>Pricing:</h3>
    <ul>
        <li><strong>Green Fee:</strong> {booking_data['green_fee']:,.0f} VND</li>
        <li><strong>Additional Services:</strong> {booking_data['services_fee']:,.0f} VND</li>
        <li><strong>Insurance:</strong> {booking_data['insurance_fee']:,.0f} VND</li>
        <li><strong>Total Amount:</strong> <span style="color: #28a745; font-size: 18px;"><strong>{booking_data['total_amount']:,.0f} VND</strong></span></li>
    </ul>
    
    <hr>
    <p><small>Booking created at: {booking_data['created_at']}</small></p>
    """
    
    # Gửi email cho admin
    admin_email = "levantrieu170604@gmail.com"  # Email admin từ config
    msg = Message(subject, recipients=[admin_email])
    msg.html = html_body
    
    try:
        mail.send(msg)
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

def login_required(f):
    """Decorator để yêu cầu login"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('user_id'):
            flash(_('Please login to access this page.'), 'warning')
            return redirect(url_for('index', lang=kwargs.get('lang', 'en')))
        return f(*args, **kwargs)
    return decorated_function

@booking_bp.before_app_request
def before_request():
    get_db()

@booking_bp.teardown_app_request
def teardown_request(exc):
    close_db()

@booking_bp.route('/', methods=['GET', 'POST'])
def booking(lang):
    db = g.db

    # 1) Load list of courses (id, name)
    courses = db.execute(
        "SELECT gc.id, gci.name FROM golf_course gc "
        "JOIN golf_course_i18n gci ON gc.id=gci.course_id AND gci.lang=?",
        (lang,)
    ).fetchall()

    # 2) Build price‐matrix: { course_id: { weekday:…, weekend:…, twilight:… } }
    tier_prices_by_course = {}
    rows = db.execute("SELECT course_id, tier_type, rack_price_vnd, discount_note FROM course_price").fetchall()
    for r in rows:
        cid = r['course_id']
        tier = r['tier_type'].lower()  # weekday/weekend/twilight
        orig = r['rack_price_vnd'] or 0
        disc_txt = r['discount_note'] or '0%'
        disc = float(disc_txt.replace('%','').replace('-',''))/100
        price = int(orig*(1-disc))
        tier_prices_by_course.setdefault(cid, {})[tier] = price

    # 3) static service prices
    service_prices = {
        'rent_clubs': 1200000,
        'caddy':      500000,
        'cart':       700000,
        'insurance':  100000
    }

    # 4) generate time slots half‐hourly
    time_slots = []
    h,m = 5,30
    while h<18 or (h==18 and m==0):
        time_slots.append(f"{h:02d}:{m:02d}")
        m+=30
        if m==60:
            m=0; h+=1

    if request.method=='POST':
        # Kiểm tra login trước khi xử lý POST
        if not session.get('user_id'):
            flash(_('Please login to book a tee time.'), 'warning')
            return redirect(url_for('booking.booking', lang=lang))
        
        # Kiểm tra nếu là admin
        if session.get('role') == 'admin':
            flash(_('Administrators cannot make bookings.'), 'danger')
            return redirect(url_for('booking.booking', lang=lang))
        
        # Lấy thông tin user từ database
        user_id = session.get('user_id')
        user = db.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
        
        # Lấy thông tin booking từ form
        course_id = request.form.get('course_id')
        play_date = request.form.get('play_date')
        play_time = request.form.get('play_time')
        players = int(request.form.get('players', 1))
        
        # Kiểm tra thời gian booking
        play_datetime = datetime.strptime(f"{play_date} {play_time}", "%Y-%m-%d %H:%M")
        now = datetime.now()
        
        # Kiểm tra nếu booking trong quá khứ
        if play_datetime <= now:
            flash(_('Cannot book for past time. Please select a future time.'), 'danger')
            return redirect(url_for('booking.booking', lang=lang))
        
        # Kiểm tra nếu booking quá gần giờ hiện tại (ít hơn 30 phút)
        time_diff = (play_datetime - now).total_seconds() / 60
        if time_diff < 30:
            flash(_('Please book at least 30 minutes in advance.'), 'warning')
            return redirect(url_for('booking.booking', lang=lang))
        
        # Lấy services đã chọn từ checkbox
        has_caddy = 'caddy' in request.form
        has_cart = 'cart' in request.form
        has_rent_clubs = 'rent_clubs' in request.form
        
        # Lấy thông tin course
        course_info = db.execute(
            "SELECT gc.*, gci.name FROM golf_course gc "
            "JOIN golf_course_i18n gci ON gc.id = gci.course_id "
            "WHERE gc.id = ? AND gci.lang = ?",
            (course_id, lang)
        ).fetchone()
        
        # Tính toán giá
        day_of_week = play_datetime.weekday()
        hour = play_datetime.hour
        
        # Xác định tier
        if hour >= 14:
            tier = 'twilight'
        elif day_of_week in [5, 6]:  # Saturday, Sunday
            tier = 'weekend'
        else:
            tier = 'weekday'
        
        # Tính toán chi phí
        green_fee_unit = tier_prices_by_course.get(int(course_id), {}).get(tier, 0)
        green_fee = green_fee_unit * players
        
        caddy_fee = service_prices['caddy'] * players if has_caddy else 0
        cart_fee = service_prices['cart'] * players if has_cart else 0
        rent_clubs_fee = service_prices['rent_clubs'] * players if has_rent_clubs else 0
        insurance_fee = service_prices['insurance'] * players
        
        services_fee = caddy_fee + cart_fee + rent_clubs_fee
        total_amount = green_fee + services_fee + insurance_fee
        
        try:
            # Lưu booking vào database
            cursor = db.execute(
                """INSERT INTO bookings 
                   (user_id, course_id, play_date, play_time, players, 
                    has_caddy, has_cart, has_rent_clubs,
                    green_fee, services_fee, insurance_fee, total_amount,
                    status, created_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'pending', datetime('now'))""",
                (user_id, course_id, play_date, play_time, players,
                 has_caddy, has_cart, has_rent_clubs,
                 green_fee, services_fee, insurance_fee, total_amount)
            )
            db.commit()
            booking_id = cursor.lastrowid
            
            # Chuẩn bị dữ liệu để gửi email
            booking_data = {
                'booking_id': booking_id,
                'username': user['username'],
                'fullname': user['fullname'] or user['username'],
                'email': user['email'],
                'phone': user['phone'] or 'Not provided',
                'course_name': course_info['name'],
                'play_date': play_date,
                'play_time': play_time,
                'players': players,
                'caddy': has_caddy,
                'cart': has_cart,
                'rent_clubs': has_rent_clubs,
                'green_fee': green_fee,
                'services_fee': services_fee,
                'insurance_fee': insurance_fee,
                'total_amount': total_amount,
                'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            # Gửi email cho admin
            email_sent = send_booking_email(booking_data)
            
            if email_sent:
                flash(_('Booking successful! We have sent a confirmation to our team.'), 'success')
            else:
                flash(_('Booking successful! However, there was an issue sending the notification email.'), 'warning')
            
            # Redirect đến trang booking detail
            return redirect(url_for('booking.booking_detail', lang=lang, booking_id=booking_id))
                
        except Exception as e:
            db.rollback()
            flash(_('An error occurred while processing your booking. Please try again.'), 'danger')
            print(f"Booking error: {e}")
            return redirect(url_for('booking.booking', lang=lang))

    return render_template(
        'booking.html',
        lang=lang,
        courses=courses,
        tier_prices_by_course=tier_prices_by_course,
        service_prices=service_prices,
        time_slots=time_slots,
    )

@booking_bp.route('/my-bookings')
@login_required
def my_bookings(lang):
    """Display user's booking history"""
    db = g.db
    user_id = session.get('user_id')
    
    # Lấy danh sách bookings của user
    bookings = db.execute("""
        SELECT b.*, gc.slug, gci.name as course_name, gci.address,
               datetime(b.created_at, 'localtime') as created_at_display
        FROM bookings b
        JOIN golf_course gc ON b.course_id = gc.id
        JOIN golf_course_i18n gci ON gc.id = gci.course_id AND gci.lang = ?
        WHERE b.user_id = ?
        ORDER BY b.created_at DESC
    """, (lang, user_id)).fetchall()
    
    return render_template(
        'booking_detail.html',
        lang=lang,
        bookings=bookings
    )

@booking_bp.route('/booking/<int:booking_id>')
@login_required
def booking_detail(lang, booking_id):
    """Display single booking details"""
    db = g.db
    user_id = session.get('user_id')
    
    # Lấy thông tin booking
    booking = db.execute("""
        SELECT b.*, 
               gc.slug, gc.par, gc.holes, gc.length_yards,
               gci.name as course_name, gci.address, gci.designer_name,
               u.username, u.email, u.fullname, u.phone,
               datetime(b.created_at, 'localtime') as created_at_display
        FROM bookings b
        JOIN golf_course gc ON b.course_id = gc.id
        JOIN golf_course_i18n gci ON gc.id = gci.course_id AND gci.lang = ?
        JOIN users u ON b.user_id = u.id
        WHERE b.id = ? AND b.user_id = ?
    """, (lang, booking_id, user_id)).fetchone()
    
    if not booking:
        flash(_('Booking not found or you do not have permission to view it.'), 'danger')
        return redirect(url_for('booking.my_bookings', lang=lang))
    
    return render_template(
        'booking_detail_single.html',
        lang=lang,
        booking=booking
    )

@booking_bp.route('/cancel/<int:booking_id>', methods=['POST'])
@login_required
def cancel_booking(lang, booking_id):
    """Cancel a booking"""
    db = g.db
    user_id = session.get('user_id')
    
    # Lấy thông tin booking để kiểm tra quyền và gửi email
    booking = db.execute("""
        SELECT b.*, 
               gc.slug, gci.name as course_name,
               u.username, u.email, u.fullname, u.phone
        FROM bookings b
        JOIN golf_course gc ON b.course_id = gc.id
        JOIN golf_course_i18n gci ON gc.id = gci.course_id AND gci.lang = ?
        JOIN users u ON b.user_id = u.id
        WHERE b.id = ? AND b.user_id = ?
    """, (lang, booking_id, user_id)).fetchone()
    
    if not booking:
        flash(_('Booking not found or you do not have permission to cancel it.'), 'danger')
        return redirect(url_for('booking.my_bookings', lang=lang))
    
    # Kiểm tra nếu booking đã bị cancel hoặc đã hoàn thành
    if booking['status'] == 'cancelled':
        flash(_('This booking has already been cancelled.'), 'warning')
        return redirect(url_for('booking.booking_detail', lang=lang, booking_id=booking_id))
    
    # Kiểm tra thời gian - không cho phép cancel nếu quá gần giờ chơi (ví dụ: 24 giờ)
    play_datetime = datetime.strptime(f"{booking['play_date']} {booking['play_time']}", "%Y-%m-%d %H:%M")
    now = datetime.now()
    hours_until_play = (play_datetime - now).total_seconds() / 3600
    
    if hours_until_play < 24:
        flash(_('Cannot cancel booking less than 24 hours before play time. Please contact us directly.'), 'danger')
        return redirect(url_for('booking.booking_detail', lang=lang, booking_id=booking_id))
    
    try:
        # Cập nhật status thành cancelled
        db.execute(
            "UPDATE bookings SET status = 'cancelled', updated_at = datetime('now') WHERE id = ?",
            (booking_id,)
        )
        db.commit()
        
        # Gửi email thông báo cho admin
        send_cancellation_email(booking)
        
        flash(_('Your booking has been cancelled successfully.'), 'success')
        
    except Exception as e:
        db.rollback()
        flash(_('An error occurred while cancelling your booking. Please try again.'), 'danger')
        print(f"Cancel booking error: {e}")
    
    return redirect(url_for('booking.booking_detail', lang=lang, booking_id=booking_id))

def send_cancellation_email(booking):
    """Gửi email thông báo booking bị cancel cho admin"""
    from app import mail
    from flask_mail import Message
    
    subject = f"[TEEtimeVN] Booking Cancelled - {booking['course_name']}"
    
    html_body = f"""
    <h2 style="color: #dc3545;">Booking Cancellation Notice</h2>
    <hr>
    <h3>Customer Information:</h3>
    <ul>
        <li><strong>Name:</strong> {booking['fullname'] or booking['username']}</li>
        <li><strong>Username:</strong> {booking['username']}</li>
        <li><strong>Email:</strong> {booking['email']}</li>
        <li><strong>Phone:</strong> {booking['phone'] or 'Not provided'}</li>
    </ul>
    
    <h3>Cancelled Booking Details:</h3>
    <ul>
        <li><strong>Booking ID:</strong> #{booking['id']}</li>
        <li><strong>Course:</strong> {booking['course_name']}</li>
        <li><strong>Play Date:</strong> {booking['play_date']}</li>
        <li><strong>Tee Time:</strong> {booking['play_time']}</li>
        <li><strong>Number of Players:</strong> {booking['players']}</li>
        <li><strong>Total Amount:</strong> {booking['total_amount']:,.0f} VND</li>
    </ul>
    
    <h3>Services that were booked:</h3>
    <ul>
        <li><strong>Caddy:</strong> {'Yes' if booking['has_caddy'] else 'No'}</li>
        <li><strong>Golf Cart:</strong> {'Yes' if booking['has_cart'] else 'No'}</li>
        <li><strong>Rent Clubs:</strong> {'Yes' if booking['has_rent_clubs'] else 'No'}</li>
    </ul>
    
    <hr>
    <p style="color: #dc3545;"><strong>This booking has been cancelled by the customer.</strong></p>
    <p><small>Cancelled at: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</small></p>
    """
    
    admin_email = "levantrieu170604@gmail.com"
    msg = Message(subject, recipients=[admin_email])
    msg.html = html_body
    
    try:
        mail.send(msg)
        return True
    except Exception as e:
        print(f"Error sending cancellation email: {e}")
        return False