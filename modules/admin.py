# file: modules/admin.py

from flask import Blueprint, render_template, request, redirect, url_for, flash, g, session, current_app
from flask_babel import _
import sqlite3, os
from datetime import datetime
import json

def create_admin_bp():
    bp = Blueprint('admin', __name__, url_prefix='/<lang>/admin')

    @bp.before_request
    def check_admin_logged_in():
        """
        Chặn tất cả request vào admin_bp nếu session['role'] không phải 'admin'.
        Nếu không phải admin, redirect về trang courses của ngôn ngữ tương ứng.
        """
        # Lấy lang từ đường dẫn URL (ví dụ '/vi/admin/...')
        lang = request.view_args.get('lang', None)

        # Nếu chưa login hoặc role không phải 'admin', cản truy cập
        if session.get('role') != 'admin':
            flash(_("You do not have permission to access the Admin area."), 'warning')
            return redirect(url_for('courses.course_list', lang=lang))

    @bp.before_app_request
    def before_request():
        """
        Mở kết nối DB trước mỗi request (ứng dụng chung cho admin).
        """
        from modules.courses import get_db
        get_db()

    @bp.teardown_app_request
    def teardown_request(exc):
        """
        Đóng kết nối DB sau mỗi request.
        """
        from modules.courses import close_db
        close_db()

    # -----------------------
    # Dashboard
    # -----------------------
    @bp.route('/')
    def dashboard(lang):
        """Hiển thị trang tổng quan admin với thống kê"""
        # Lấy thống kê tổng quan
        stats = {}
        
        # Tổng số bookings
        total_bookings = g.db.execute("SELECT COUNT(*) as count FROM bookings").fetchone()
        stats['total_bookings'] = total_bookings['count'] if total_bookings else 0
        
        # Tổng số courses
        total_courses = g.db.execute("SELECT COUNT(*) as count FROM golf_course").fetchone()
        stats['total_courses'] = total_courses['count'] if total_courses else 0
        
        # Bookings đang chờ xử lý
        pending = g.db.execute(
            "SELECT COUNT(*) as count FROM bookings WHERE status = 'pending'"
        ).fetchone()
        stats['pending_bookings'] = pending['count'] if pending else 0
        
        # Doanh thu tháng này
        current_month = datetime.now().strftime('%Y-%m')
        revenue = g.db.execute("""
            SELECT SUM(total_amount) as total 
            FROM bookings 
            WHERE strftime('%Y-%m', play_date) = ? 
            AND status = 'confirmed'
        """, (current_month,)).fetchone()
        stats['monthly_revenue'] = revenue['total'] if revenue and revenue['total'] else 0
        
        # Lấy 10 booking gần nhất
        recent_bookings = g.db.execute("""
            SELECT b.id, b.play_date, b.status,
                   u.username, u.fullname,
                   gci.name as course_name
            FROM bookings b
            JOIN users u ON b.user_id = u.id
            JOIN golf_course gc ON b.course_id = gc.id
            JOIN golf_course_i18n gci ON gc.id = gci.course_id AND gci.lang = ?
            ORDER BY b.created_at DESC
            LIMIT 10
        """, (lang,)).fetchall()
        
        # Format recent bookings
        formatted_bookings = []
        for booking in recent_bookings:
            formatted_bookings.append({
                'id': booking['id'],
                'customer_name': booking['fullname'] or booking['username'],
                'course_name': booking['course_name'],
                'play_date': booking['play_date'],
                'status': booking['status']
            })
        
        return render_template('admin/dashboard_content.html', 
                             lang=lang,
                             total_bookings=stats['total_bookings'],
                             total_courses=stats['total_courses'],
                             pending_bookings=stats['pending_bookings'],
                             monthly_revenue=stats['monthly_revenue'],
                             recent_bookings=formatted_bookings)

    # -----------------------
    # I18n routes
    # -----------------------
    @bp.route('/i18n/')
    def i18n_list(lang):
        rows = g.db.execute('SELECT * FROM golf_course_i18n').fetchall()
        return render_template('admin/i18n_list.html', lang=lang, rows=rows)

    @bp.route('/i18n/edit/<int:id>/', methods=('GET', 'POST'))
    def i18n_edit(lang, id):
        row = g.db.execute('SELECT * FROM golf_course_i18n WHERE id=?', (id,)).fetchone()
        if not row:
            flash(_('Translation not found'), 'warning')
            return redirect(url_for('admin.i18n_list', lang=lang))

        if request.method == 'POST':
            fields = [
                'course_id', 'lang', 'name', 'designer_name', 'address',
                'seo_title', 'seo_description', 'meta_keywords',
                'overview', 'content', 'fee_note', 'best_season', 'tips_note'
            ]
            values = [request.form.get(f) for f in fields] + [id]
            set_clause = ', '.join(f"{f}=?" for f in fields)
            g.db.execute(
                f"UPDATE golf_course_i18n SET {set_clause} WHERE id=?",
                values
            )
            g.db.commit()
            flash(_('Translation updated'), 'success')
            return redirect(url_for('admin.i18n_list', lang=lang))

        return render_template('admin/i18n_form.html', lang=lang, row=row)

    # -----------------------
    # FX routes
    # -----------------------
    @bp.route('/fx/')
    def fx_list(lang):
        rows = g.db.execute('SELECT * FROM fx_rate').fetchall()
        return render_template('admin/fx_list.html', lang=lang, rows=rows)

    @bp.route('/fx/edit/<int:id>/', methods=('GET', 'POST'))
    def fx_edit(lang, id):
        row = g.db.execute('SELECT * FROM fx_rate WHERE id=?', (id,)).fetchone()
        if not row:
            flash(_('FX rate not found'), 'warning')
            return redirect(url_for('admin.fx_list', lang=lang))

        if request.method == 'POST':
            fields = ['rate_date', 'currency', 'rate_to_vnd', 'source']
            values = [request.form.get(f) for f in fields] + [id]
            set_clause = ', '.join(f"{f}=?" for f in fields)
            g.db.execute(
                f"UPDATE fx_rate SET {set_clause} WHERE id=?",
                values
            )
            g.db.commit()
            flash(_('FX rate updated'), 'success')
            return redirect(url_for('admin.fx_list', lang=lang))

        return render_template('admin/fx_form.html', lang=lang, row=row)

    # -----------------------
    # Courses routes
    # -----------------------
    @bp.route('/courses/')
    def course_list(lang):
        courses = g.db.execute('SELECT * FROM golf_course').fetchall()
        return render_template('admin/course_list.html', lang=lang, courses=courses)

    @bp.route('/courses/create/', methods=('GET', 'POST'))
    def course_create(lang):
        existing_images = []
        if request.method == 'POST':
            data = (
                request.form['slug'],
                request.form.get('holes') or None,
                request.form.get('par') or None,
                request.form.get('length_yards') or None,
                request.form.get('opened_year') or None,
                request.form.get('lat') or None,
                request.form.get('lng') or None,
                request.form.get('maps_url'),
                request.form.get('scorecard_pdf')
            )
            try:
                g.db.execute(
                    """INSERT INTO golf_course
                       (slug, holes, par, length_yards, opened_year,
                        lat, lng, maps_url, scorecard_pdf)
                       VALUES (?,?,?,?,?,?,?,?,?)""",
                    data
                )
                g.db.commit()
                flash(_('Course created successfully'), 'success')
                return redirect(url_for('admin.course_list', lang=lang))
            except sqlite3.IntegrityError as e:
                flash(_('Error: %(error)s', error=str(e)), 'danger')
        return render_template('admin/course_form.html',
                               lang=lang,
                               course=None,
                               existing_images=existing_images)

    @bp.route('/courses/edit/<int:id>/', methods=('GET', 'POST'))
    def course_edit(lang, id):
        course = g.db.execute('SELECT * FROM golf_course WHERE id=?', (id,)).fetchone()
        if not course:
            flash(_('Course not found'), 'warning')
            return redirect(url_for('admin.course_list', lang=lang))

        if request.method == 'POST':
            upd = (
                request.form['slug'],
                request.form.get('holes') or None,
                request.form.get('par') or None,
                request.form.get('length_yards') or None,
                request.form.get('opened_year') or None,
                request.form.get('lat') or None,
                request.form.get('lng') or None,
                request.form.get('maps_url'),
                request.form.get('scorecard_pdf'),
                id
            )
            try:
                g.db.execute(
                    """UPDATE golf_course
                       SET slug=?, holes=?, par=?, length_yards=?, opened_year=?,
                           lat=?, lng=?, maps_url=?, scorecard_pdf=?
                       WHERE id=?""",
                    upd
                )
                g.db.commit()
                flash(_('Course updated successfully'), 'success')
                return redirect(url_for('admin.course_list', lang=lang))
            except sqlite3.IntegrityError as e:
                flash(_('Error: %(error)s', error=str(e)), 'danger')

        # Lấy danh sách ảnh hiện có trong folder media nếu có
        folder = os.path.join(current_app.static_folder,
                              'media', str(course['slug']), 'gallery')
        existing_images = sorted([
            f for f in os.listdir(folder)
            if os.path.splitext(f)[1].lower() in ('.jpg', '.jpeg', '.png', '.gif')
        ]) if os.path.isdir(folder) else []

        return render_template('admin/course_form.html',
                               lang=lang,
                               course=course,
                               existing_images=existing_images)

    @bp.route('/courses/delete/<int:id>/', methods=('POST',))
    def course_delete(lang, id):
        g.db.execute('DELETE FROM golf_course WHERE id=?', (id,))
        g.db.commit()
        flash(_('Course deleted'), 'success')
        return redirect(url_for('admin.course_list', lang=lang))

    # -----------------------
    # Price routes
    # -----------------------
    @bp.route('/prices/')
    def price_list(lang):
        rows = g.db.execute('SELECT * FROM course_price').fetchall()
        return render_template('admin/price_list.html', lang=lang, rows=rows)

    @bp.route('/prices/create/', methods=('GET', 'POST'))
    def price_create(lang):
        if request.method == 'POST':
            rack = float(request.form.get('rack_price_vnd', 0))
            discount_note = request.form.get('discount_note', '0%').replace('%', '').replace('-', '')
            discount_rate = float(discount_note) / 100 if discount_note else 0
            discount_price = int(rack - rack * discount_rate)

            fields = ['course_id', 'tier_type', 'rack_price_vnd', 'discount_price_vnd',
                      'discount_note', 'inc_caddie', 'inc_cart', 'inc_tax']
            values = [
                request.form.get('course_id'),
                request.form.get('tier_type'),
                rack,
                discount_price,
                request.form.get('discount_note'),
                request.form.get('inc_caddie'),
                request.form.get('inc_cart'),
                request.form.get('inc_tax')
            ]
            placeholders = ','.join('?' for _ in fields)
            g.db.execute(
                f"INSERT INTO course_price ({','.join(fields)}) VALUES ({placeholders})",
                values
            )
            g.db.commit()
            flash(_('Price created'), 'success')
            return redirect(url_for('admin.price_list', lang=lang))
        return render_template('admin/price_form.html', lang=lang, row={})

    @bp.route('/prices/edit/<int:id>/', methods=('GET', 'POST'))
    def price_edit(lang, id):
        row = g.db.execute('SELECT * FROM course_price WHERE id=?', (id,)).fetchone()
        if not row:
            flash(_('Price not found'), 'warning')
            return redirect(url_for('admin.price_list', lang=lang))

        if request.method == 'POST':
            rack = float(request.form.get('rack_price_vnd', 0))
            discount_note = request.form.get('discount_note', '0%').replace('%', '').replace('-', '')
            discount_rate = float(discount_note) / 100 if discount_note else 0
            discount_price = int(rack - rack * discount_rate)

            fields = ['course_id', 'tier_type', 'rack_price_vnd', 'discount_price_vnd',
                      'discount_note', 'inc_caddie', 'inc_cart', 'inc_tax']
            values = [
                request.form.get('course_id'),
                request.form.get('tier_type'),
                rack,
                discount_price,
                request.form.get('discount_note'),
                request.form.get('inc_caddie'),
                request.form.get('inc_cart'),
                request.form.get('inc_tax'),
                id
            ]
            set_clause = ', '.join(f"{f}=?" for f in fields)
            g.db.execute(
                f"UPDATE course_price SET {set_clause} WHERE id=?",
                values
            )
            g.db.commit()
            flash(_('Price updated'), 'success')
            return redirect(url_for('admin.price_list', lang=lang))
        return render_template('admin/price_form.html', lang=lang, row=row)

    @bp.route('/prices/delete/<int:id>/', methods=('POST',))
    def price_delete(lang, id):
        g.db.execute('DELETE FROM course_price WHERE id=?', (id,))
        g.db.commit()
        flash(_('Price deleted'), 'success')
        return redirect(url_for('admin.price_list', lang=lang))

    # -----------------------
    # Evaluation routes (course_evaluation)
    # -----------------------
    @bp.route('/evaluations/')
    def evaluation_list(lang):
        rows = g.db.execute(
            'SELECT * FROM course_evaluation ORDER BY course_id'
        ).fetchall()
        return render_template('admin/evaluation_list.html', lang=lang, rows=rows)

    @bp.route('/evaluations/edit/<int:id>/', methods=('GET', 'POST'))
    def evaluation_edit(lang, id):
        row = g.db.execute(
            'SELECT * FROM course_evaluation WHERE id=?', (id,)
        ).fetchone()
        if not row:
            flash(_('Evaluation not found'), 'warning')
            return redirect(url_for('admin.evaluation_list', lang=lang))

        if request.method == 'POST':
            fields = [
                'course_id',
                'design_layout',
                'turf_maintenance',
                'facilities_services',
                'landscape_environment',
                'playability_access'
            ]
            values = [request.form.get(f) for f in fields] + [id]
            set_clause = ', '.join(f"{f}=?" for f in fields)
            g.db.execute(
                f"UPDATE course_evaluation SET {set_clause} WHERE id=?",
                values
            )
            g.db.commit()
            flash(_('Evaluation updated'), 'success')
            return redirect(url_for('admin.evaluation_list', lang=lang))

        return render_template('admin/evaluation_form.html', lang=lang, row=row)

    @bp.route('/evaluations/delete/<int:id>/', methods=('POST',))
    def evaluation_delete(lang, id):
        g.db.execute('DELETE FROM course_evaluation WHERE id=?', (id,))
        g.db.commit()
        flash(_('Evaluation deleted'), 'success')
        return redirect(url_for('admin.evaluation_list', lang=lang))

    # -----------------------
    # Booking Management routes
    # -----------------------
    @bp.route('/bookings/')
    def booking_list(lang):
        """Hiển thị danh sách tất cả bookings"""
        # Lấy filter parameters
        status_filter = request.args.get('status', '')
        date_filter = request.args.get('date', '')
        course_filter = request.args.get('course_id', '')
        
        # Base query
        query = """
            SELECT b.*, gc.slug, gci.name as course_name, 
                   u.username, u.fullname, u.email, u.phone,
                   datetime(b.created_at) as created_at_formatted
            FROM bookings b
            JOIN golf_course gc ON b.course_id = gc.id
            JOIN golf_course_i18n gci ON gc.id = gci.course_id AND gci.lang = ?
            JOIN users u ON b.user_id = u.id
            WHERE 1=1
        """
        params = [lang]
        
        # Apply filters
        if status_filter:
            query += " AND b.status = ?"
            params.append(status_filter)
        if date_filter:
            query += " AND b.play_date = ?"
            params.append(date_filter)
        if course_filter:
            query += " AND b.course_id = ?"
            params.append(course_filter)
            
        query += " ORDER BY b.created_at DESC"
        
        bookings = g.db.execute(query, params).fetchall()
        
        # Get courses for filter dropdown
        courses = g.db.execute("""
            SELECT gc.id, gci.name 
            FROM golf_course gc
            JOIN golf_course_i18n gci ON gc.id = gci.course_id AND gci.lang = ?
            ORDER BY gci.name
        """, (lang,)).fetchall()
        
        # Calculate statistics
        stats = g.db.execute("""
            SELECT 
                COUNT(*) as total,
                SUM(CASE WHEN status = 'pending' THEN 1 ELSE 0 END) as pending,
                SUM(CASE WHEN status = 'confirmed' THEN 1 ELSE 0 END) as confirmed,
                SUM(CASE WHEN status = 'cancelled' THEN 1 ELSE 0 END) as cancelled,
                SUM(total_amount) as total_revenue
            FROM bookings
        """).fetchone()
        
        return render_template('admin/booking_list.html', 
                             lang=lang, 
                             bookings=bookings,
                             courses=courses,
                             stats=stats,
                             filters={
                                 'status': status_filter,
                                 'date': date_filter,
                                 'course_id': course_filter
                             })

    @bp.route('/bookings/<int:booking_id>/')
    def booking_detail_admin(lang, booking_id):
        """Xem chi tiết booking cho admin"""
        booking = g.db.execute("""
            SELECT b.*, gc.slug, gc.par, gc.holes, gc.length_yards,
                   gci.name as course_name, gci.address, gci.designer_name,
                   u.username, u.fullname, u.email, u.phone,
                   datetime(b.created_at) as created_at_formatted,
                   datetime(b.updated_at) as updated_at_formatted
            FROM bookings b
            JOIN golf_course gc ON b.course_id = gc.id
            JOIN golf_course_i18n gci ON gc.id = gci.course_id AND gci.lang = ?
            JOIN users u ON b.user_id = u.id
            WHERE b.id = ?
        """, (lang, booking_id)).fetchone()
        
        if not booking:
            flash(_('Booking not found'), 'warning')
            return redirect(url_for('admin.booking_list', lang=lang))
        
        # Get status history if exists
        status_history = g.db.execute("""
            SELECT * FROM booking_status_history 
            WHERE booking_id = ? 
            ORDER BY created_at DESC
        """, (booking_id,)).fetchall()
        
        return render_template('admin/booking_detail.html',
                             lang=lang,
                             booking=booking,
                             status_history=status_history)

    @bp.route('/bookings/<int:booking_id>/update-status/', methods=['POST'])
    def update_booking_status(lang, booking_id):
        """Cập nhật status của booking"""
        new_status = request.form.get('status')
        notes = request.form.get('notes', '')
        
        if new_status not in ['pending', 'confirmed', 'cancelled', 'completed']:
            flash(_('Invalid status'), 'danger')
            return redirect(url_for('admin.booking_detail_admin', lang=lang, booking_id=booking_id))
        
        try:
            # Get current booking
            booking = g.db.execute("""
                SELECT b.*, u.email, u.fullname, u.username,
                       gci.name as course_name
                FROM bookings b
                JOIN users u ON b.user_id = u.id
                JOIN golf_course gc ON b.course_id = gc.id
                JOIN golf_course_i18n gci ON gc.id = gci.course_id AND gci.lang = ?
                WHERE b.id = ?
            """, (lang, booking_id)).fetchone()
            
            if not booking:
                flash(_('Booking not found'), 'warning')
                return redirect(url_for('admin.booking_list', lang=lang))
            
            old_status = booking['status']
            
            # Update booking status
            g.db.execute("""
                UPDATE bookings 
                SET status = ?, updated_at = CURRENT_TIMESTAMP
                WHERE id = ?
            """, (new_status, booking_id))
            
            # Log status change
            g.db.execute("""
                INSERT INTO booking_status_history 
                (booking_id, old_status, new_status, changed_by, notes, created_at)
                VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
            """, (booking_id, old_status, new_status, session.get('username'), notes))
            
            g.db.commit()
            
            # Send email notification to user
            if new_status != old_status:
                send_status_update_email(booking, old_status, new_status, notes)
            
            flash(_('Booking status updated successfully'), 'success')
            
        except Exception as e:
            g.db.rollback()
            flash(_('Error updating booking status: %(error)s', error=str(e)), 'danger')
        
        return redirect(url_for('admin.booking_detail_admin', lang=lang, booking_id=booking_id))

    @bp.route('/bookings/<int:booking_id>/add-note/', methods=['POST'])
    def add_booking_note(lang, booking_id):
        """Thêm ghi chú cho booking"""
        notes = request.form.get('notes', '')
        
        try:
            g.db.execute("""
                UPDATE bookings 
                SET notes = ?, updated_at = CURRENT_TIMESTAMP
                WHERE id = ?
            """, (notes, booking_id))
            g.db.commit()
            
            flash(_('Note added successfully'), 'success')
        except Exception as e:
            g.db.rollback()
            flash(_('Error adding note: %(error)s', error=str(e)), 'danger')
        
        return redirect(url_for('admin.booking_detail_admin', lang=lang, booking_id=booking_id))

    # -----------------------
    # Review Management routes với đầy đủ CRUD
    # -----------------------
    @bp.route('/reviews/')
    def review_list(lang):
        """Hiển thị danh sách tất cả reviews"""
        # Lấy filter parameters
        course_filter = request.args.get('course_id', '')
        rating_filter = request.args.get('rating', '')
        search_query = request.args.get('q', '')
        
        # Base query
        query = """
            SELECT r.*, gc.slug, gci.name as course_name,
                   u.username, u.fullname, u.email,
                   datetime(r.created_at) as created_at_formatted
            FROM reviews r
            JOIN golf_course gc ON r.course_id = gc.id
            JOIN golf_course_i18n gci ON gc.id = gci.course_id AND gci.lang = ?
            JOIN users u ON r.user_id = u.id
            WHERE 1=1
        """
        params = [lang]
        
        # Apply filters
        if course_filter:
            query += " AND r.course_id = ?"
            params.append(course_filter)
        if rating_filter:
            query += " AND r.rating = ?"
            params.append(rating_filter)
        if search_query:
            query += " AND (r.comment LIKE ? OR u.username LIKE ? OR u.fullname LIKE ?)"
            search_param = f"%{search_query}%"
            params.extend([search_param, search_param, search_param])
            
        query += " ORDER BY r.created_at DESC"
        
        reviews = g.db.execute(query, params).fetchall()
        
        # Format reviews
        formatted_reviews = []
        for review in reviews:
            review_dict = dict(review)
            review_dict['user_name'] = review['fullname'] or review['username']
            if review['images']:
                try:
                    review_dict['images'] = json.loads(review['images'])
                except:
                    review_dict['images'] = []
            else:
                review_dict['images'] = []
            formatted_reviews.append(review_dict)
        
        # Get courses for filter
        courses = g.db.execute("""
            SELECT gc.id, gci.name 
            FROM golf_course gc
            JOIN golf_course_i18n gci ON gc.id = gci.course_id AND gci.lang = ?
            ORDER BY gci.name
        """, (lang,)).fetchall()
        
        # Calculate statistics
        stats = g.db.execute("""
            SELECT 
                COUNT(*) as total,
                AVG(rating) as avg_rating,
                SUM(CASE WHEN rating = 5 THEN 1 ELSE 0 END) as five_star,
                SUM(CASE WHEN rating = 4 THEN 1 ELSE 0 END) as four_star,
                SUM(CASE WHEN rating = 3 THEN 1 ELSE 0 END) as three_star,
                SUM(CASE WHEN rating = 2 THEN 1 ELSE 0 END) as two_star,
                SUM(CASE WHEN rating = 1 THEN 1 ELSE 0 END) as one_star
            FROM reviews
        """).fetchone()
        
        return render_template('admin/review_list.html',
                             lang=lang,
                             reviews=formatted_reviews,
                             courses=courses,
                             stats=stats,
                             filters={
                                 'course_id': course_filter,
                                 'rating': rating_filter,
                                 'q': search_query
                             })

    @bp.route('/reviews/create/', methods=['GET', 'POST'])
    def review_create(lang):
        """Admin tạo review mới"""
        if request.method == 'POST':
            try:
                # Lấy dữ liệu từ form
                course_id = request.form.get('course_id')
                user_id = request.form.get('user_id')
                rating = request.form.get('rating')
                comment = request.form.get('comment')
                
                # Validate
                if not all([course_id, user_id, rating, comment]):
                    flash(_('Please fill in all required fields'), 'error')
                    return redirect(url_for('admin.review_create', lang=lang))
                
                # Insert review
                g.db.execute("""
                    INSERT INTO reviews (course_id, user_id, rating, comment, created_at)
                    VALUES (?, ?, ?, ?, datetime('now'))
                """, (course_id, user_id, int(rating), comment))
                g.db.commit()
                
                flash(_('Review created successfully'), 'success')
                return redirect(url_for('admin.review_list', lang=lang))
                
            except Exception as e:
                g.db.rollback()
                flash(_('Error creating review: %(error)s', error=str(e)), 'danger')
        
        # GET: Hiển thị form
        courses = g.db.execute("""
            SELECT gc.id, gci.name 
            FROM golf_course gc
            JOIN golf_course_i18n gci ON gc.id = gci.course_id AND gci.lang = ?
            ORDER BY gci.name
        """, (lang,)).fetchall()
        
        users = g.db.execute("""
            SELECT id, username, fullname, email 
            FROM users 
            ORDER BY username
        """).fetchall()
        
        return render_template('admin/review_form.html',
                             lang=lang,
                             courses=courses,
                             users=users,
                             review=None)

    @bp.route('/reviews/<int:review_id>/edit/', methods=['GET', 'POST'])
    def review_edit(lang, review_id):
        """Admin sửa review"""
        # Lấy review hiện tại
        review = g.db.execute("""
            SELECT r.*, u.username, u.fullname, gci.name as course_name
            FROM reviews r
            JOIN users u ON r.user_id = u.id
            JOIN golf_course gc ON r.course_id = gc.id
            JOIN golf_course_i18n gci ON gc.id = gci.course_id AND gci.lang = ?
            WHERE r.id = ?
        """, (lang, review_id)).fetchone()
        
        if not review:
            flash(_('Review not found'), 'warning')
            return redirect(url_for('admin.review_list', lang=lang))
        
        if request.method == 'POST':
            try:
                # Update review
                rating = request.form.get('rating')
                comment = request.form.get('comment')
                
                g.db.execute("""
                    UPDATE reviews 
                    SET rating = ?, comment = ?, updated_at = datetime('now')
                    WHERE id = ?
                """, (int(rating), comment, review_id))
                g.db.commit()
                
                flash(_('Review updated successfully'), 'success')
                return redirect(url_for('admin.review_list', lang=lang))
                
            except Exception as e:
                g.db.rollback()
                flash(_('Error updating review: %(error)s', error=str(e)), 'danger')
        
        # GET: Hiển thị form với dữ liệu hiện tại
        courses = g.db.execute("""
            SELECT gc.id, gci.name 
            FROM golf_course gc
            JOIN golf_course_i18n gci ON gc.id = gci.course_id AND gci.lang = ?
            ORDER BY gci.name
        """, (lang,)).fetchall()
        
        users = g.db.execute("""
            SELECT id, username, fullname, email 
            FROM users 
            ORDER BY username
        """).fetchall()
        
        # Format review data
        review_dict = dict(review)
        if review['images']:
            try:
                review_dict['images'] = json.loads(review['images'])
            except:
                review_dict['images'] = []
        else:
            review_dict['images'] = []
            
        return render_template('admin/review_form.html',
                             lang=lang,
                             courses=courses,
                             users=users,
                             review=review_dict)

    @bp.route('/reviews/<int:review_id>/delete/', methods=['POST'])
    def delete_review_admin(lang, review_id):
        """Admin xóa review"""
        review = g.db.execute(
            "SELECT * FROM reviews WHERE id = ?", (review_id,)
        ).fetchone()
        
        if not review:
            flash(_('Review not found'), 'warning')
            return redirect(url_for('admin.review_list', lang=lang))
        
        try:
            # Xóa ảnh nếu có
            if review['images']:
                upload_folder = os.path.join(current_app.root_path, 'static/media/reviews')
                images = json.loads(review['images'])
                for img in images:
                    try:
                        os.remove(os.path.join(upload_folder, img))
                    except:
                        pass
            
            # Xóa review và helpful votes
            g.db.execute("DELETE FROM review_helpful WHERE review_id = ?", (review_id,))
            g.db.execute("DELETE FROM reviews WHERE id = ?", (review_id,))
            g.db.commit()
            
            flash(_('Review deleted successfully'), 'success')
        except Exception as e:
            g.db.rollback()
            flash(_('Error deleting review: %(error)s', error=str(e)), 'danger')
        
        return redirect(url_for('admin.review_list', lang=lang))

    @bp.route('/reviews/<int:review_id>/')
    def review_detail_admin(lang, review_id):
        """Xem chi tiết review"""
        review = g.db.execute("""
            SELECT r.*, 
                   gc.slug, gci.name as course_name, gci.address,
                   u.username, u.fullname, u.email, u.phone,
                   datetime(r.created_at) as created_at_formatted,
                   datetime(r.updated_at) as updated_at_formatted
            FROM reviews r
            JOIN golf_course gc ON r.course_id = gc.id
            JOIN golf_course_i18n gci ON gc.id = gci.course_id AND gci.lang = ?
            JOIN users u ON r.user_id = u.id
            WHERE r.id = ?
        """, (lang, review_id)).fetchone()
        
        if not review:
            flash(_('Review not found'), 'warning')
            return redirect(url_for('admin.review_list', lang=lang))
        
        # Format review
        review_dict = dict(review)
        if review['images']:
            try:
                review_dict['images'] = json.loads(review['images'])
            except:
                review_dict['images'] = []
        else:
            review_dict['images'] = []
        
        # Get helpful votes
        helpful_users = g.db.execute("""
            SELECT u.username, u.fullname, rh.created_at
            FROM review_helpful rh
            JOIN users u ON rh.user_id = u.id
            WHERE rh.review_id = ?
            ORDER BY rh.created_at DESC
        """, (review_id,)).fetchall()
        
        return render_template('admin/review_detail.html',
                             lang=lang,
                             review=review_dict,
                             helpful_users=helpful_users)

    @bp.route('/reviews/bulk-action/', methods=['POST'])
    def review_bulk_action(lang):
        """Xử lý bulk actions cho reviews"""
        action = request.form.get('action')
        review_ids = request.form.getlist('review_ids[]')
        
        if not review_ids:
            flash(_('No reviews selected'), 'warning')
            return redirect(url_for('admin.review_list', lang=lang))
        
        try:
            if action == 'delete':
                # Xóa nhiều reviews
                for review_id in review_ids:
                    review = g.db.execute(
                        "SELECT images FROM reviews WHERE id = ?", 
                        (review_id,)
                    ).fetchone()
                    
                    if review and review['images']:
                        # Xóa ảnh
                        upload_folder = os.path.join(current_app.root_path, 'static/media/reviews')
                        images = json.loads(review['images'])
                        for img in images:
                            try:
                                os.remove(os.path.join(upload_folder, img))
                            except:
                                pass
                
                # Xóa reviews và helpful votes
                placeholders = ','.join('?' * len(review_ids))
                g.db.execute(f"DELETE FROM review_helpful WHERE review_id IN ({placeholders})", review_ids)
                g.db.execute(f"DELETE FROM reviews WHERE id IN ({placeholders})", review_ids)
                g.db.commit()
                
                flash(_('%(count)d reviews deleted successfully', count=len(review_ids)), 'success')
                
            elif action == 'approve':
                # Có thể thêm field approved trong database nếu cần
                flash(_('Reviews approved'), 'success')
                
        except Exception as e:
            g.db.rollback()
            flash(_('Error processing bulk action: %(error)s', error=str(e)), 'danger')
        
        return redirect(url_for('admin.review_list', lang=lang))

    return bp

