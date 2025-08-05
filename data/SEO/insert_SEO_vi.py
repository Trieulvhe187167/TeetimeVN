import sqlite3
from pathlib import Path

# Đường dẫn đến database
DB_PATH = Path(__file__).resolve().parent / 'teetimevn_dev.db'

# Danh sách các sân cần cập nhật SEO (ID, Tên)
golf_courses = [
    (1, 'Khu nghỉ dưỡng & Sân golf BRG Kings Island'),
    (2, 'Câu lạc bộ golf Chi Linh Star'),
    (3, 'Sân golf Heron Lake'),
    (4, 'Sân golf Long Biên'),
    (5, 'Khu nghỉ dưỡng & Sân golf Sky Lake'),
    (6, 'Sân golf FLC Hạ Long Bay'),
    (7, 'Sân golf Khu nghỉ dưỡng Tuần Châu'),
    (8, 'Sân golf Vân Trì'),
    (9, 'Sân golf Tam Đảo'),
    (10, 'Montgomerie Links Việt Nam'),
    (11, 'Sân golf Laguna Lăng Cô'),
    (12, 'Sân golf Ba Na Hills Light'),
    (13, 'Câu lạc bộ golf Việt Nam'),
    (14, 'Sân golf Twin Doves'),
    (15, 'Sân golf Sanctuary Hồ Tràm'),
    (16, 'Sân golf Vinpearl Phú Quốc'),
    (17, 'Sân golf Đà Lạt 1200'),
    (44, 'Tràng An Golf & Country Club'),
    (45, 'Sân golf Hoàng Gia – Royal Golf Course'),
    (46, 'Dragon Golf Links'),
    (47, 'Sân golf Vinpearl Hải Phòng'),
    (48, 'Sono Felice Country Club Hải Phòng'),
    (49, 'Sân golf Ruby Tree Hải Phòng'),
    (50, 'Câu lạc bộ Golf Quốc tế Móng Cái'),
    (51, 'Sân Golf Amber Hills'),
    (52, 'Sân golf Stone Highland Golf & Resort'),
    (53, 'Sân Golf Ngôi Sao Yên Bái'),
    (54, 'Sân Golf Sapa Grand'),
    (55, 'Sân golf Đồi Ngô'),
    (56, 'Sân golf Văn Lang Empire'),
]

def generate_seo_content(name):
    seo_title = f"Đặt giờ chơi tại {name} | TEEtimeVN"
    seo_description = f"Khám phá {name} – sân golf hàng đầu Việt Nam với thiết kế đẹp và dịch vụ chất lượng. Đặt giờ chơi dễ dàng với TEEtimeVN."
    meta_keywords = f"{name.lower()}, đặt sân golf, chơi golf tại Việt Nam, sân golf đẹp"
    overview = f"""{name} là một trong những sân golf nổi bật tại Việt Nam, kết hợp giữa thiết kế tinh tế và không gian thiên nhiên tuyệt đẹp. Sân có đầy đủ tiện nghi, dịch vụ chất lượng, phù hợp cho cả golfer chuyên nghiệp và người mới chơi.

Hệ thống sân gồm nhiều hố tiêu chuẩn quốc tế, cảnh quan xanh mát và điều kiện sân tốt quanh năm. Đây là điểm đến lý tưởng cho những ai yêu thích golf và muốn trải nghiệm đẳng cấp tại Việt Nam."""
    fee_note = "Giá đã bao gồm phí sân, caddie và xe điện. Không áp dụng ngày lễ."
    tips_note = "Nên đặt giờ chơi sớm để có trải nghiệm mượt mà và thời tiết dễ chịu."
    best_season = "Tháng 10 đến tháng 4 năm sau"
    return {
        "seo_title": seo_title,
        "seo_description": seo_description,
        "meta_keywords": meta_keywords,
        "overview": overview,
        "fee_note": fee_note,
        "tips_note": tips_note,
        "best_season": best_season
    }

def insert_seo():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    lang = 'vi'

    for course_id, name in golf_courses:
        content = generate_seo_content(name)

        cursor.execute("SELECT id FROM golf_course_i18n WHERE course_id=? AND lang=?", (course_id, lang))
        exists = cursor.fetchone()

        if exists:
            cursor.execute("""
                UPDATE golf_course_i18n
                SET seo_title=?, seo_description=?, meta_keywords=?,
                    overview=?, fee_note=?, tips_note=?, best_season=?
                WHERE course_id=? AND lang=?
            """, (
                content["seo_title"],
                content["seo_description"],
                content["meta_keywords"],
                content["overview"],
                content["fee_note"],
                content["tips_note"],
                content["best_season"],
                course_id, lang
            ))
            print(f"✅ Đã cập nhật lại SEO cho: {name}")
        else:
            cursor.execute("""
                INSERT INTO golf_course_i18n (
                    course_id, lang, name,
                    seo_title, seo_description, meta_keywords,
                    overview, fee_note, tips_note, best_season
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                course_id, lang, name,
                content["seo_title"],
                content["seo_description"],
                content["meta_keywords"],
                content["overview"],
                content["fee_note"],
                content["tips_note"],
                content["best_season"]
            ))
            print(f"➕ Đã chèn mới SEO cho: {name}")

    conn.commit()
    conn.close()
    print("🎉 Đã hoàn tất việc cập nhật và chèn nội dung SEO!")

if __name__ == "__main__":
    insert_seo()
