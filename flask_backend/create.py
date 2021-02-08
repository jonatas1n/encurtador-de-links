import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS enderecos (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    url TEXT NOT NULL,
    counter INTEGER DEFAULT 0 NOT NULL,
    short TEXT
)""")

conn.commit()