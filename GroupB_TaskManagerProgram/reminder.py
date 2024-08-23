from datetime import date

class Reminder(Task):
    def __init__ (self, time_until_deadline, notifications):
      super().__init__(task_name, description, due_date, priority_level, completion_status)  
        self.time_until_deadline = time_until_deadline
        self.notifications = notifications
    def generate_reminder (self):
        #date format YYYY/MM/DD
        current_date = date.today()
        difference = self.time_until_deadline - current_date
        print(f"The task is due in {difference.days} days")
    def display_notif ():
        pass

#test instance lang para macheck nyo sa Visual Code pano gumagana
#sa instance mo rin ilalagay yung deadline ng task in year/month/day format
test = Reminder (date(2024, 8, 30), "N/a")
test.generate_reminder()
