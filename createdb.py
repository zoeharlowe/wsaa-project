import sqlite3

connection = sqlite3.connect("words.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS words (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    irish TEXT NOT NULL,
    english TEXT NOT NULL
)
""")

connection.commit()
connection.close()

print("Database created.")
