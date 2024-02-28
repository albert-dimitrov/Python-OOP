from OOP.ClassesandObjectsExercise.TodoList.project_.task import Task

class Section:

    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)

        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        try:
            task = next(filter(lambda t: t.name == task_name, self.tasks))
            task.completed = True

            return f"Completed task {task_name}"
        except StopIteration:
            return f"Could not find task with the name {task_name}"

    def clean_section(self):
        count_of_tasks = 0

        for t in self.tasks:
            if t.completed:
                count_of_tasks += 1
                self.tasks.remove(t)

        return f"Cleared {count_of_tasks} tasks."

    def view_section(self):
        task_with_details = '\n'.join(t.details() for t in self.tasks)

        return f"Section {self.name}:\n" \
               f"{task_with_details}"

