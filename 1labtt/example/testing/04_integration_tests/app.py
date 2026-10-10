import os
import json
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)
DB_NAME = "tasks.db"

def init_db(db_path=DB_NAME):
    """Ініціалізація бази даних"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "Missing title"}), 400
    
    title = data["title"]
    

    db_path = app.config.get("DATABASE", DB_NAME)
    
    init_db(db_path) 
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    
    return jsonify({"id": task_id, "title": title}), 201

def export_tasks(file_path, db_path=DB_NAME):
    """Експорт завдань у JSON-файл"""
    if not os.path.exists(db_path):
        data = []
    else:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, title FROM tasks")
        rows = cursor.fetchall()
        conn.close()
        data = [{"id": row[0], "title": row[1]} for row in rows]
    
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)