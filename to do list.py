class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def view_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            status = "✓" if task["completed"] else " "
            print(f"{index}. [{status}] {task['task']}")

    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

# Example usage:
todo_list = ToDoList()

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Mark Task as Completed\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        todo_list.add_task(task)
    elif choice == "2":
        todo_list.view_tasks()
    elif choice == "3":
        task_index = int(input("Enter the task index to mark as completed: "))
        todo_list.mark_completed(task_index)
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose again.")
