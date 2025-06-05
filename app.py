from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# DB connection
DB = 'ecommerce.db'

def connect_db():
    return sqlite3.connect(DB)

@app.route('/api/search', methods=['POST'])
def search_product():
    data = request.json
    keyword = data.get('query', '')
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT name, category, price FROM products WHERE name LIKE ?", (f"%{keyword}%",))
    results = cursor.fetchall()
    conn.close()
    return jsonify(results)

@app.route('/api/chatlog', methods=['POST'])
def store_chat():
    data = request.json
    user_id = data['user_id']
    message = data['message']
    timestamp = data['timestamp']
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO chatlogs (user_id, message, timestamp) VALUES (?, ?, ?)", (user_id, message, timestamp))
    conn.commit()
    conn.close()
    return jsonify({"status": "saved"})

if __name__ == '__main__':
    app.run(debug=True)
