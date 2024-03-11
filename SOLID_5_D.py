# [Dependency Inversion Principle (DIP)] Download the python file from this link. Suppose we have a NotificationService class 
# that is responsible for sending notifications. The NotificationService class directly depends on the EmailSender class to send 
# emails.

# In this implementation, the NotificationService class directly depends on the EmailSender class, which violates the Dependency 
# Inversion Principle. The high-level NotificationService should not depend on the low-level EmailSender, as it tightly couples 
# the classes together.

# Redesign this program to follow the  Dependency Inversion Principle (DIP) principle which represents that “Abstractions should 
# not depend upon details. Details should depend upon abstractions.”

from abc import ABC, abstractmethod

class NotificationSender(ABC):
    def send_notification(self, recipient, subject, message):
        pass

class EmailSender(NotificationSender):
    def send_email(self, recipient, subject, message):
        # Code to send an email
        print(f"Sending email to {recipient}: {subject} - {message}")

class NotificationService:
    def __init__(self, email_sender):
        self.email_sender = email_sender

    def send_notification(self, recipient, message):
        self.email_sender.send_email(recipient, "Notification", message)

# Using the NotificationService to send a notification
email_sender = EmailSender()
notification_service = NotificationService(email_sender)
notification_service.send_notification("user@example.com", "Hello, this is a notification!")