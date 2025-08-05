import sqlite3
import re

# Đường dẫn tới file database SQLite
db_path = "teetimevn_dev.db"  # Đổi thành đường dẫn thật nếu cần

# Kết nối tới database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Lấy tất cả các dòng có chứa ":contentReference[oaicite:"
cursor.execute("""
    SELECT course_id, lang, overview 
    FROM golf_course_i18n 
    WHERE overview LIKE '%:contentReference[oaicite:%'
""")
rows = cursor.fetchall()

# Xử lý và cập nhật từng dòng
updates = []
for course_id, lang, overview in rows:
    cleaned_overview = re.sub(r":contentReference\[oaicite:\d+\]{index=\d+}", "", overview)
    updates.append((cleaned_overview, course_id, lang))

# Cập nhật lại cơ sở dữ liệu
cursor.executemany("""
    UPDATE golf_course_i18n 
    SET overview = ? 
    WHERE course_id = ? AND lang = ?
""", updates)

# Lưu thay đổi và đóng kết nối
conn.commit()
conn.close()

print("Đã xoá các đoạn ':contentReference[oaicite:X]{index=X}' khỏi overview.")
