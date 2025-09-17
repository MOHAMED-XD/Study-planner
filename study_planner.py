# 📚 Study Planner
# Author: Mohammed Al Motasem Bellah Al Halabi
# A simple console app for students to manage study tasks.

import json
import os

TASKS_FILE = "tasks.json"

# Load existing tasks
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Display tasks
def show_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks yet. Add your first one!\n")
        return
    print("\n📝 Your Study Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['subject']} - {task['description']} (Deadline: {task['deadline']})")
    print()

# Add a task
def add_task(tasks):
    subject = input("📖 Enter subject: ")
    description = input("🖊️ Enter task description: ")
    deadline = input("📅 Enter deadline (e.g., 2025-09-20): ")
    tasks.append({"subject": subject, "description": description, "deadline": deadline})
    save_tasks(tasks)
    print("✅ Task added successfully!\n")

# Delete a task
def delete_task(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            choice = int(input("Enter the number of the task to delete: "))
            if 1 <= choice <= len(tasks):
                removed = tasks.pop(choice - 1)
                save_tasks(tasks)
                print(f"🗑️ Task '{removed['description']}' deleted.\n")
            else:
                print("⚠️ Invalid choice.\n")
        except ValueError:
            print("⚠️ Please enter a valid number.\n")

# Main loop
def main():
    print("✨ Welcome to Study Planner ✨")
    tasks = load_tasks()

    while True:
        print("Choose an option:")
        print("1️⃣ Show tasks")
        print("2️⃣ Add task")
        print("3️⃣ Delete task")
        print("4️⃣ Exit")

        choice = input("> ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("👋 Goodbye! Keep studying hard!")
            break
        else:
            print("⚠️ Invalid option. Try again.\n")

if __name__ == "__main__":
    main()
