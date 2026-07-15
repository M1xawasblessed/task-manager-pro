import sqlite3

DATABASE_NAME = "database/tasks.db"


def get_connection():
    """
    Create and return a database connection.
    """
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    """
    Create tasks table if it does not exist.
    """
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        priority TEXT NOT NULL DEFAULT 'Medium',
        due_date TEXT,
        status TEXT NOT NULL DEFAULT 'Pending',
        created_at TEXT NOT NULL
    )
    """)

    # Migration for older databases
    columns = [row["name"] for row in cursor.execute("PRAGMA table_info(tasks)").fetchall()]

    if "priority" not in columns:
        cursor.execute("""
            ALTER TABLE tasks
            ADD COLUMN priority TEXT NOT NULL DEFAULT 'Medium'
        """)

    if "due_date" not in columns:
        cursor.execute("""
            ALTER TABLE tasks
            ADD COLUMN due_date TEXT
        """)

    connection.commit()
    connection.close()


def execute_query(query, params=()):
    """
    Execute INSERT, UPDATE or DELETE query.
    """
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(query, params)

    connection.commit()
    connection.close()


def fetch_all(query, params=()):
    """
    Fetch all rows.
    """
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(query, params)
    rows = cursor.fetchall()

    connection.close()
    return rows


def fetch_one(query, params=()):
    """
    Fetch one row.
    """
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(query, params)
    row = cursor.fetchone()

    connection.close()
    return row