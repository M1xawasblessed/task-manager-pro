from database.db import get_connection
from models.task import Task


class TaskService:
    def add_task(self, title, description):
        task = Task(title=title, description=description)

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO tasks (title, description, status, created_at)
            VALUES (?, ?, ?, ?)
            """,
            (
                task.title,
                task.description,
                task.status,
                task.created_at,
            ),
        )

        connection.commit()
        connection.close()

        return task