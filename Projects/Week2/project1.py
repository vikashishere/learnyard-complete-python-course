# Project 1: To-Do List CLI App

# Concepts Used:
# lists, for loops
# if-elif-else, while
# Functions for modular design

# To-Do List CLI App

tasks = []

def show_menu():
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("Your Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def delete_task():
    view_tasks()
    if tasks:
        try:
            choice = int(input("Enter task number to delete: "))
            if 1 <= choice <= len(tasks):
                removed = tasks.pop(choice - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number.")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")
