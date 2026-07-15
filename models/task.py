from datetime import datetime


class Task:
    """
    Represents a task in the Task Manager.
    """

    def __init__(
        self,
        title,
        description,
        priority="Medium",
        due_date=None,
        status="Pending",
        created_at=None,
        task_id=None,
    ):
        self.id = task_id
        self.title = title.strip()
        self.description = description.strip()
        self.priority = priority
        self.due_date = due_date
        self.status = status
        self.created_at = created_at or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @classmethod
    def from_row(cls, row):
        """
        Create a Task object from a SQLite row.
        """

        return cls(
            task_id=row["id"],
            title=row["title"],
            description=row["description"],
            priority=row["priority"],
            due_date=row["due_date"],
            status=row["status"],
            created_at=row["created_at"],
        )

    def to_dict(self):
        """
        Convert task to dictionary.
        """

        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "due_date": self.due_date,
            "status": self.status,
            "created_at": self.created_at,
        }

    def __str__(self):
        due = self.due_date if self.due_date else "No Due Date"

        return (
            f"\nTask ID      : {self.id}"
            f"\nTitle        : {self.title}"
            f"\nDescription  : {self.description}"
            f"\nPriority     : {self.priority}"
            f"\nDue Date     : {due}"
            f"\nStatus       : {self.status}"
            f"\nCreated At   : {self.created_at}"
        )