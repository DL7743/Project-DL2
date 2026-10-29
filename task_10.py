from db import connect_db
# 10 Удаление своей тестовой записи
# 1. Создайте task_10.py. Сначала просмотрите доставку 99 через SELECT.
# 2. Удалите только эту тестовую строку через параметризованный запрос по ID.
# 3. Выведите число удалённых строк. Затем повторите поиск: запись не должна находиться, 
# исходные пять строк должны остаться.

# Просматриваем сначала доставку ID 99 через параметризированный запрос оп ID 
sql = """
SELECT id, cargo, price, status
FROM lesson_deliveries
WHERE id = %s;
"""
with connect_db() as conn:
    with conn.cursor() as cur:
# при выполнении указываем именно на доставку ID 99
        cur.execute(sql, (99,))
        rows = cur.fetchall()
    for row in rows:
        print(row)

# через параметризированный запрос удаляем доставку ID 99
sql_delete = """
DELETE FROM lesson_deliveries
WHERE id = %s;
"""
with connect_db() as conn:
    with conn.cursor() as cur:
# при выполнении указываем именно на доставку ID 99, которую уудаляем
        cur.execute(sql_delete, (99, ))
        deleted = cur.rowcount
print(f"Удалено строк: {deleted}")

# выводим список словарей без доставки 99
sql_all = """
SELECT id, cargo, price, status
FROM lesson_deliveries
ORDER BY id;
"""
with connect_db() as conn:
    with conn.cursor() as cur:
        cur.execute(sql_all)
        rows = cur.fetchall()
    for row in rows:
        print(row)