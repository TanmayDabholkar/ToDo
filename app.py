# app.py
from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app, origins="*")
def init_db():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def get_db():
    conn = sqlite3.connect('todo.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return f"Hello Flask!"

@app.route('/get_todo', methods=['GET'])
def get():
    conn = get_db()
    todos = conn.execute('SELECT * FROM todos').fetchall()
    conn.close()
    data = []
    for todo in todos:
        data.append(dict(todo))
    return jsonify(data)

@app.route('/add_todo', methods=['POST'])
def add():
    title = request.json.get('title')
    if title:
        conn = get_db()
        c = conn.cursor()
        c.execute('INSERT INTO todos (title) VALUES (?)', (title,))
        conn.commit()
        conn.close()
    return f"Successfully created todo!!!"

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
