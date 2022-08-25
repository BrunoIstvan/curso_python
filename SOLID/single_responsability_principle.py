'''

The single responsibility principle (SRP) states that every class, method, and function should have only one job or one reason to change.

The purposes of the single responsibility principle are to:

    Create high cohesive and robust classes, methods, and functions.
    Promote class composition
    Avoid code duplication


class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person(name={self.name})'

    @classmethod
    def save(cls, person):
        print(f'Save the {person} to the database')


if __name__ == '__main__':
    p = Person('John Doe')
    Person.save(p)

Later, if you want to save the Person into different storage such as a file, you’ll need to change the save() method, which also changes the whole Person class.

To make the Person class conforms to the single responsibility principle, you’ll need to create another class that is in charge of storing the Person to a database. For example:

'''
class PersonDB:
    def save(self, person):
        print(f'Save the {person} to the database')


class Person:
    def __init__(self, name):
        self.name = name
        self.db = PersonDB()

    def __repr__(self):
        return f'Person(name={self.name})'

    def save(self):
        self.db.save(person=self)


if __name__ == '__main__':
    p = Person('John Doe')
    p.save()