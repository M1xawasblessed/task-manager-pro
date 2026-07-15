from database.db import execute_query, fetch_all, fetch_one
from models.task import Task
from utils.validator import Validator


class TaskService:
    """
    Handles all task operations.
    """

    def add_task(self, title, description, priority="Medium", due_date=None):
        title = Validator.validate_title(title)
        description = Validator.validate_description(description)
        priority = Validator.validate_priority(priority)

        task = Task(
            title=title,
            description=description,
            priority=priority,
            due_date=due_date,
        )

        execute_query(
            """
            INSERT INTO tasks
            (title, description, priority, due_date, status, created_at)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                task.title,
                task.description,
                task.priority,
                task.due_date,
                task.status,
                task.created_at,
            ),
        )

        return task

    def get_all_tasks(self):
        rows = fetch_all(
            """
            SELECT *
            FROM tasks
            ORDER BY id DESC
            """
        )

        return [Task.from_row(row) for row in rows]

    def get_task_by_id(self, task_id):
        task_id = Validator.validate_task_id(task_id)

        row = fetch_one(
            """
            SELECT *
            FROM tasks
            WHERE id = ?
            """,
            (task_id,),
        )

        if row:
            return Task.from_row(row)

        return None

    def search_tasks(self, keyword):
        keyword = keyword.strip()

        rows = fetch_all(
            """
            SELECT *
            FROM tasks
            WHERE title LIKE ?
               OR description LIKE ?
            ORDER BY id DESC
            """,
            (f"%{keyword}%", f"%{keyword}%"),
        )

        return [Task.from_row(row) for row in rows]

    def update_task(
        self,
        task_id,
        title,
        description,
        priority,
        due_date,
    ):
        task_id = Validator.validate_task_id(task_id)
        title = Validator.validate_title(title)
        description = Validator.validate_description(description)
        priority = Validator.validate_priority(priority)

        if self.get_task_by_id(task_id) is None:
            return False

        execute_query(
            """
            UPDATE tasks
            SET
                title=?,
                description=?,
                priority=?,
                due_date=?
            WHERE id=?
            """,
            (
                title,
                description,
                priority,
                due_date,
                task_id,
            ),
        )

        return True

    def delete_task(self, task_id):
        task_id = Validator.validate_task_id(task_id)

        if self.get_task_by_id(task_id) is None:
            return False

        execute_query(
            """
            DELETE FROM tasks
            WHERE id=?
            """,
            (task_id,),
        )

        return True

    def mark_completed(self, task_id):
        task_id = Validator.validate_task_id(task_id)

        if self.get_task_by_id(task_id) is None:
            return False

        execute_query(
            """
            UPDATE tasks
            SET status='Completed'
            WHERE id=?
            """,
            (task_id,),
        )

        return True

    def mark_pending(self, task_id):
        task_id = Validator.validate_task_id(task_id)

        if self.get_task_by_id(task_id) is None:
            return False

        execute_query(
            """
            UPDATE tasks
            SET status='Pending'
            WHERE id=?
            """,
            (task_id,),
        )

        return True

    def filter_by_status(self, status):
        rows = fetch_all(
            """
            SELECT *
            FROM tasks
            WHERE status=?
            ORDER BY id DESC
            """,
            (status,),
        )

        return [Task.from_row(row) for row in rows]

    def filter_by_priority(self, priority):
        priority = Validator.validate_priority(priority)

        rows = fetch_all(
            """
            SELECT *
            FROM tasks
            WHERE priority=?
            ORDER BY id DESC
            """,
            (priority,),
        )

        return [Task.from_row(row) for row in rows]

    def statistics(self):
        total = fetch_one(
            "SELECT COUNT(*) AS total FROM tasks"
        )["total"]

        completed = fetch_one(
            """
            SELECT COUNT(*) AS completed
            FROM tasks
            WHERE status='Completed'
            """
        )["completed"]

        pending = fetch_one(
            """
            SELECT COUNT(*) AS pending
            FROM tasks
            WHERE status='Pending'
            """
        )["pending"]

        high = fetch_one(
            """
            SELECT COUNT(*) AS high
            FROM tasks
            WHERE priority='High'
            """
        )["high"]

        return {
            "total": total,
            "completed": completed,
            "pending": pending,
            "high_priority": high,
        }