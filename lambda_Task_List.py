class Task:
    def __init__(self, description, priority, status="pending"):
        self.description = description
        self.priority = priority
        self.status = status

    def __repr__(self):
        return f"Task(description='{self.description}', priority={self.priority}, status='{self.status}')"

class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority, status="pending"):
        task = Task(description, priority, status)
        self.tasks.append(task)

    def sort_tasks_by_priority(self):
        self.tasks.sort(key=lambda task: task.priority)

    def filter_tasks_by_status(self, status):
        return list(filter(lambda task: task.status == status, self.tasks))

    def display_tasks(self, tasks=None):
        if tasks is None:
            tasks = self.tasks
        for task in tasks:
            print(task)
    
# Method to add tasks dynamically
def add_task_interactively(task_list):
    while True:
        description = input("Enter the task description or type 'done' to finish the task: ")
        if description.lower() == 'done':
            break
        try:
            priority = int(input("Enter the task priority (eg. 1 - High, 2 - Medium, 3 - Low): "))
        except ValueError:
            print("Priority must be a number. Try again.")
            continue
        status = input("Enter the task status (pending/completed): ").lower()
        if status not in ["pending", "completed"]:
            print("Invalid status. Defaulting to 'pending'.")
            status = "pending"

        task_list.add_task(description, priority, status)

if __name__ == "__main__":
    task_list = TaskList()

    # Adding tasks interactively
    add_task_interactively(task_list)

    print("\nAll Tasks:")
    task_list.display_tasks()

    # Sorting tasks by priority
    task_list.sort_tasks_by_priority()
    print("\nTasks Sorted by Priority:")
    task_list.display_tasks()

    # Filter tasks by status
    pending_tasks = task_list.filter_tasks_by_status("pending")
    completed_tasks = task_list.filter_tasks_by_status("completed")

    print("\nPending Tasks:")
    task_list.display_tasks(pending_tasks)

    print("\nCompleted Tasks:")

