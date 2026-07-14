class Validator:

    @staticmethod
    def validate_title(title):
        """
        Validate task title.
        """

        title = title.strip()

        if not title:
            raise ValueError("Title cannot be empty.")

        if len(title) < 3:
            raise ValueError("Title must contain at least 3 characters.")

        if len(title) > 100:
            raise ValueError("Title cannot exceed 100 characters.")

        return title

    @staticmethod
    def validate_description(description):
        """
        Validate task description.
        """

        description = description.strip()

        if len(description) > 500:
            raise ValueError("Description cannot exceed 500 characters.")

        return description

    @staticmethod
    def validate_task_id(task_id):
        """
        Validate task id.
        """

        try:
            task_id = int(task_id)

            if task_id <= 0:
                raise ValueError

            return task_id

        except ValueError:
            raise ValueError("Invalid task ID.")

    @staticmethod
    def validate_status(status):
        """
        Validate task status.
        """

        allowed = ["Pending", "Completed"]

        if status not in allowed:
            raise ValueError("Invalid task status.")

        return status