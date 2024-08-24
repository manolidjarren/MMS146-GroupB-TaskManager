class TaskManager(Task):
    def __init__ (task_name, description, due_date, priority_level, completion_status):
        super ().__init__(task_name, description, due_date, priority_level, completion_status)
        self.__tasklist = tasklist
    def add_task ():
        self.__tasklist.append(Task)
    def edit_task ():
        pass
    def delete_task ():
        self.__tasklist.remove(Task)
    def view_tasks ():
        pass
    def sort_tasks_by_priority ():
        pass
    def get_overdue_tasks ():
        pass
