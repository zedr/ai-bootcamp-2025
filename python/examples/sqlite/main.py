import datetime
import sqlite3

conn = sqlite3.connect("my.db")
cur = conn.cursor()

cur.execute(
    '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,  
        age INTEGER,
        created DATE DEFAULT CURRENT_TIMESTAMP
    )''')
conn.commit()

cur.execute(
    "INSERT INTO users (name, age, created) VALUES (?, ?, ?)",
    ('Alice', 25, datetime.datetime.now() - datetime.timedelta(days=7))
)
conn.commit()

cur.execute("SELECT age, name FROM users")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.execute('''UPDATE users 
SET age = '99' 
WHERE id = 1
''')

#cur.execute("DELETE FROM users WHERE name = ?", ('Alice', ))
#conn.commit()
cur.close()