# Helper function để gửi email thông báo status (ĐẶT NGOÀI create_admin_bp)
def send_status_update_email(booking, old_status, new_status, notes):
    """Gửi email thông báo khi status booking thay đổi"""
    from app import mail
    from flask_mail import Message
    from flask_babel import _
    
    status_messages = {
        'confirmed': _('Your booking has been confirmed!'),
        'cancelled': _('Your booking has been cancelled.'),
        'pending': _('Your booking is pending review.'),
        'completed': _('Your booking has been completed. Thank you!')
    }
    
    subject = f"[TEEtimeVN] Booking #{booking['id']} - {status_messages.get(new_status, 'Status Updated')}"
    
    html_body = f"""
    <h2>Booking Status Update</h2>
    <p>Dear {booking['fullname'] or booking['username']},</p>
    
    <p>Your booking status has been updated:</p>
    
    <div style="background: #f8f9fa; padding: 20px; border-radius: 5px; margin: 20px 0;">
        <h3>Booking Details:</h3>
        <ul>
            <li><strong>Booking ID:</strong> #{booking['id']}</li>
            <li><strong>Course:</strong> {booking['course_name']}</li>
            <li><strong>Date:</strong> {booking['play_date']}</li>
            <li><strong>Time:</strong> {booking['play_time']}</li>
            <li><strong>Previous Status:</strong> <span style="color: #6c757d;">{old_status.title()}</span></li>
            <li><strong>New Status:</strong> <span style="color: {'#28a745' if new_status == 'confirmed' else '#dc3545' if new_status == 'cancelled' else '#ffc107'};">{new_status.title()}</span></li>
        </ul>
        
        {f'<p><strong>Admin Notes:</strong> {notes}</p>' if notes else ''}
    </div>
    
    <p>If you have any questions, please contact us.</p>
    
    <p>Best regards,<br>TEEtimeVN Team</p>
    """
    
    msg = Message(subject, recipients=[booking['email']])
    msg.html = html_body
    
    try:
        mail.send(msg)
    except Exception as e:
        print(f"Error sending status update email: {e}")

# Tạo instance admin_bp
admin_bp = create_admin_bp()