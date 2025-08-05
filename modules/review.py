# modules/review.py

from flask import Blueprint, request, redirect, url_for, flash, jsonify, session, g, current_app
from flask_babel import _
from modules.courses import get_db, close_db
from werkzeug.utils import secure_filename
from datetime import datetime
import os
import json

review_bp = Blueprint('review', __name__, url_prefix='/<lang>/review')

# File upload settings
UPLOAD_FOLDER = 'static/media/reviews'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@review_bp.before_app_request
def before():
    get_db()

@review_bp.teardown_app_request
def after(exc):
    close_db()

@review_bp.route('/add', methods=['POST'])
def add_review(lang):
    """Thêm hoặc cập nhật review"""
    if not session.get('user_id'):
        flash(_('Please login to write a review'), 'error')
        return redirect(url_for('auth.login', lang=lang))
    
    if session.get('role') == 'admin':
        flash(_('Administrators cannot write reviews'), 'error')
        return redirect(url_for('index', lang=lang))
    
    db = g.db
    course_id = request.form.get('course_id')
    rating = request.form.get('rating')
    comment = request.form.get('comment')
    review_id = request.form.get('review_id')
    
    if not all([course_id, rating, comment]):
        flash(_('Please fill in all required fields'), 'error')
        return redirect(url_for('courses.course_detail', lang=lang, slug=get_course_slug(course_id)))
    
    # Kiểm tra user đã có booking chưa (chỉ khi tạo mới)
    if not review_id:
        has_booking = db.execute("""
            SELECT id FROM bookings 
            WHERE user_id = ? AND course_id = ? 
            AND status IN ('confirmed', 'completed')
            LIMIT 1
        """, (session['user_id'], course_id)).fetchone()
        
        if not has_booking:
            flash(_('You need to book and play at this course before writing a review'), 'error')
            return redirect(url_for('courses.course_detail', lang=lang, slug=get_course_slug(course_id)))
    
    # Xử lý upload ảnh
    images = []
    upload_folder = os.path.join(current_app.root_path, UPLOAD_FOLDER)
    
    # Tạo thư mục nếu chưa tồn tại
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    
    if 'images[]' in request.files:
        files = request.files.getlist('images[]')
        for file in files[:5]:  # Giới hạn 5 ảnh
            if file and file.filename and allowed_file(file.filename):
                # Kiểm tra kích thước file
                file.seek(0, os.SEEK_END)
                file_size = file.tell()
                file.seek(0)
                
                if file_size <= MAX_FILE_SIZE:
                    filename = secure_filename(file.filename)
                    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                    filename = f"{session['user_id']}_{timestamp}_{filename}"
                    filepath = os.path.join(upload_folder, filename)
                    file.save(filepath)
                    images.append(filename)
    
    try:
        if review_id:
            # Update existing review
            existing = db.execute(
                "SELECT * FROM reviews WHERE id = ? AND user_id = ?",
                (review_id, session['user_id'])
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
                """, (int(rating), comment, json.dumps(images) if images else existing['images'], 
                      review_id, session['user_id']))
        else:
            # Create new review
            db.execute("""
                INSERT INTO reviews (course_id, user_id, rating, comment, images, created_at)
                VALUES (?, ?, ?, ?, ?, datetime('now'))
            """, (course_id, session['user_id'], int(rating), comment, 
                  json.dumps(images) if images else None))
        
        db.commit()
        flash(_('Review submitted successfully!'), 'success')
        
    except Exception as e:
        db.rollback()
        flash(_('An error occurred while saving your review'), 'error')
        print(f"Review error: {e}")
    
    # Redirect về course detail
    course_slug = get_course_slug(course_id)
    return redirect(url_for('courses.course_detail', lang=lang, slug=course_slug) + '#reviews')

@review_bp.route('/api/<int:review_id>')
def get_review(lang, review_id):
    """API để lấy thông tin review"""
    db = g.db
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

@review_bp.route('/api/<int:review_id>', methods=['DELETE'])
def delete_review(lang, review_id):
    """API để xóa review"""
    if not session.get('user_id'):
        return jsonify({'success': False, 'message': 'Login required'}), 401
    
    db = g.db
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

@review_bp.route('/api/<int:review_id>/helpful', methods=['POST'])
def toggle_helpful(lang, review_id):
    """API để đánh dấu review hữu ích"""
    if not session.get('user_id'):
        return jsonify({'success': False, 'message': 'Login required'}), 401
    
    db = g.db
    
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

def get_course_slug(course_id):
    """Helper function để lấy slug của course"""
    db = g.db
    course = db.execute(
        "SELECT slug FROM golf_course WHERE id = ?", (course_id,)
    ).fetchone()
    return course['slug'] if course else ''