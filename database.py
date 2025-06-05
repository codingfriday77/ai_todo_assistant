import sqlite3

def connect_db():
    conn = sqlite3.connect("tasks.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            date TEXT,
            time TEXT,
            status TEXT DEFAULT 'pending'
        )
    """)
    conn.commit()
    conn.close()

def add_task(task, date=None, time=None):
    conn = sqlite3.connect("tasks.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO tasks (task, date, time) VALUES (?, ?, ?)", (task, date, time))
    conn.commit()
    conn.close()

def get_tasks():
    conn = sqlite3.connect("tasks.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE status = 'pending'")
    rows = cur.fetchall()
    conn.close()
    return rows

def complete_task(task_id):
    conn = sqlite3.connect("tasks.db")
    cur = conn.cursor()
    cur.execute("UPDATE tasks SET status = 'done' WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
