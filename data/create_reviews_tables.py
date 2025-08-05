# create_reviews_tables.py
# Chạy script này để tạo bảng reviews trong database

import sqlite3
from pathlib import Path
import sys

# Đường dẫn đến database
script_path  = Path(__file__).resolve()
project_root = script_path.parent.parent      # nếu script nằm trong thư mục data/
DB_PATH      = project_root / "data" / "teetimevn_dev.db"

def create_reviews_tables():
    """Tạo các bảng cần thiết cho hệ thống reviews"""
    
    # Kết nối database
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    try:
        # Tạo bảng reviews
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            rating INTEGER NOT NULL CHECK (rating >= 1 AND rating <= 5),
            comment TEXT NOT NULL,
            images TEXT,
            helpful_count INTEGER DEFAULT 0,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (course_id) REFERENCES golf_course (id) ON DELETE CASCADE,
            FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
        )
        """)
        print("✓ Đã tạo bảng 'reviews'")
        
        # Tạo bảng review_helpful
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS review_helpful (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            review_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (review_id) REFERENCES reviews (id) ON DELETE CASCADE,
            FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE,
            UNIQUE(review_id, user_id)
        )
        """)
        print("✓ Đã tạo bảng 'review_helpful'")
        
        # Tạo indexes
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_reviews_course ON reviews(course_id)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_reviews_user ON reviews(user_id)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_reviews_created ON reviews(created_at DESC)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_helpful_review ON review_helpful(review_id)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_helpful_user ON review_helpful(user_id)")
        print("✓ Đã tạo các indexes")
        
        # Tạo trigger để update updated_at
        cursor.execute("""
        CREATE TRIGGER IF NOT EXISTS update_reviews_timestamp 
        AFTER UPDATE ON reviews
        BEGIN
            UPDATE reviews SET updated_at = datetime('now') WHERE id = NEW.id;
        END
        """)
        print("✓ Đã tạo trigger update_reviews_timestamp")
        
        # Kiểm tra và tạo bảng booking_status_history nếu chưa có
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS booking_status_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            booking_id INTEGER NOT NULL,
            old_status VARCHAR(50),
            new_status VARCHAR(50),
            changed_by VARCHAR(100),
            notes TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (booking_id) REFERENCES bookings (id) ON DELETE CASCADE
        )
        """)
        print("✓ Đã tạo bảng 'booking_status_history'")
        
        # Commit changes
        conn.commit()
        print("\n✅ Tất cả các bảng đã được tạo thành công!")
        
        # Kiểm tra các bảng đã tạo
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'review%'")
        tables = cursor.fetchall()
        print("\nCác bảng liên quan đến reviews:")
        for table in tables:
            print(f"  - {table[0]}")
            
    except Exception as e:
        print(f"\n❌ Lỗi khi tạo bảng: {e}")
        conn.rollback()
        
    finally:
        conn.close()

def check_existing_tables():
    """Kiểm tra các bảng hiện có trong database"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    print("\n📋 Danh sách tất cả các bảng trong database:")
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
    tables = cursor.fetchall()
    for table in tables:
        print(f"  - {table[0]}")
    
    conn.close()

if __name__ == "__main__":
    print(f"🔧 Đang tạo các bảng cho hệ thống reviews...")
    print(f"📁 Database path: {DB_PATH}")
    print("-" * 50)
    
    # Kiểm tra database tồn tại
    if not DB_PATH.exists():
        print(f"❌ Không tìm thấy database tại: {DB_PATH}")
        exit(1)
    
    # Tạo các bảng
    create_reviews_tables()
    
    # Kiểm tra lại
    check_existing_tables()