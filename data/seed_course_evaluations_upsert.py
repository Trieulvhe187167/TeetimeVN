# -*- coding: utf-8 -*-
"""
seed_course_evaluations_upsert.py
--------------------------------
Upsert đánh giá vào bảng course_evaluation.
Nếu course_id đã tồn tại, cập nhật; nếu chưa, insert mới.
"""

import sqlite3
from pathlib import Path
import sys

# 1) Xác định đường dẫn tới project root và file DB
script_path  = Path(__file__).resolve()
project_root = script_path.parent.parent      # nếu script nằm trong thư mục data/
DB_PATH      = project_root / "data" / "teetimevn_dev.db"

if not DB_PATH.exists():
    print(f"❌ Không tìm thấy database tại {DB_PATH}", file=sys.stderr)
    sys.exit(1)

conn = sqlite3.connect(DB_PATH)
cur  = conn.cursor()

# 2) Tạo bảng nếu chưa có...
cur.executescript("""
CREATE TABLE IF NOT EXISTS golf_course (
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    slug TEXT    UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS golf_course_i18n (
    course_id INTEGER NOT NULL,
    lang      TEXT    NOT NULL,
    name      TEXT    NOT NULL,
    PRIMARY KEY(course_id, lang),
    FOREIGN KEY(course_id) REFERENCES golf_course(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS course_evaluation (
    id                    INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id             INTEGER NOT NULL UNIQUE,
    design_layout         INTEGER,
    turf_maintenance      INTEGER,
    facilities_services   INTEGER,
    landscape_environment INTEGER,
    playability_access    INTEGER,
    FOREIGN KEY(course_id) REFERENCES golf_course(id) ON DELETE CASCADE
);
""")

# 3) Dữ liệu đánh giá đã có + bổ sung cho các sân thiếu
evaluations = [
    ("BRG Kings Island Golf Resort",      8, 7, 7, 8,  8),
    ("Chi Linh Star Golf & Country Club", 7, 7, 7, 8,  7),
    ("Heron Lake Golf Course",            7, 7, 7, 7,  8),
    ("Long Bien Golf Course",             7, 8, 8, 6, 10),
    ("Sky Lake Resort & Golf Club",       8, 8, 8, 8,  8),
    ("FLC Halong Bay Golf Club",          8, 8, 8,10,  7),
    ("Laguna Lang Co Golf Club",          9, 9, 9, 9,  7),
    ("Montgomerie Links Vietnam",         9, 9, 9, 8, 10),
    ("Tam Dao Golf Resort",               8, 8, 7, 9,  8),
    ("The Dalat 1200 Golf Club",          8, 7, 7, 9,  6),
    ("Twin Doves Golf Club",              7, 8, 8, 7,  7),
    ("Van Tri Golf Club",                 7,10, 9, 6,  6),
    ("Vietnam Golf & Country Club",       7, 7, 7, 6,  8),
    ("Ba Na Hills GC Light Course",       9, 9, 9, 9, 10),
    ("Tuan Chau Golf Resort",             8, 8, 8, 8,  9),
    ("Sanctuary Ho Tram Golf",            9, 9, 9, 8,  9),
    ("Vinpearl Golf Phu Quoc",            7, 8, 8, 8,  7),
]

# 4) UPSERT từng bản ghi
for name, d, t, f, l, p in evaluations:
    # tìm course_id
    cur.execute("""
        SELECT course_id
          FROM golf_course_i18n
         WHERE lang='en' AND name=?
    """, (name,))
    row = cur.fetchone()
    if not row:
        print(f"⚠️ Không tìm thấy khóa cho sân: {name}", file=sys.stderr)
        continue

    course_id = row[0]

    # chèn hoặc cập nhật
    cur.execute("""
        INSERT INTO course_evaluation
          (course_id, design_layout, turf_maintenance,
           facilities_services, landscape_environment, playability_access)
        VALUES (?, ?, ?, ?, ?, ?)
        ON CONFLICT(course_id) DO UPDATE SET
          design_layout         = excluded.design_layout,
          turf_maintenance      = excluded.turf_maintenance,
          facilities_services   = excluded.facilities_services,
          landscape_environment = excluded.landscape_environment,
          playability_access    = excluded.playability_access
    """, (course_id, d, t, f, l, p))

conn.commit()
cur.close()
conn.close()

print("✅ Đã cập nhật xong đánh giá — các sân mới sẽ được insert, sân cũ sẽ được update.")
