from utilities import load_tasks, save_tasks
from storage import calculate_days_left, is_valid_date

def add_task():
    title = input("Enter task title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return

    while True:
        deadline = input("Enter deadline (DD-MM-YYYY): ").strip()
        if is_valid_date(deadline):
            break
        print("Invalid date format. Please try again.")

    tasks = load_tasks()

    task_id = tasks[-1]["id"] + 1 if tasks else 1

    task = {
        "id": task_id,
        "title": title,
        "deadline": deadline
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")


def view_tasks():
    tasks = load_tasks()

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        days_left = calculate_days_left(task["deadline"])

        if days_left > 0:
            print(f"{task['id']}. {task['title']} — {days_left} days left")
        else:
            print(f"{task['id']}. {task['title']} — Overdue by {abs(days_left)} days")
        
def delete_task():
    tasks = load_tasks()

    if not tasks:
        print("No tasks to delete.")
        return

    for task in tasks:
        print(f"{task['id']}. {task['title']}")

    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            confirm = input(f"Delete '{task['title']}' permanently? (y/n): ").lower()

            if confirm == "y":
                del tasks[i]  
                save_tasks(tasks)
                print("Task deleted permanently.")
            else:
                print("Deletion cancelled.")
            return

    print("Task ID not found.")