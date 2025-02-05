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
    "INSERT INTO users (name, age) VALUES (?, ?)",
    ('Alice', 25)
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
conn.commit()

#cur.execute("DELETE FROM users WHERE name = ?", ('Alice', ))
#conn.commit()
cur.close()