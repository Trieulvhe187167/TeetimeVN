#!/usr/bin/env python3
"""
Script để tạo bảng bookings trong database SQLite
"""

import sqlite3
from pathlib import Path
import sys

# 1) Xác định đường dẫn tới project root và file DB
script_path  = Path(__file__).resolve()
project_root = script_path.parent.parent      # nếu script nằm trong thư mục data/
DB_PATH      = project_root / "data" / "teetimevn_dev.db"

def create_bookings_table():
    """Tạo bảng bookings và các index liên quan"""
    
    # Kiểm tra database có tồn tại không
    if not DB_PATH.exists():
        print(f"❌ Database không tồn tại tại: {DB_PATH}")
        return False
    
    try:
        # Kết nối database
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        print(f"📁 Kết nối database: {DB_PATH}")
        
        # Tạo bảng bookings
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS bookings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                course_id INTEGER NOT NULL,
                play_date DATE NOT NULL,
                play_time TIME NOT NULL,
                players INTEGER NOT NULL DEFAULT 1,
                has_caddy BOOLEAN DEFAULT 0,
                has_cart BOOLEAN DEFAULT 0,
                has_rent_clubs BOOLEAN DEFAULT 0,
                green_fee REAL NOT NULL,
                services_fee REAL NOT NULL,
                insurance_fee REAL NOT NULL,
                total_amount REAL NOT NULL,
                status VARCHAR(20) DEFAULT 'pending',
                notes TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id),
                FOREIGN KEY (course_id) REFERENCES golf_course(id)
            )
        """)
        print("✅ Tạo bảng bookings thành công")
        
        # Tạo các index
        indexes = [
            ("idx_bookings_user_id", "bookings(user_id)"),
            ("idx_bookings_course_id", "bookings(course_id)"),
            ("idx_bookings_play_date", "bookings(play_date)"),
            ("idx_bookings_status", "bookings(status)")
        ]
        
        for index_name, index_def in indexes:
            try:
                cursor.execute(f"CREATE INDEX IF NOT EXISTS {index_name} ON {index_def}")
                print(f"✅ Tạo index {index_name}")
            except sqlite3.Error as e:
                print(f"⚠️  Index {index_name} có thể đã tồn tại: {e}")
        
        # Commit changes
        conn.commit()
        
        # Kiểm tra bảng đã được tạo
        cursor.execute("""
            SELECT name FROM sqlite_master 
            WHERE type='table' AND name='bookings'
        """)
        if cursor.fetchone():
            print("\n✨ Bảng bookings đã được tạo thành công!")
            
            # Hiển thị cấu trúc bảng
            cursor.execute("PRAGMA table_info(bookings)")
            columns = cursor.fetchall()
            print("\n📋 Cấu trúc bảng bookings:")
            print("-" * 60)
            for col in columns:
                print(f"  {col[1]:<20} {col[2]:<15} {'NOT NULL' if col[3] else 'NULL':<10} {f'DEFAULT {col[4]}' if col[4] else ''}")
        
        return True
        
    except sqlite3.Error as e:
        print(f"❌ Lỗi SQLite: {e}")
        return False
    except Exception as e:
        print(f"❌ Lỗi không xác định: {e}")
        return False
    finally:
        if conn:
            conn.close()
            print("\n🔒 Đã đóng kết nối database")

def check_existing_bookings():
    """Kiểm tra xem bảng bookings đã có dữ liệu chưa"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM bookings")
        count = cursor.fetchone()[0]
        
        if count > 0:
            print(f"\n📊 Bảng bookings hiện có {count} bản ghi")
        else:
            print("\n📊 Bảng bookings hiện đang trống")
            
        conn.close()
        return count
    except:
        return 0

if __name__ == "__main__":
    print("🚀 Bắt đầu tạo bảng bookings...")
    print("=" * 60)
    
    if create_bookings_table():
        check_existing_bookings()
        print("\n✅ Hoàn thành! Bảng bookings đã sẵn sàng sử dụng.")
    else:
        print("\n❌ Có lỗi xảy ra khi tạo bảng.")