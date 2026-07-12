from database.db import create_tables


def main():
    create_tables()

    print("=" * 40)
    print("      TASK MANAGER PRO")
    print("=" * 40)
    print("Database initialized successfully!")
    print("Project setup completed.")
    print("\nReady to build the Task Manager.")


if __name__ == "__main__":
    main()