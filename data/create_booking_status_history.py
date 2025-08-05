#!/usr/bin/env python3
"""
Script để tạo bảng booking_status_history trong database SQLite
Bảng này lưu lịch sử thay đổi status của các booking
"""

import sqlite3
from pathlib import Path
import sys

# 1) Xác định đường dẫn tới project root và file DB
script_path  = Path(__file__).resolve()
project_root = script_path.parent.parent      # nếu script nằm trong thư mục data/
DB_PATH      = project_root / "data" / "teetimevn_dev.db"

def create_booking_status_history_table():
    """Tạo bảng booking_status_history và index"""
    
    # Kiểm tra database có tồn tại không
    if not DB_PATH.exists():
        print(f"❌ Database không tồn tại tại: {DB_PATH}")
        return False
    
    try:
        # Kết nối database
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        print(f"📁 Kết nối database: {DB_PATH}")
        
        # Kiểm tra bảng bookings có tồn tại không
        cursor.execute("""
            SELECT name FROM sqlite_master 
            WHERE type='table' AND name='bookings'
        """)
        if not cursor.fetchone():
            print("❌ Bảng 'bookings' chưa tồn tại. Vui lòng tạo bảng bookings trước!")
            return False
        
        # Tạo bảng booking_status_history
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS booking_status_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                booking_id INTEGER NOT NULL,
                old_status VARCHAR(20),
                new_status VARCHAR(20),
                changed_by VARCHAR(100),
                notes TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (booking_id) REFERENCES bookings(id)
            )
        """)
        print("✅ Tạo bảng booking_status_history thành công")
        
        # Tạo index để tối ưu truy vấn
        try:
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_booking_status_history_booking_id 
                ON booking_status_history(booking_id)
            """)
            print("✅ Tạo index idx_booking_status_history_booking_id")
        except sqlite3.Error as e:
            print(f"⚠️  Index có thể đã tồn tại: {e}")
        
        # Commit changes
        conn.commit()
        
        # Kiểm tra bảng đã được tạo
        cursor.execute("""
            SELECT name FROM sqlite_master 
            WHERE type='table' AND name='booking_status_history'
        """)
        if cursor.fetchone():
            print("\n✨ Bảng booking_status_history đã được tạo thành công!")
            
            # Hiển thị cấu trúc bảng
            cursor.execute("PRAGMA table_info(booking_status_history)")
            columns = cursor.fetchall()
            print("\n📋 Cấu trúc bảng booking_status_history:")
            print("-" * 70)
            print(f"{'Column':<20} {'Type':<20} {'Null':<10} {'Default':<20}")
            print("-" * 70)
            for col in columns:
                col_name = col[1]
                col_type = col[2]
                col_null = "NULL" if not col[3] else "NOT NULL"
                col_default = col[4] if col[4] else ""
                print(f"{col_name:<20} {col_type:<20} {col_null:<10} {col_default:<20}")
            
            # Kiểm tra foreign key
            cursor.execute("PRAGMA foreign_key_list(booking_status_history)")
            fks = cursor.fetchall()
            if fks:
                print("\n🔗 Foreign Keys:")
                for fk in fks:
                    print(f"  - {fk[3]} → {fk[2]}.{fk[4]}")
        
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

def check_existing_history():
    """Kiểm tra xem bảng booking_status_history đã có dữ liệu chưa"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Kiểm tra số lượng record
        cursor.execute("SELECT COUNT(*) FROM booking_status_history")
        count = cursor.fetchone()[0]
        
        if count > 0:
            print(f"\n📊 Bảng booking_status_history hiện có {count} bản ghi")
            
            # Hiển thị 5 record mới nhất
            cursor.execute("""
                SELECT booking_id, old_status, new_status, changed_by, created_at
                FROM booking_status_history
                ORDER BY created_at DESC
                LIMIT 5
            """)
            recent = cursor.fetchall()
            if recent:
                print("\n📝 5 thay đổi status gần nhất:")
                print("-" * 80)
                for r in recent:
                    print(f"  Booking #{r[0]}: {r[1]} → {r[2]} by {r[3]} at {r[4]}")
        else:
            print("\n📊 Bảng booking_status_history hiện đang trống")
            
        conn.close()
        return count
    except Exception as e:
        print(f"⚠️  Không thể kiểm tra dữ liệu: {e}")
        return 0

def add_sample_data():
    """Thêm dữ liệu mẫu để test (optional)"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Kiểm tra có booking nào không
        cursor.execute("SELECT id FROM bookings LIMIT 1")
        booking = cursor.fetchone()
        
        if booking:
            # Thêm một record mẫu
            cursor.execute("""
                INSERT INTO booking_status_history 
                (booking_id, old_status, new_status, changed_by, notes)
                VALUES (?, 'pending', 'confirmed', 'admin', 'Test status change')
            """, (booking[0],))
            conn.commit()
            print(f"\n✅ Đã thêm dữ liệu mẫu cho booking #{booking[0]}")
        else:
            print("\n⚠️  Không có booking nào để test")
            
        conn.close()
    except Exception as e:
        print(f"⚠️  Không thể thêm dữ liệu mẫu: {e}")

if __name__ == "__main__":
    print("🚀 Bắt đầu tạo bảng booking_status_history...")
    print("=" * 70)
    
    if create_booking_status_history_table():
        check_existing_history()
        
        # Hỏi user có muốn thêm dữ liệu mẫu không
        response = input("\n❓ Bạn có muốn thêm dữ liệu mẫu để test không? (y/n): ")
        if response.lower() == 'y':
            add_sample_data()
            
        print("\n✅ Hoàn thành! Bảng booking_status_history đã sẵn sàng sử dụng.")
        print("📌 Bảng này sẽ tự động lưu lịch sử mỗi khi admin thay đổi status booking.")
    else:
        print("\n❌ Có lỗi xảy ra khi tạo bảng.")