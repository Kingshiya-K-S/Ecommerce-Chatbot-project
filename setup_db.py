import sqlite3

conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT,
    price REAL
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS chatlogs (
    id INTEGER PRIMARY KEY,
    user_id TEXT,
    message TEXT,
    timestamp TEXT
)''')

# Populate mock data
for i in range(100):
    cursor.execute("INSERT INTO products (name, category, price) VALUES (?, ?, ?)", (f"Product {i+1}", "Electronics", round(100 + i*2.5, 2)))

conn.commit()
conn.close()
