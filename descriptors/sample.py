class RequiredString:
    def __set_name__(self, owner, name):
        self.property_name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self

        return instance.__dict__[self.property_name] or None

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'The {self.property_name} must be a string')

        if len(value) == 0:
            raise ValueError(f'The {self.property_name} cannot be empty')

        instance.__dict__[self.property_name] = value

class Person:
    first_name = RequiredString()
    last_name = RequiredString()


person = Person()

try:
    person.first_name = ''
except ValueError as e:
    print(e)

try:
    person.last_name = None
except ValueError as e:
    print(e)

try:
    person.first_name = 200
except ValueError as e:
    print(e)    