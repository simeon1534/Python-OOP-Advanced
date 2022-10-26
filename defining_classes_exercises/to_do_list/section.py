from to_do_list.task import Task


class Section:
    name: str
    tasks: list

    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        else:
            return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        for task_object in self.tasks:
            if task_object.name == task_name:
                task_object.completed = True
                return f"Completed task {task_object.name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        cleaned = 0
        for task_obj in self.tasks:
            if task_obj.completed:
                self.tasks.remove(task_obj)
                cleaned += 1  # potencialen error
        return f"Cleared {cleaned} tasks."

    def view_section(self):
        res = f"Section {self.name}\n"
        details_tasks = "\n".join([task_obj.details() for task_obj in self.tasks])

        return res + details_tasks


task = Task("Drink Tea", "27/05/2020")
task2 = Task("Make bed", "27/05/2020")


section = Section("Daily tasks")
print(section.add_task(task))
print(section.add_task(task2))


print(section.complete_task("Drink Tea"))
print(section.view_section())

print(section.clean_section())
print(section.view_section())
