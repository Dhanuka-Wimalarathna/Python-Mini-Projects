import json
import os
from datetime import datetime

TASK_FILE = "TODOS.json"

def load_data ():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as file:
        return json.load(file)

def save_data (data):
    with open(TASK_FILE, "w") as file:
        return json.dump(data, file, indent=4)

print("\n<-- Welcome TODO CLI -->\n")


def add_task():
    tasks = load_data()

    description = input ("Enter the task: ")

    new_task =  {
        "id": len(tasks) + 1,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updatedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    tasks.append(new_task)
    save_data(tasks)
    print(f'Task "{description}" saved! (ID: {new_task["id"]})')


def update_task():
    tasks = load_data()

    if len(tasks) == 0:
        print("No tasks to update.")
        return

    view_all()

    task_id = int(input("\nEnter the task ID need to update: "))

    for task in tasks:
        if task["id"] == task_id:
            print ("\n 01.Todo")
            print (" 02.In progress")
            print (" 03.Done")

            new_status = input("Enter new status: ")

            if new_status == "1":
                task["status"] = "Todo"
            elif new_status == "2":
                task["status"] = "In progress"
            elif new_status == "3":
                task["status"] = "Done"
            else:
                print("Invalid Status Choice.")
                return

            task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_data(tasks)
            print(f"Task {task_id} updated successfully.")
            return

    print(f"Task {task_id} not found.")



def delete_tasks():
    tasks = load_data()

    if len(tasks) == 0:
        print("No tasks to delete.")
        return
    
    confirm = input("Are you sure you want to delete all tasks? (Y/N): ")

    if confirm == "Y" or confirm == "y":
        save_data([])
        print("All Tasks are deleted.")
    else: 
        print("Deleting cancelled.")



def view_all():
    tasks = load_data()

    if len(tasks) == 0:
        print("No tasks to show.")
        return

    id_w    = 5
    desc_w  = 25
    stat_w  = 15
    date_w  = 22

    line = f"+{'-'*id_w}+{'-'*desc_w}+{'-'*stat_w}+{'-'*date_w}+{'-'*date_w}+"


    print("\n" + line)
    print(f"| {'ID':<{id_w-1}}| {'Description':<{desc_w-1}}| {'Status':<{stat_w-1}}| {'Created At':<{date_w-1}}| {'Updated At':<{date_w-1}}|")
    print(line)

    for task in tasks:
        print(f"| {task['id']:<{id_w-1}}| {task['description']:<{desc_w-1}}| {task['status']:<{stat_w-1}}| {task['createdAt']:<{date_w-1}}| {task['updatedAt']:<{date_w-1}}|")
        print(line)

    print()

def show_task():
    while True:
        print (" 01. Add New Task: ")
        print (" 02. Update Status of Selected Task: ")
        print (" 03. Delete All Tasks: ")
        print (" 04. View All Tasks: ")
        print (" 05. Exit: ")

        choice = input("\nSelect one option: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            update_task()
        elif choice == "3":
            delete_tasks()
        elif choice == "4":
            view_all()
        elif choice == "5":
            print ("\nGoodBye!!")
            break
        else:
            print("\nInvalid choice.")

show_task()

