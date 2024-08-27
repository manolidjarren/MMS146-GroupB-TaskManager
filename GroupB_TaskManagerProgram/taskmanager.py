from task import Task
from datetime import date

class TaskManager(Task):
    task_list = []
    def __init__(self, task_name, description, due_date):
        super().__init__(task_name, description, due_date)

    def add_task (self, task_name): #i rlly like this one but i might change this according sa edit task method
       if self.task_name == task_name:
           task_info = {
                "Task Name": self.task_name,
                "Description": self.description,
                "Due Date": self.due_date,
                "Priority Level": self.priority_level,
                "Completion Status": self.completion_status
            }
           TaskManager.task_list.append(task_info)
           print(f"Task '{task_name}' added!")

    def edit_task (self, task_name, new_task_name, new_desc): #Im working on this :3
        if task_name in TaskManager.task_list:
            self.task_name = new_task_name
            self.description = new_desc

    def delete_task (self, task_name): #Very not finished at all eyuck HELLP
        if task_name in TaskManager.task_list:
            TaskManager.task_list.remove(task_name)

    @classmethod
    def view_all_tasks(cls): #very slay
        print(cls.task_list)

    def sort_tasks_by_priority (): 
        pass
    def get_overdue_tasks ():
        pass

task1 = TaskManager(
    task_name = "Task Manager Group Project",
    due_date=date(2024,9,1),
    description ="Reminder: Submit the group project!"
)
task1.add_task("Task Manager Group Project")
TaskManager.view_all_tasks()
