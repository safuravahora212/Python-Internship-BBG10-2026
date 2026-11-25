class Notification:
    def send(self):
        print("Sending generic notification")

class EmailNotification(Notification):
    def send(self):
        print("Sending Email notification")

class SMSNotification(Notification):
    def send(self):
        print("Sending SMS notification")

# Test
notifications = [Notification(), EmailNotification(), SMSNotification()]

for n in notifications:
    n.send()