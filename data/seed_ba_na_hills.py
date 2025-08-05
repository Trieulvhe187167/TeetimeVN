# -*- coding: utf-8 -*-
"""
seed_ba_na_hills.py
--------------------------------------------------
向 teetimevn_dev.db 插入 Ba Na Hills Golf Club 示例数据
语言：vi / zh-CN / zh-TW / en / ko / ja
"""

import sqlite3
from pathlib import Path
from datetime import date

DB_PATH = Path("teetimevn_dev.db")
TODAY = date.today().isoformat()

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# 1) 清理旧记录
cur.execute("DELETE FROM golf_course WHERE slug = ?", ("ba-na-hills-golf-club",))

# 2) golf_course
cur.execute("""
INSERT INTO golf_course
(slug, holes, par, length_yards, opened_year,
 lat, lng, maps_url, scorecard_pdf)
VALUES (?,?,?,?,?,?,?,?,?)
""", (
    "ba-na-hills-golf-club",
    18, 72, 7858, 2016,
    16.0499, 108.0167,
    '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4548.977514045348!2d108.0466116757594!3d16.01753034081862!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31421df6e3a730bb%3A0xd899060c1d60086f!2sBa%20Na%20Hills%20Golf%20Club!5e1!3m2!1szh-CN!2s!4v1746716298259!5m2!1szh-CN!2s" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>',
    "/static/media/ba_na_hills_scorecard.pdf"
))
course_id = cur.lastrowid

# 3) golf_course_i18n
multilang = [
    # lang, name, designer, address,
    # seo_title, seo_desc, meta_keywords,
    # overview, content, fee_note, best_season, tips_note
    ("vi",
     "Ba Na Hills Golf Club",
     "Luke Donald",
     "An Sơn, Hòa Ninh, Hòa Vang, Đà Nẵng",
     "Ba Na Hills Golf Club - Sân golf trên núi tốt nhất Việt Nam",
     "Thông tin, bảng giá và mùa chơi đẹp nhất của Ba Na Hills Golf Club.",
     "ba na hills golf club, sân golf đà nẵng, golf đà nẵng",
     "Sân golf 18 hố par 72 trên sườn núi Bà Nà, do Luke Donald thiết kế.",
     "Ba Na Hills Golf Club nằm ở độ cao 700 m với địa hình uốn lượn tự nhiên...",
     "Phí đã bao gồm caddie, xe điện và thuế 10 %.",
     "Tháng 2-4 & 9-11, thời tiết khô ráo, mát mẻ.",
     "Trang phục lịch sự; tip caddie 300-400k; hủy trước 48 h miễn phí."),
    ("zh-CN",
     "巴拿山高尔夫俱乐部",
     "卢克·唐纳德",
     "An Sơn, Hòa Ninh, Hòa Vang, 岘港",
     "巴拿山高尔夫球场—山地之巅·越南最佳",
     "球场信息、价格、最佳季节一站式了解。",
     "巴拿山高尔夫, 岘港高尔夫, Ba Na Hills Golf",
     "18 洞山地球场，海拔 700 米，卢克·唐纳德设计。",
     "球道依山势而建，俯瞰岘港平原和海岸线...",
     "已含球童、球车及 10 % 税费。",
     "每年 2-4 月、9-11 月气候最佳。",
     "需有领上衣；球童小费 300-400k；48 小时内取消免罚费。"),
    ("zh-TW",
     "巴拿山高爾夫俱樂部",
     "Luke Donald",
     "An Sơn, Hòa Ninh, Hòa Vang, 峴港",
     "越南巴拿山高爾夫—山頂球場資訊",
     "球場詳情、費用與最佳季節。",
     "巴拿山高爾夫, 峴港高爾夫, Ba Na Hills",
     "18 洞 Par 72 山岳球場。",
     "球場位於海拔 700 公尺山腰，可遠眺峴港市區...",
     "含桿弟、球車與 10% 稅金。",
     "2-4 月及 9-11 月較乾爽涼爽。",
     "需穿有領上衣；桿弟小費 300-400k；48 小時前取消免費。"),
    ("en",
     "Ba Na Hills Golf Club",
     "Luke Donald",
     "An Son, Hoa Ninh, Hoa Vang, Da Nang",
     "Ba Na Hills Golf Club | Rates & Course Info",
     "Full rates, season guide and booking tips for Ba Na Hills GC.",
     "ba na hills golf, da nang golf, luke donald design",
     "Mountain-side 18-hole course at 700 m elevation, design by Luke Donald.",
     "Nestled within the Ba Na foothills, the layout features dramatic elevation...",
     "Green fee includes caddie, cart and 10 % VAT.",
     "Best months: Feb-Apr & Sep-Nov, dry and cool.",
     "Collared shirt required; caddie tip 300-400k; free cancel ≥48 h."),
    ("ko",
     "바나 힐스 골프 클럽",
     "Luke Donald",
     "An Sơn, Hoa Ninh, Hòa Vang, 다낭",
     "바나 힐스 골프 클럽 요금·코스 안내",
     "요금, 시즌, 예약 팁 한눈에 보기.",
     "ba na hills golf, 다낭 골프, 루크 도널드",
     "해발 700 m의 18홀 산악 코스.",
     "바나 힐 산자락에 위치, 고저차가 풍부하고 시그니처 홀...",
     "캐디·카트·세금 포함.",
     "2-4월·9-11월이 가장 쾌적.",
     "카라 티셔츠 착용; 캐디팁 300-400k; 48시간 전 취소 무료."),
    ("ja",
     "バナヒルズ・ゴルフクラブ",
     "ルーク・ドナルド",
     "An Sơn, Hòa Ninh, Hòa Vang, ダナン",
     "バナヒルズGC 料金・コース情報",
     "料金・ベストシーズン・予約方法を紹介。",
     "バナヒルズゴルフ, ダナンゴルフ, Luke Donald",
     "標高700 mの18ホール山岳コース。",
     "バナ山麓に位置し、起伏に富んだフェアウェイ...",
     "キャディ・カート・10％税金込み。",
     "2-4月＆9-11月がベストシーズン。",
     "襟付きシャツ必須; キャディチップ300-400k; 48h前キャンセル無料。")
]

cur.executemany("""
INSERT INTO golf_course_i18n
(course_id, lang, name, designer_name, address,
 seo_title, seo_description, meta_keywords,
 overview, content, fee_note, best_season, tips_note)
VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
""", [(course_id, *row) for row in multilang])

# 4) course_price
cur.execute("DELETE FROM course_price WHERE course_id = ?", (course_id,))
prices = [
    ("weekday", 3200000, 2800000, "-12%"),
    ("weekend", 3700000, 3300000, "-11%"),
    ("twilight", 2600000, 2300000, "Twilight -11%")
]
cur.executemany("""
INSERT INTO course_price
(course_id, tier_type, rack_price_vnd, discount_price_vnd, discount_note,
 inc_caddie, inc_cart, inc_tax)
VALUES (?,?,?,?,?,1,1,1)
""", [(course_id, *p) for p in prices])

# 5) fx_rate 示例汇率
cur.execute("DELETE FROM fx_rate WHERE rate_date = ?", (TODAY,))
rates = [("USD", 25500), ("CNY", 3550), ("KRW", 19.5),
         ("JPY", 170), ("TWD", 830)]
cur.executemany("""
INSERT INTO fx_rate (rate_date, currency, rate_to_vnd, source)
VALUES (?,?,?, 'seed')
""", [(TODAY, c, r) for c, r in rates])

conn.commit()
cur.close()
conn.close()
print("✅ 数据已写入 teetimevn_dev.db")
