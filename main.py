from database.db import create_tables
from services.task_service import TaskService


service = TaskService()


def show_menu():
    print("\n" + "=" * 40)
    print("        TASK MANAGER PRO")
    print("=" * 40)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Search Tasks")
    print("4. Update Task")
    print("5. Mark Completed")
    print("6. Mark Pending")
    print("7. Delete Task")
    print("8. Exit")


def add_task():
    print("\n--- Add Task ---")

    title = input("Title: ")
    description = input("Description: ")

    try:
        service.add_task(title, description)
        print("\nTask added successfully!")

    except ValueError as error:
        print(f"\nError: {error}")


def view_tasks():
    print("\n--- All Tasks ---")

    tasks = service.get_all_tasks()

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        print(task)


def search_tasks():
    print("\n--- Search Tasks ---")

    keyword = input("Keyword: ")

    tasks = service.search_tasks(keyword)

    if not tasks:
        print("\nNo matching tasks found.")
        return

    for task in tasks:
        print(task)

def update_task():
    print("\n--- Update Task ---")

    task_id = input("Task ID: ")
    title = input("New Title: ")
    description = input("New Description: ")

    try:
        if service.update_task(task_id, title, description):
            print("\nTask updated successfully!")
        else:
            print("\nTask not found.")

    except ValueError as error:
        print(f"\nError: {error}")


def mark_completed():
    print("\n--- Mark Completed ---")

    task_id = input("Task ID: ")

    try:
        if service.mark_completed(task_id):
            print("\nTask marked as completed.")
        else:
            print("\nTask not found.")

    except ValueError as error:
        print(f"\nError: {error}")


def mark_pending():
    print("\n--- Mark Pending ---")

    task_id = input("Task ID: ")

    try:
        if service.mark_pending(task_id):
            print("\nTask marked as pending.")
        else:
            print("\nTask not found.")

    except ValueError as error:
        print(f"\nError: {error}")


def delete_task():
    print("\n--- Delete Task ---")

    task_id = input("Task ID: ")

    try:
        if service.delete_task(task_id):
            print("\nTask deleted successfully!")
        else:
            print("\nTask not found.")

    except ValueError as error:
        print(f"\nError: {error}")


def main():
    create_tables()

    while True:
        show_menu()

        choice = input("\nChoose option: ").strip()

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            search_tasks()

        elif choice == "4":
            update_task()

        elif choice == "5":
            mark_completed()

        elif choice == "6":
            mark_pending()

        elif choice == "7":
            delete_task()

        elif choice == "8":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid option. Please try again.")


if __name__ == "__main__":
    main()        