'''
The Liskov substitution principle states that a child class must be substitutable for its parent class. 
Liskov substitution principle aims to ensure that the child class can assume the place of its parent class without causing any errors.

from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def notify(self, message, email):
        pass


class Email(Notification):
    def notify(self, message, email):
        print(f'Send {message} to {email}')


class SMS(Notification):
    def notify(self, message, phone):
        print(f'Send {message} to {phone}')


if __name__ == '__main__':
    notification = SMS()
    notification.notify('Hello', 'john@test.com')

The Notification abstract class has the notify() method that sends a message to an email.

The notify() method of the Email class sends a message to an email, which is fine.

However, the SMS class uses a phone number, not an email, for sending a message. 
Therefore, we need to change the signature of the notify() method of the SMS class to accept a phone number instead of an email.


class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


class NotificationManager:
    def __init__(self, notification, contact):
        self.contact = contact
        self.notification = notification

    def send(self, message):
        if isinstance(self.notification, Email):
            self.notification.notify(message, contact.email)
        elif isinstance(self.notification, SMS):
            self.notification.notify(message, contact.phone)
        else:
            raise Exception('The notification is not supported')


if __name__ == '__main__':
    contact = Contact('John Doe', 'john@test.com', '(408)-888-9999')
    notification_manager = NotificationManager(SMS(), contact)
    notification_manager.send('Hello John')

The send() method of the NoticationManager class accepts a notification object. 
It checks whether the notification is an instance of the Email or SMS and passes the email and phone of contact to the notify() method respectively.

'''

from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def notify(self, message: str) -> None:
        pass


class Email(Notification):
    def __init__(self, email: str):
        self.email = email

    def notify(self, message: str) -> None:
        print(f'Send "{message}" to {self.email}')


class SMS(Notification):
    def __init__(self, phone: str):
        self.phone = phone

    def notify(self, message: str) -> None:
        print(f'Send "{message}" to {self.phone}')


class Contact:
    def __init__(self, name: str, email: str, phone: str):
        self.name = name
        self.email = email
        self.phone = phone


class NotificationManager:
    def __init__(self, notification: Notification):
        self.notification = notification

    def send(self, message: str) -> None:
        self.notification.notify(message)


if __name__ == '__main__':
    contact = Contact(name='John Doe', email='john@test.com', phone='(408)-888-9999')

    sms_notification = SMS(contact.phone)
    email_notification = Email(contact.email)

    notification_manager = NotificationManager(sms_notification)
    notification_manager.send('Hello John')

    notification_manager.notification = email_notification
    notification_manager.send('Hi John')
