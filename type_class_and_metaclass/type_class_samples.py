class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        return f'Hi, I am {self.name}. I am {self.age} year old.'

print(type(Person))

print(isinstance(Person, type))

'''
Python uses the type class to create other classes.
The type class itself is a callable. 

The constructor has three parameters for creating a new class:

    name: is the name of the class e.g., Person
    bases is a tuple that contains the base classes of the new class. For example, the Person inherits from the object class, so the bases contains one class (object,)
    dict is the class namespace

Technically, you can use the type class to create a class dynamically. Before doing it, you need to understand how Python creates the classes.

When the Python interpreter encounters a class definition in the code, it will:

    First, extract the class body as string.
    Second, create a class dictionary for the class namespace.
    Third, execute the class body to fill up the class dictionary.
    Finally, create a new instance of type using the above type() constructor.

Let`s emulate the steps above to create a Person class dynamically:

'''

# First, extract the class body:
class_body = """
def __init__(self, name: str, age: int):
    self.name = name
    self.age = age

def greeting(self):
    return f'Hi, I am {self.name}. I am {self.age} year old.'
"""

# Second, create a class dictionary:
class_dict = {}

# Third, execute the class body and fill up the class dictionary:
exec(class_body, globals(), class_dict)

# The exec() function executes the class body and fills up the global and class namespaces.
# Finally, create a new Person class using the type constructor:
Personal = type('Personal', (object,), class_dict)

print(Personal.__dict__)

print(isinstance(Personal, type))


personal = Personal(name='Bruno', age=39)
print(personal.__dict__)

'''
In this example, Python creates the type class dynamically, which is the same as the one that you define statically in the code.

Because the type class creates other classes, we often refer to it as a metaclass. 
A metaclass is a class used to create other classes.
'''
