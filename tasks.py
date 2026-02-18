import json
import os


TASKS_FILE = "tasks.json"


# Adding a new task
def add_task(tasks):
    description = input("Enter task description: ").strip()
    if description:
        tasks.append({"description": description, "done": False})
        print("Task added.")
    else:
        print("Task cannot be empty.")


# Viewing all tasks
def list_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    print("\nCurrent tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "[x]" if task["done"] else "[ ]"
        print(f"{i}. {status} {task['description']}")
    print()


# Marking a task as done
def mark_task_as_done(tasks):
    list_tasks(tasks)
    if not tasks:
        return
    try:
        choice = int(input("Enter task number to mark as done: "))
        if 1 <= choice <= len(tasks):
            if tasks[choice - 1]["done"]:
                print("Task already done.")
            else:
                tasks[choice - 1]["done"] = True
                print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


# Saving tasks to tasks.json
def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4)


# Loading tasks from tasks.json
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            tasks = json.load(f)
        for task in tasks:
            if "description" not in task or "done" not in task:
                raise ValueError("Corrupted task entry")
        return tasks
    except (json.JSONDecodeError, ValueError, FileNotFoundError):
        return []


# Main function
def main():
    tasks = load_tasks()
    while True:
        print("\n--- Task Manager ---")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Mark a task as done")
        print("4. Save tasks (manual save)")
        print("5. Load tasks (reload from file)")
        print("6. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            mark_task_as_done(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Tasks saved.")
        elif choice == "5":
            tasks = load_tasks()
            print("Tasks reloaded from file.")
        elif choice == "6":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
