import sqlite3
from pathlib import Path

# Database path
DATABASE_DIR = Path(__file__).parent
DATABASE_PATH = DATABASE_DIR / "tasks.db"


def get_connection():
    """
    Returns a SQLite connection.
    """
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def create_tables():
    """
    Creates database tables if they do not exist.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT NOT NULL DEFAULT 'Pending',
            created_at TEXT NOT NULL
        )
        """
    )

    connection.commit()
    connection.close()


def execute_query(query, params=()):
    """
    Execute INSERT, UPDATE or DELETE queries.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(query, params)

    connection.commit()
    connection.close()


def fetch_one(query, params=()):
    """
    Returns one row.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(query, params)

    row = cursor.fetchone()

    connection.close()

    return row


def fetch_all(query, params=()):
    """
    Returns all rows.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(query, params)

    rows = cursor.fetchall()

    connection.close()

    return rows