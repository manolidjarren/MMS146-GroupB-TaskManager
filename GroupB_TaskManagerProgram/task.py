import datetime

class Task:

    #priority levels
    PRIORITY_LOW = 0
    PRIORITY_MEDIUM = 1
    PRIORITY_HIGH = 2

    # Completion statuses
    STATUS_NOT_STARTED = "Not Started"
    STATUS_IN_PROGRESS = "In Progress"
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
    def set_description (self, new_description):
        if type(new_description) == str: #checks if the value is a valid type for this attribute
            self.description = new_description
    #update the priority of the task (numeric value)
    def set_priority (self, new_priority_level):
        if type(new_priority_level) == int:
            if new_priority_level <= 2 & new_priority_level >= 0: #only changes value if within a certain range
                self.priority_level = new_priority_level
    #update the completion status of the task 
    def set_completion_status (self, new_completion_status):
        if type(new_completion_status) == str:
            status = ["Not Started", "In Progress", "Completed"]
            if any(s == new_completion_status for s in status): #only changes value if its any of the valid statuses
                self.completion_status = new_completion_status
