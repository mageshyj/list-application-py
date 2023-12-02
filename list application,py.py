class Task:
    def __init__(self, name):
        self.name = name
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        new_task = Task(task_name)
        self.tasks.append(new_task)

    def remove_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                self.tasks.remove(task)

    def mark_task_completed(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True

    def print_tasks(self):
        for task in self.tasks:
            if task.completed:
                print("[X] " + task.name)
            else:
                print("[ ] " + task.name)


to_do_list = ToDoList()

to_do_list.add_task("Buy groceries")
to_do_list.add_task("Finish homework")
to_do_list.add_task("Go for a run")

to_do_list.print_tasks()

to_do_list.mark_task_completed("Buy groceries")

to_do_list.print_tasks()

to_do_list.remove_task("Finish homework")

to_do_list.print_tasks()
