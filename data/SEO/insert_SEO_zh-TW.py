import sqlite3
from pathlib import Path

# 資料庫路徑
DB_PATH = Path(__file__).resolve().parent / 'teetimevn_dev.db'

# 球場 ID 與名稱（繁體中文）
golf_courses = [
    (1, "BRG帝王島高爾夫度假俱樂部"),
    (2, "芝玲星高爾夫鄉村俱樂部"),
    (3, "蒼鷺湖高爾夫球場"),
    (4, "龍邊高爾夫俱樂部"),
    (5, "天湖高爾夫度假俱樂部"),
    (6, "FLC下龍灣高爾夫球場"),
    (7, "珍珠島傳奇高爾夫"),
    (8, "雲池高爾夫俱樂部"),
    (9, "三島高爾夫度假俱樂部"),
    (10, "蒙哥馬利連鎖越南高爾夫"),
    (11, "朗哥拉古娜高爾夫俱樂部"),
    (12, "巴拿山光影高爾夫俱樂部"),
    (13, "越南高爾夫鄉村俱樂部"),
    (14, "雙鴿高爾夫俱樂部"),
    (15, "後潭聖地高爾夫"),
    (16, "珍珠富國高爾夫俱樂部"),
    (17, "大叻1200高爾夫俱樂部"),
    (44, "長安高爾夫鄉村俱樂部"),
    (45, "皇家高爾夫球場"),
    (46, "龍高爾夫連鎖球場"),
    (47, "海防珍珠高爾夫球場"),
    (48, "海防索諾菲利斯鄉村俱樂部"),
    (49, "海防紅寶石樹高爾夫度假村"),
    (50, "芒街國際高爾夫俱樂部"),
    (51, "琥珀山高爾夫度假村"),
    (52, "石高原高爾夫度假村"),
    (53, "延拜星高爾夫度假村"),
    (54, "沙壩大高爾夫球場"),
    (55, "玉米山高爾夫度假村"),
    (56, "文郎帝國高爾夫俱樂部"),
]

def generate_seo_content(name):
    seo_title = f"{name} 開球時間預約 | TEEtimeVN"
    seo_description = f"探索 {name}，越南頂級高爾夫球場，設計精美，服務優質。立即透過 TEEtimeVN 輕鬆預約開球時間。"
    meta_keywords = f"{name}, 越南高爾夫球場, 預約開球, 高爾夫旅遊, 高爾夫度假村"
    fee_note = "價格包含球童與電動球車。節假日不適用。"
    tips_note = "建議預約清晨時段開球，可享最佳體驗與天氣。"
    best_season = "10月至翌年4月（乾季）"

    return {
        "seo_title": seo_title,
        "seo_description": seo_description,
        "meta_keywords": meta_keywords,
        "fee_note": fee_note,
        "tips_note": tips_note,
        "best_season": best_season
    }

def insert_seo():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    lang = 'zh-TW'

    for course_id, name in golf_courses:
        content = generate_seo_content(name)

        cursor.execute("SELECT id FROM golf_course_i18n WHERE course_id=? AND lang=?", (course_id, lang))
        exists = cursor.fetchone()

        if exists:
            cursor.execute("""
                UPDATE golf_course_i18n
                SET seo_title=?, seo_description=?, meta_keywords=?,
                    fee_note=?, tips_note=?, best_season=?
                WHERE course_id=? AND lang=?
            """, (
                content["seo_title"],
                content["seo_description"],
                content["meta_keywords"],
                content["fee_note"],
                content["tips_note"],
                content["best_season"],
                course_id, lang
            ))
            print(f"✅ 已更新 SEO：{name}")
        else:
            cursor.execute("""
                INSERT INTO golf_course_i18n (
                    course_id, lang, name,
                    seo_title, seo_description, meta_keywords,
                    fee_note, tips_note, best_season
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                course_id, lang, name,
                content["seo_title"],
                content["seo_description"],
                content["meta_keywords"],
                content["fee_note"],
                content["tips_note"],
                content["best_season"]
            ))
            print(f"➕ 已新增 SEO：{name}")

    conn.commit()
    conn.close()
    print("🎉 已完成繁體中文 SEO 的新增與更新！")

if __name__ == "__main__":
    insert_seo()
