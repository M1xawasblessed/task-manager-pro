from datetime import datetime


class Task:
    def __init__(
        self,
        title,
        description="",
        status="Pending",
        task_id=None,
        created_at=None,
    ):
        self.id = task_id
        self.title = title.strip()
        self.description = description.strip()
        self.status = status
        self.created_at = (
            created_at
            if created_at
            else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )

    def mark_completed(self):
        self.status = "Completed"

    def mark_pending(self):
        self.status = "Pending"

    def __str__(self):
        return (
            f"ID          : {self.id}\n"
            f"Title       : {self.title}\n"
            f"Description : {self.description}\n"
            f"Status      : {self.status}\n"
            f"Created At  : {self.created_at}"
        )