import datetime

class Task:

    #priority levels
    PRIORITY_LOW = 0
    PRIORITY_MEDIUM = 1
    PRIORITY_HIGH = 2

    # Completion statuses
    STATUS_NOT_STARTED = "Not Started"
    STATUS_IN_PROGRESS = "In progress"
    STATUS_COMPLETED = "Completed"

    def __init__(self, task_name, description, due_date, priority_level=PRIORITY_LOW, completion_status=STATUS_NOT_STARTED):
        self.task_name = task_name
        self.description =  description
        self.due_date = due_date
        self.priority_level = priority_level
        #could also be 0 like set priority level numerically then assign keywords low, medium. and high to numerical value
        #OR para sa sort tasks by priority sa TaskManager class, we can first arrange each low, medium, and high priority by due date,
        #and then print low tasks, then medium, then high. Maybe we need a list for this idunno gl task class people
        self.completion_status = completion_status #Ongoing or Completed ganern
    
    #update the description of the task
    def set_description (self, description): 
        self.description = description
    #update the priority of the task (numeric value)
    def set_priority (self, priority_level):
        self.priority_level = priority_level
    #update the completion status of the task 
    def set_completion_status (self, completion_status):
        self.completion_status = completion_status
