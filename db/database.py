import sqlite3

conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    task TEXT,
    done INTEGER DEFAULT 0
)
""")

conn.commit()


def add_task(user_id, task):
    cursor.execute(
        "INSERT INTO tasks (user_id, task, done) VALUES (?, ?, 0)",
        (user_id, task)
    )
    conn.commit()


def get_tasks(user_id):
    cursor.execute(
        "SELECT id, task, done FROM tasks WHERE user_id = ?",
        (user_id,)
    )
    return cursor.fetchall()


def toggle_task(task_id):
    cursor.execute(
        "UPDATE tasks SET done = 1 - done WHERE id = ?",
        (task_id,)
    )
    conn.commit()


def delete_task(task_id):
    cursor.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )
    conn.commit()