# Initial empty list to store tasks
todo_list = []

def show_menu():
    print("\n----- To-Do List Menu -----")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

def view_tasks():
    if not todo_list:
        print("\nTo-do list is empty.")
    else:
        print("\nTo-Do List:")
        for idx, task in enumerate(todo_list, 1):
            status = "Done" if task['completed'] else "Not Done"
            print(f"{idx}. {task['task']} - {status}")

def add_task():
    task = input("\nEnter the task you want to add: ")
    todo_list.append({"task": task, "completed": False})
    print("Task added successfully!")

def update_task():
    view_tasks()
    if todo_list:
        try:
            task_num = int(input("\nEnter the task number you want to update: "))
            if 1 <= task_num <= len(todo_list):
                new_task = input("Enter the new task description: ")
                todo_list[task_num - 1]['task'] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number.")

def mark_completed():
    view_tasks()
    if todo_list:
        try:
            task_num = int(input("\nEnter the task number to mark as completed: "))
            if 1 <= task_num <= len(todo_list):
                todo_list[task_num - 1]['completed'] = True
                print("Task marked as completed!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number.")

# Main program loop
while True:
    show_menu()
    choice = input("\nChoose an option (1-5): ")
    
    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        update_task()
    elif choice == '4':
        mark_completed()
    elif choice == '5':
        print("Exiting To-Do List program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select from the menu options.")