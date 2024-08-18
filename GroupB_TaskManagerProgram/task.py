import datetime

class Task:
    def __init__(self, task_name, due_date):
        self.task_name = task_name
        self.description =  ""
        self.due_date = due_date
        self.priority_level = None
        #could also be 0 like set priority level numerically then assign keywords low, medium. and high to numerical value
        #OR para sa sort tasks by priority sa TaskManager class, we can first arrange each low, medium, and high priority by due date,
        #and then print low tasks, then medium, then high. Maybe we need a list for this idunno gl task class people
        self.completion_status = "" #Ongoing or Completed ganern
    def set_description ():
        pass
    def set_priority ():
        pass
    def set_completion_status ():
        pass
