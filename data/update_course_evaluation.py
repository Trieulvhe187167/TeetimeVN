import sqlite3
conn = sqlite3.connect('data/teetimevn_dev.db')
cur = conn.cursor()

evaluations = [
    (8, 7, 7, 8,  8,  1),
    (7, 7, 7, 8,  7,  2),
    (7, 7, 7, 7,  8,  3),
    (7, 8, 8, 6, 10,  4),
    (8, 8, 8, 8,  8,  5),
    (8, 8, 8,10,  7,  6),
    (8, 8, 8, 8,  9,  7),
    (7,10, 9, 6,  6,  8),
    (8, 8, 7, 9,  8,  9),
    (9, 9, 9, 8, 10, 10),
    (9, 9, 9, 9,  7, 11),
    (9, 9, 9, 9, 10, 12),
    (7, 7, 7, 6,  8, 13),
    (7, 8, 8, 7,  7, 14),
    (9, 9, 9, 8,  9, 15),
    (7, 8, 8, 8,  7, 16),
    (8, 7, 7, 9,  6, 17),
    (7,10, 9, 6,  6, 18),
    (8, 8, 7, 9,  8, 19),
    (9, 9, 9, 8, 10, 20),
    (9, 9, 9, 9,  7, 21),
    (9, 9, 9, 9, 10, 22),
    (7, 7, 7, 6,  8, 23),
    (7, 8, 8, 7,  7, 24),
    (9, 9, 9, 8,  9, 25),
    (7, 8, 8, 8,  7, 26),
    (8, 7, 7, 9,  6, 27),
    (7, 8, 8, 8,  7, 28),
    (8, 7, 7, 9,  6, 29),
    (8, 7, 7, 8,  8, 30),

]


# Cập nhật từng bản ghi
for design, turf, facilities, landscape, playability, course_id in evaluations:
    cur.execute("""
        UPDATE course_evaluation
        SET design_layout         = ?,
            turf_maintenance      = ?,
            facilities_services   = ?,
            landscape_environment = ?,
            playability_access    = ?
        WHERE course_id = ?
    """, (design, turf, facilities, landscape, playability, course_id))

conn.commit()
conn.close()

print("Đã cập nhật thành công tất cả các điểm đánh giá vào database!")
