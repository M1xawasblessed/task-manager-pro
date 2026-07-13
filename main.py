from database.db import create_tables
from services.task_service import TaskService


def show_menu():
    print("\n" + "=" * 40)
    print("        TASK MANAGER PRO")
    print("=" * 40)
    print("1. Add Task")
    print("2. Exit")


def main():
    create_tables()

    task_service = TaskService()

    while True:
        show_menu()

        choice = input("Choose option: ")

        if choice == "1":
            title = input("Title: ").strip()
            description = input("Description: ").strip()

            task_service.add_task(title, description)

            print("\nTask added successfully!")

        elif choice == "2":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid option.")


if __name__ == "__main__":
    main()