import os
import json
import sqlite3 
import pytest
from app import app, init_db, export_tasks, DB_NAME


@pytest.fixture
def client():
    app.config["TESTING"] = True
    # Використовуємо тимчасову базу даних для тестів
    app.config["DATABASE"] = "test_tasks.db"
    
    init_db("test_tasks.db")
    
    with app.test_client() as client:
        yield client
        
    if os.path.exists("test_tasks.db"):
        os.remove("test_tasks.db")

def test_create_task(client):
    response = client.post("/tasks", json={"title": "Вивчити pytest"})
    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "Вивчити pytest"

def test_create_task_bad_request(client):
    # Тест на POST-запит без поля title
    response = client.post("/tasks", json={})
    assert response.status_code == 400

def test_export_tasks(tmp_path):
    # Тестування експорту у файл за допомогою фікстури tmp_path
    db_path = tmp_path / "test.db"
    conn = sqlite3_test = sqlite3.connect(db_path)
    cursor = sqlite3_test.cursor()
    cursor.execute("CREATE TABLE tasks (id INTEGER PRIMARY KEY, title TEXT)")
    cursor.execute("INSERT INTO tasks (title) VALUES ('Тестове завдання')")
    sqlite3_test.commit()
    sqlite3_test.close()
    
    file_path = tmp_path / "tasks.json"
    export_tasks(file_path, db_path=db_path)
    
    assert file_path.exists()
    content = json.loads(file_path.read_text(encoding="utf-8"))
    assert len(content) == 1
    assert content[0]["title"] == "Тестове завдання"