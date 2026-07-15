from datetime import datetime


class Validator:
    """
    Validation helper class.
    """

    @staticmethod
    def validate_title(title):
        if not isinstance(title, str):
            raise ValueError("Title must be a string.")

        title = title.strip()

        if len(title) < 3:
            raise ValueError("Title must contain at least 3 characters.")

        if len(title) > 100:
            raise ValueError("Title cannot exceed 100 characters.")

        return title

    @staticmethod
    def validate_description(description):
        if description is None:
            return ""

        if not isinstance(description, str):
            raise ValueError("Description must be a string.")

        description = description.strip()

        if len(description) > 500:
            raise ValueError("Description cannot exceed 500 characters.")

        return description

    @staticmethod
    def validate_priority(priority):
        allowed = ["Low", "Medium", "High"]

        if priority not in allowed:
            raise ValueError(
                "Priority must be one of: Low, Medium, High."
            )

        return priority

    @staticmethod
    def validate_due_date(due_date):
        """
        Accepts:
            None
            ""
            YYYY-MM-DD
        """

        if due_date is None or due_date == "":
            return None

        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError(
                "Due date format must be YYYY-MM-DD."
            )

        return due_date

    @staticmethod
    def validate_task_id(task_id):
        try:
            task_id = int(task_id)
        except (TypeError, ValueError):
            raise ValueError("Task ID must be an integer.")

        if task_id <= 0:
            raise ValueError("Task ID must be greater than zero.")

        return task_id