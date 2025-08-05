# file: init_db.py
from pathlib import Path
import sqlite3
from werkzeug.security import generate_password_hash

# Đường dẫn tới file SQLite DB (thư mục "data" sẽ nằm cùng cấp với file này)
DB_PATH = Path("data/teetimevn_dev.db")

def init_db():
    # 1. Định nghĩa SQL tạo bảng users (nếu chưa tồn tại)
    sql_create = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL UNIQUE,
        phone TEXT,
        username TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL,
        role TEXT NOT NULL DEFAULT 'user',
        fullname TEXT,
        created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    """

    # 2. Kết nối và tạo bảng
    conn = sqlite3.connect(DB_PATH)
    try:
        conn.execute(sql_create)
        conn.commit()
        print("Đã tạo hoặc kiểm tra thành công bảng 'users'.")
    except sqlite3.Error as e:
        print(f"Lỗi khi tạo bảng users: {e}")
        conn.close()
        return

    # 3. Chuẩn bị chèn 2 tài khoản mẫu (Admin và User)
    try:
        # Tạo hash cho 2 mật khẩu
        admin_plain  = "admin123"
        user_plain   = "12345678"
        admin_hash   = generate_password_hash(admin_plain)
        user_hash    = generate_password_hash(user_plain)

        # Thông tin tài khoản Admin
        email_admin   = "trieulvhe187167@fpt.edu.vn"
        phone_admin   = "0385217604"
        username_admin = "admin"
        role_admin    = "admin"
        fullname_admin = "Administrator"

        # Thông tin tài khoản User thường
        email_user    = "baotrieu300@gmail.com"
        phone_user    = "0385217604"
        username_user = "user"
        role_user     = "user"
        fullname_user = "User"

        cursor = conn.cursor()

        # Dùng INSERT OR IGNORE để tránh lỗi UNIQUE nếu chạy nhiều lần
        cursor.execute(
            """
            INSERT OR IGNORE INTO users
                (email, phone, username, password_hash, role, fullname)
            VALUES (?, ?, ?, ?, ?, ?);
            """,
            (email_admin, phone_admin, username_admin, admin_hash, role_admin, fullname_admin)
        )

        cursor.execute(
            """
            INSERT OR IGNORE INTO users
                (email, phone, username, password_hash, role, fullname)
            VALUES (?, ?, ?, ?, ?, ?);
            """,
            (email_user, phone_user, username_user, user_hash, role_user, fullname_user)
        )

        conn.commit()
        print("Đã chèn dữ liệu mẫu cho Admin và User (nếu chưa tồn tại).")
    except sqlite3.Error as e:
        print(f"Lỗi khi chèn dữ liệu mẫu: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    init_db()
