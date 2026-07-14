from dataclasses import dataclass
from datetime import datetime


@dataclass
class Task:
    title: str
    description: str = ""
    status: str = "Pending"
    created_at: str = ""
    task_id: int | None = None

    def __post_init__(self):
        self.title = self.title.strip()
        self.description = self.description.strip()

        if not self.created_at:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def mark_completed(self):
        self.status = "Completed"

    def mark_pending(self):
        self.status = "Pending"

    @classmethod
    def from_row(cls, row):
        """
        Creates a Task object from a SQLite row.
        """

        return cls(
            task_id=row["id"],
            title=row["title"],
            description=row["description"],
            status=row["status"],
            created_at=row["created_at"],
        )

    def __str__(self):
        return (
            f"\n"
            f"{'-' * 40}\n"
            f"ID          : {self.task_id}\n"
            f"Title       : {self.title}\n"
            f"Description : {self.description}\n"
            f"Status      : {self.status}\n"
            f"Created At  : {self.created_at}\n"
            f"{'-' * 40}"
        )