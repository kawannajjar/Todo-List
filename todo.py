import json

# List to store tasks
tasks = []


def load_tasks():
    """Load tasks from a JSON file. """
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_tasks():
    """Save tasks to a JSON file."""
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
        

def show_tasks():
    """Display all tasks in the list."""
    if len(tasks) == 0:
        print("No task available")
    else:
        print("Your tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
            

def add_task(task):
    """Add a new task to the list."""
    tasks.append(task)
    print(f"Task '{task} added to the list.")
    save_tasks()
    

def remove_tasks(task_index):
    """Remove a task from the list based on its index."""
    if task_index < 1 or task_index > len(tasks):
        print("Invalid task number.")
    else:
        removed_task = tasks.pop(task_index - 1)
        print(f"Task '{removed_task}' removed from the list.")
        save_tasks()

# Loading tasks at the start of the program


tasks = load_tasks()

# Main program loop
while True:
    print("\nOptions:")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == "3":
        task_index = int(input("Enter the task number to remove: "))
        remove_tasks(task_index)
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice, please try again.")