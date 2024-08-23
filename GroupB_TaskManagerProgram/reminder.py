from datetime import date

class Reminder(Task):
    def __init__(self, task_name, due_date, notifications):
        super().__init__(task_name, due_date)
        self.time_until_deadline = self.calculate_time_until_deadline()
        self.notifications = notifications

    def calculate_time_until_deadline(self):
        current_date = date.today()
        return self.due_date - current_date 

    def generate_reminder (self):
        difference = self.time_until_deadline
        if difference.days >= 0:
            print(f"The task is due in {difference.days} days")
        else: 
            print(f"The task {self.task_name} was due {-difference.days} days ago.")

    def display_notif(self):
        print(self.notifications)

reminder = Reminder(
    task_name = "Task Manager Group Project",
    due_date=date(2024,9,1),
    notifications="Reminder: Submit the group project!"
)

reminder2 = Reminder(
    task_name = "KAS 1: Draft your Essay Answers",
    due_date=date(2024,8,22),
    notifications="Complete it as soon as possible!"
)

reminder.generate_reminder()
reminder.display_notif()
reminder2.generate_reminder()
reminder2.display_notif()
