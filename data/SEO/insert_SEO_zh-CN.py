import sqlite3
from pathlib import Path

# Đường dẫn đến database
DB_PATH = Path(__file__).resolve().parent / 'teetimevn_dev.db'

# Danh sách sân golf bằng tiếng Trung (ID, name)
golf_courses = [
    (1, "BRG帝王岛高尔夫度假俱乐部"),
    (2, "芝玲星高尔夫乡村俱乐部"),
    (3, "苍鹭湖高尔夫球场"),
    (4, "龙边高尔夫俱乐部"),
    (5, "天湖高尔夫度假俱乐部"),
    (6, "FLC下龙湾高尔夫球场"),
    (7, "珍珠岛传奇高尔夫"),
    (8, "云池高尔夫俱乐部"),
    (9, "三岛高尔夫度假俱乐部"),
    (10, "蒙哥马利林克斯高尔夫"),
    (11, "朗珂拉古娜高尔夫俱乐部"),
    (12, "巴拿山光影高尔夫俱乐部"),
    (13, "越南高尔夫乡村俱乐部"),
    (14, "双鸽高尔夫俱乐部"),
    (15, "后潭圣地高尔夫"),
    (16, "珍珠富国高尔夫俱乐部"),
    (17, "大叻1200高尔夫俱乐部"),
    (44, "长安高尔夫乡村俱乐部"),
    (45, "皇家高尔夫球场"),
    (46, "龙高尔夫林克斯球场"),
    (47, "海防珍珠高尔夫球场"),
    (48, "海防索诺菲利斯乡村俱乐部"),
    (49, "海防红宝石树高尔夫度假村"),
    (50, "芒街国际高尔夫俱乐部"),
    (51, "琥珀山高尔夫度假村"),
    (52, "石高原高尔夫度假村"),
    (53, "延拜星高尔夫度假村"),
    (54, "萨帕大高尔夫球场"),
    (55, "玉米山高尔夫度假村"),
    (56, "文郎帝国高尔夫俱乐部"),
]

def generate_seo_content(name):
    seo_title = f"{name}在线预订开球时间 | TEEtimeVN"
    seo_description = f"探索{name}，越南顶级高尔夫球场，设计优美，服务一流。通过TEEtimeVN轻松预订开球时间。"
    meta_keywords = f"{name}, 越南高尔夫球场, 在线预订高尔夫, 高尔夫旅游"
    fee_note = "费用包含球童和电瓶车。不适用于节假日。"
    tips_note = "建议选择清晨开球时间，以获得最佳体验与舒适天气。"
    best_season = "每年10月至次年4月（旱季）"

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
    lang = 'zh-CN'

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
            print(f"✅ 已更新 SEO: {name}")
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
            print(f"➕ 已新增 SEO: {name}")

    conn.commit()
    conn.close()
    print("🎉 已完成中文 SEO 内容的插入与更新！")

if __name__ == "__main__":
    insert_seo()
