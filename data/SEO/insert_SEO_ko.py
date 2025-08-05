import sqlite3
from pathlib import Path

# DB 경로
DB_PATH = Path(__file__).resolve().parent / 'teetimevn_dev.db'

# 골프장 ID 및 한국어 이름
golf_courses = [
    (1, "BRG 킹스 아일랜드 골프 리조트"),
    (2, "찌린 스타 골프 & 컨트리 클럽"),
    (3, "헤론 레이크 골프장"),
    (4, "롱비엔 골프 클럽"),
    (5, "스카이레이크 리조트 & 골프 클럽"),
    (6, "FLC 하롱베이 골프 클럽"),
    (7, "뚜언짜우 골프 리조트"),
    (8, "반찌 골프 클럽"),
    (9, "탐다오 골프 리조트"),
    (10, "몽고메리 링크스 베트남"),
    (11, "라구나 랑꼬 골프 클럽"),
    (12, "바나힐 GC 라이트 코스"),
    (13, "베트남 골프 & 컨트리 클럽"),
    (14, "트윈 더브스 골프 클럽"),
    (15, "성소 호짬 골프"),
    (16, "빈펄 푸꾸옥 골프 클럽"),
    (17, "달랏 1200 골프 클럽"),
    (44, "장안 골프 & 컨트리 클럽"),
    (45, "로열 골프장"),
    (46, "드래곤 골프 링크스"),
    (47, "빈펄 하이퐁 골프장"),
    (48, "소노 펠리체 컨트리 클럽 하이퐁"),
    (49, "루비 트리 골프 리조트 하이퐁"),
    (50, "몽까이 국제 골프 클럽"),
    (51, "앰버 힐즈 골프 & 리조트"),
    (52, "스톤 하일랜드 골프 리조트"),
    (53, "옌바이 스타 골프 리조트"),
    (54, "사파 그랜드 골프 코스"),
    (55, "콘힐 골프 & 리조트"),
    (56, "반랑 엠파이어 골프 클럽"),
]

def generate_seo_content(name):
    seo_title = f"{name} 티타임 예약 | TEEtimeVN"
    seo_description = f"{name}는 베트남 최고의 골프장 중 하나입니다. 아름다운 디자인과 탁월한 서비스로 TEEtimeVN에서 손쉽게 티타임을 예약하세요."
    meta_keywords = f"{name}, 베트남 골프장, 골프 예약, 티타임, 골프 리조트"
    fee_note = "요금에는 캐디와 전동카트가 포함됩니다. 공휴일에는 적용되지 않습니다."
    tips_note = "쾌적한 날씨를 위해 아침 일찍 티타임을 예약하는 것을 추천합니다."
    best_season = "10월부터 다음 해 4월까지 (건기)"

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
    lang = 'ko'

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
            print(f"✅ SEO 업데이트 완료: {name}")
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
            print(f"➕ 새로운 SEO 삽입 완료: {name}")

    conn.commit()
    conn.close()
    print("🎉 한국어 SEO 정보 등록 및 업데이트 완료!")

if __name__ == "__main__":
    insert_seo()
