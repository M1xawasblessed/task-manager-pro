from database.db import execute_query, fetch_all, fetch_one
from models.task import Task
from utils.validator import Validator


class TaskService:

    def add_task(self, title, description):
        """
        Create a new task.
        """

        title = Validator.validate_title(title)
        description = Validator.validate_description(description)

        task = Task(
            title=title,
            description=description,
        )

        execute_query(
            """
            INSERT INTO tasks
            (title, description, status, created_at)
            VALUES (?, ?, ?, ?)
            """,
            (
                task.title,
                task.description,
                task.status,
                task.created_at,
            ),
        )

        return task

    def get_all_tasks(self):
        """
        Return all tasks.
        """

        rows = fetch_all(
            """
            SELECT *
            FROM tasks
            ORDER BY id
            """
        )

        return [Task.from_row(row) for row in rows]

    def get_task_by_id(self, task_id):
        """
        Find task by ID.
        """

        task_id = Validator.validate_task_id(task_id)

        row = fetch_one(
            """
            SELECT *
            FROM tasks
            WHERE id = ?
            """,
            (task_id,),
        )

        if row is None:
            return None

        return Task.from_row(row)

    def search_tasks(self, keyword):
        """
        Search tasks by title.
        """

        keyword = keyword.strip()

        rows = fetch_all(
            """
            SELECT *
            FROM tasks
            WHERE title LIKE ?
            ORDER BY id
            """,
            (f"%{keyword}%",),
        )

        return [Task.from_row(row) for row in rows]

    def update_task(self, task_id, title, description):
        """
        Update an existing task.
        """

        task_id = Validator.validate_task_id(task_id)
        title = Validator.validate_title(title)
        description = Validator.validate_description(description)

        if self.get_task_by_id(task_id) is None:
            return False

        execute_query(
            """
            UPDATE tasks
            SET title = ?, description = ?
            WHERE id = ?
            """,
            (title, description, task_id),
        )

        return True

    def delete_task(self, task_id):
        """
        Delete a task.
        """

        task_id = Validator.validate_task_id(task_id)

        if self.get_task_by_id(task_id) is None:
            return False

        execute_query(
            """
            DELETE FROM tasks
            WHERE id = ?
            """,
            (task_id,),
        )

        return True

    def mark_completed(self, task_id):
        """
        Mark task as completed.
        """

        task_id = Validator.validate_task_id(task_id)

        if self.get_task_by_id(task_id) is None:
            return False

        execute_query(
            """
            UPDATE tasks
            SET status = 'Completed'
            WHERE id = ?
            """,
            (task_id,),
        )

        return True

    def mark_pending(self, task_id):
        """
        Mark task as pending.
        """

        task_id = Validator.validate_task_id(task_id)

        if self.get_task_by_id(task_id) is None:
            return False

        execute_query(
            """
            UPDATE tasks
            SET status = 'Pending'
            WHERE id = ?
            """,
            (task_id,),
        )

        return True