import sqlite3
from pathlib import Path

# Đường dẫn đến database
DB_PATH = Path(__file__).resolve().parent / "teetimevn_dev.db"


def create_and_insert_static_page_seo():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Tạo bảng nếu chưa có
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS static_page_i18n (
            page_id TEXT NOT NULL,
            lang TEXT NOT NULL,
            title TEXT,
            description TEXT,
            keywords TEXT,
            PRIMARY KEY (page_id, lang)
        );
    """)

    # Danh sách dữ liệu SEO
    data = [
        ('home', 'vi',
         'TEEtimeVN - Đặt sân golf tại Việt Nam',
         'TEEtimeVN là nền tảng đặt sân golf thông minh, hỗ trợ đa ngôn ngữ. Khám phá hàng chục sân golf tại Việt Nam và đặt giờ chơi dễ dàng.',
         'đặt sân golf, tee time, tee time golf, đặt giờ chơi golf, booking sân golf, tee booking, tee time vietnam, đặt sân golf online, sân golf gần tôi, sân golf mở cửa hôm nay, giờ chơi golf tốt nhất, cách đặt tee time nhanh chóng, tee time giá rẻ, sân golf Hà Nội, sân golf Sài Gòn, sân golf Đà Nẵng, sân golf Vũng Tàu, đặt sân golf miền Bắc, sân golf miền Nam, đánh giá sân golf, sân golf đẹp, sân golf nổi tiếng Việt Nam, top sân golf, sân golf cho người mới, sân golf cao cấp, golf course vietnam, book tee time vietnam, play golf vietnam, golf booking app, golf tee time platform, sân golf tổ chức giải đấu, sân golf ban đêm, sân golf giá tốt cuối tuần, ưu đãi booking sân golf'),

        ('home', 'en',
         'TEEtimeVN - Book Golf Courses in Vietnam',
         'TEEtimeVN is a smart platform for booking golf tee times across Vietnam, with multilingual support and competitive pricing.',
         'book golf course, tee time, golf vietnam, play golf, vietnam golf, book tee time, golf near me, golf course booking, tee time online, best golf courses, golf app, top golf courses in vietnam'),

        ('home', 'zh-CN',
         'TEEtimeVN - 越南高尔夫球场预订平台',
         'TEEtimeVN 是越南领先的高尔夫球场预订平台，支持多语言和快速预订。',
         '高尔夫, 越南高尔夫, 高尔夫球场预订, tee time 越南, 在线预订高尔夫, 打高尔夫, 越南 tee time'),

        ('home', 'zh-TW',
         'TEEtimeVN - 越南高爾夫球場預訂平台',
         'TEEtimeVN 是越南領先的高爾夫球場預訂平台，支援多語系與快速預約開球時間。',
         '高爾夫, 預訂球場, tee time 越南, 越南打高爾夫, 高爾夫線上預約, 高爾夫球場平台'),

        ('home', 'ja',
         'TEEtimeVN - ベトナムのゴルフ場予約サイト',
         'TEEtimeVNはベトナム全土のゴルフ場を多言語対応で簡単に予約できるスマートプラットフォームです。',
         'ベトナム ゴルフ, ゴルフ予約, ゴルフ場, tee time ベトナム, ゴルフコース ベトナム, ゴルフプレイ, ゴルフ 予約サイト'),

        ('home', 'ko',
         'TEEtimeVN - 베트남 골프장 예약 플랫폼',
         'TEEtimeVN은 베트남 전역의 골프장을 다양한 언어로 쉽게 예약할 수 있는 스마트 플랫폼입니다.',
         '골프 예약, tee time, 베트남 골프, 골프장 예약, 골프 코스, 온라인 골프 예약, 베트남 tee time')
    ]

    # Thêm từng bản ghi
    for record in data:
        cursor.execute("""
            INSERT OR REPLACE INTO static_page_i18n (page_id, lang, title, description, keywords)
            VALUES (?, ?, ?, ?, ?);
        """, record)

    conn.commit()
    conn.close()
    print("✅ Đã tạo bảng và thêm dữ liệu SEO cho trang chủ thành công.")

if __name__ == "__main__":
    create_and_insert_static_page_seo()
