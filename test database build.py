import sqlite3
from sqlite3 import Error

conn = sqlite3.connect("football_match_hist.db")

print(conn.total_changes)

cursor=conn.cursor()
'''
cursor.execute("CREATE TABLE IF NOT EXISTS example (id INTEGER, name TEXT, age INTEGER)")
cursor.execute("INSERT INTO example VALUES (1, alice, 20)")
cursor.execute("INSERT INTO example VALUES (2, 'bob', 30)")
cursor.execute("INSERT INTO example VALUES (3, 'eve', 40)")
conn.commit
'''

cursor.execute("Select * from example")
rows = cursor.fetchall()
for row in rows:
    print(row)