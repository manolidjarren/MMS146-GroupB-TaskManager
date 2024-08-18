class Reminder(Task):
    def __init__ (self, time_until_deadline, notifications):
        self.time_until_deadline = time_until_deadline
        self.notifications = notifications
    super().__init__(task_name, description, due_date, priority_level, completion_status)
    def generate_reminder ():
        pass
    def display_notif ():
        pass