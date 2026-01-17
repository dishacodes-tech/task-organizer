from task_manager import add_task, view_tasks, delete_task

def main():
    while True:
        print("\n--- Task Scheduler ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Thank you!Have a nice day")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()