"""
Project 1: To-Do List
A simple Python program demonstrating the IPO model (Input -> Process -> Output)
using a list to store tasks in temporary memory.
"""

tasks = []  # Temporary in-memory storage for tasks


def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("\nTask added successfully!\n")


def view_tasks():
    print("\nYour Tasks:")
    if not tasks:
        print("No tasks added yet.\n")
        return
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
    print()


def main():
    while True:
        print("===== TO-DO LIST =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.\n")


if __name__ == "__main__":
    main()