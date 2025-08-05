import sqlite3
from pathlib import Path

# Path to the database
DB_PATH = Path(__file__).resolve().parent / 'teetimevn_dev.db'

# List of courses to update (ID, English name)
golf_courses = [
    (1, "BRG Kings Island Golf Resort"),
    (2, "Chi Linh Star Golf & Country Club"),
    (3, "Heron Lake Golf Course"),
    (4, "Long Bien Golf Course"),
    (5, "Sky Lake Resort & Golf Club"),
    (6, "FLC Halong Bay Golf Club"),
    (7, "Tuan Chau Golf Resort"),
    (8, "Van Tri Golf Club"),
    (9, "Tam Dao Golf Resort"),
    (10, "Montgomerie Links Vietnam"),
    (11, "Laguna Lang Co Golf Club"),
    (12, "Ba Na Hills GC Light Course"),
    (13, "Vietnam Golf & Country Club"),
    (14, "Twin Doves Golf Club"),
    (15, "Sanctuary Ho Tram Golf"),
    (16, "Vinpearl Golf Phu Quoc"),
    (17, "The Dalat 1200 Golf Club"),
    (44, "Trang An Golf & Country Club"),
    (45, "Royal Golf Course"),
    (46, "Dragon Golf Links"),
    (47, "Vinpearl Golf Hai Phong"),
    (48, "Sono Felice Country Club Hai Phong"),
    (49, "Ruby Tree Golf Resort Hai Phong"),
    (50, "Mong Cai International Golf Club"),
    (51, "Amber Hills Golf & Resort"),
    (52, "Stone Highland Golf & Resort"),
    (53, "Yen Bai Star Golf & Resort"),
    (54, "Sapa Grand Golf Course"),
    (55, "Corn Hill Golf & Resort"),
    (56, "Van Lang Empire Golf Club"),
]

def generate_seo_content(name):
    seo_title = f"Tee Time Booking at {name} | TEEtimeVN"
    seo_description = f"Discover {name}, a top-tier golf course in Vietnam with beautiful design and excellent services. Book your tee time easily via TEEtimeVN."
    meta_keywords = f"{name.lower()}, book golf tee time, golf course Vietnam, best golf courses"
    fee_note = "Green fee includes caddie and electric cart. Not applicable on public holidays."
    tips_note = "We recommend booking early morning tee times for the best experience and comfortable weather."
    best_season = "October to April (dry season)"

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
    lang = 'en'

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
            print(f"✅ Updated SEO for: {name}")
        else:
            cursor.execute("""
                INSERT INTO golf_course_i18n (
                    course_id, lang, name,
                    seo_title, seo_description, meta_keywords,
                  fee_note, tips_note, best_season
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                course_id, lang, name,
                content["seo_title"],
                content["seo_description"],
                content["meta_keywords"],
                content["fee_note"],
                content["tips_note"],
                content["best_season"]
            ))
            print(f"➕ Inserted new SEO for: {name}")

    conn.commit()
    conn.close()
    print("🎉 Finished inserting/updating SEO for English entries!")

if __name__ == "__main__":
    insert_seo()
