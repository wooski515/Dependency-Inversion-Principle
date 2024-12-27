# Принцип інверсії залежностей (Dependency Inversion Principle)

from abc import ABC, abstractmethod

class NotificationService:
    def __init__(self, sender):
        self.sender = sender

    def send(self, message):
        self.sender.send_message(message)

class MessageSender(ABC):
    @abstractmethod
    def send_message(self, message):
        pass

class EmailSender(MessageSender):
    def send_message(self, message):
        print(f"Надсилання електронного листа з повідомленням: {message}")

class SMSSender(MessageSender):
    def send_message(self, message):
        print(f"Надсилання SMS з повідомленням: {message}")

if __name__ == "__main__":
    email_sender = EmailSender()
    sms_sender = SMSSender()

    email_notification = NotificationService(email_sender)
    sms_notification = NotificationService(sms_sender)

    email_notification.send("Привіт по електронній пошті!")
    sms_notification.send("Привіт через SMS!")
