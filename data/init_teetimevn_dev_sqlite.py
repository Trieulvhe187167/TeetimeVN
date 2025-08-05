# -*- coding: utf-8 -*-
"""
init_teetimevn_dev_sqlite.py
------------------------------------------------------------
中文：
    · 如果已存在 teetimevn_dev.db 文件则删除（可选）
    · 创建全新 SQLite 数据库并建 4 张表
越南语:
    · Nếu đã có file teetimevn_dev.db sẽ xoá (tuỳ chọn)
    · Tạo mới CSDL SQLite và tạo 4 bảng
"""

import os
import sqlite3
from pathlib import Path

DB_PATH = Path("teetimevn_dev.db")  # 数据库文件 / File CSDL

# 若想保留旧数据，可注释掉下面两行
if DB_PATH.exists():
    DB_PATH.unlink()        # 删除旧文件 / Xoá file cũ
    print("[INFO] Removed existing teetimevn_dev.db")

# 连接 SQLite（文件不存在会自动创建）
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# 1. golf_course
cursor.executescript("""
DROP TABLE IF EXISTS golf_course;
CREATE TABLE golf_course (
  id            INTEGER PRIMARY KEY AUTOINCREMENT,
  slug          TEXT UNIQUE NOT NULL,
  holes         INTEGER DEFAULT 18,
  par           INTEGER,
  length_yards  INTEGER,
  opened_year   INTEGER,
  lat           REAL,
  lng           REAL,
  maps_url      TEXT,
  scorecard_pdf TEXT,
  created_at    TEXT DEFAULT (datetime('now')),
  updated_at    TEXT DEFAULT (datetime('now'))
);
""")

# 2. golf_course_i18n
cursor.executescript("""
DROP TABLE IF EXISTS golf_course_i18n;
CREATE TABLE golf_course_i18n (
  id             INTEGER PRIMARY KEY AUTOINCREMENT,
  course_id      INTEGER NOT NULL,
  lang           TEXT NOT NULL,
  name           TEXT NOT NULL,
  designer_name  TEXT,
  address        TEXT,
  seo_title      TEXT,
  seo_description TEXT,
  meta_keywords  TEXT,
  overview       TEXT,
  content        TEXT,
  fee_note       TEXT,
  best_season    TEXT,
  tips_note      TEXT,
  UNIQUE(course_id, lang),
  FOREIGN KEY(course_id) REFERENCES golf_course(id) ON DELETE CASCADE
);
""")

# 3. course_price
cursor.executescript("""
DROP TABLE IF EXISTS course_price;
CREATE TABLE course_price (
  id                 INTEGER PRIMARY KEY AUTOINCREMENT,
  course_id          INTEGER NOT NULL,
  tier_type          TEXT CHECK(tier_type IN ('weekday','weekend','twilight')) NOT NULL,
  rack_price_vnd     REAL NOT NULL,
  discount_price_vnd REAL,
  discount_note      TEXT,
  inc_caddie         INTEGER DEFAULT 0,
  inc_cart           INTEGER DEFAULT 0,
  inc_tax            INTEGER DEFAULT 0,
  updated_at         TEXT DEFAULT (datetime('now')),
  FOREIGN KEY(course_id) REFERENCES golf_course(id) ON DELETE CASCADE
);
""")

# 4. fx_rate
cursor.executescript("""
DROP TABLE IF EXISTS fx_rate;
CREATE TABLE fx_rate (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  rate_date   TEXT NOT NULL,       -- YYYY-MM-DD
  currency    TEXT NOT NULL,       -- USD / CNY / …
  rate_to_vnd REAL NOT NULL,
  source      TEXT,
  created_at  TEXT DEFAULT (datetime('now')),
  UNIQUE(rate_date, currency)
);
""")

conn.commit()
cursor.close()
conn.close()
print("[SUCCESS] SQLite database 'teetimevn_dev.db' and 4 tables created!")
