import sqlite3
from datetime import date

conn = sqlite3.connect('data/teetimevn_dev.db')
cursor = conn.cursor()

# 1. Xóa toàn bộ dữ liệu trong fx_rate
cursor.execute("DELETE FROM fx_rate")

# 2. Thêm lại tỷ giá mới
today = date.today().isoformat()
new_rates = [
    ("USD", 25000, "Vietcombank"),
    ("CNY", 3500, "Vietcombank"),
    ("JPY", 180, "Vietcombank"),
    ("KRW", 19, "Vietcombank"),
    ("TWD", 830, "Vietcombank"),
    ("EUR", 26000, "Vietcombank")
]

cursor.executemany(
    "INSERT INTO fx_rate (rate_date, currency, rate_to_vnd, source) VALUES (?, ?, ?, ?)",
    [(today, cur, rate, src) for cur, rate, src in new_rates]
)

conn.commit()
conn.close()
print("✅ Đã xóa và cập nhật lại tỷ giá.")
