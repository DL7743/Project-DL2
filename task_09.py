from db import connect_db
# 09 Посылка доставлена
# 1. Создайте task_09.py. Для тестовой доставки с ID 99 измените status с ready на done.
# 2. Передайте новый статус и ID отдельно от текста SQL.
# 3. Выведите число изменённых строк. Проверьте через SELECT, что остальные пять доставок не изменились.

# Изменяем через UPDATE и мняем статус с "ready" на "done" для доставки ID 99
sql = """
UPDATE lesson_deliveries
SET status = 'done'
WHERE id = 99;
"""
# выводим число измененных строк
with connect_db() as conn:
    with conn.cursor() as cur:
        cur.execute(sql)
        changed = cur.rowcount
print(f"Изменено строк: {changed}")

# запрашиваем всю таблицу/список словарей, проверяем не измненились ли другие доставки
sql = """
SELECT id, cargo, price, status
FROM lesson_deliveries
ORDER BY id;
"""
with connect_db() as conn:
    with conn.cursor() as cur:
        cur.execute(sql)
        rows = cur.fetchall()
    for row in rows:
        print(row)
     