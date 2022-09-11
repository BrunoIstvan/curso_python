'''
Python calls the __new__ method and the __init__ method after that.
'''

class Person:
    def __new__(cls, name):
        print(f'Creating a new {cls.__name__} object...')
        obj = object.__new__(cls)
        return obj

    def __init__(self, name):
        print(f'Initializing the person object...')
        self.name = name


person = Person('John')


'''
In this example, the __new__() method of the SquareNumber class accepts an integer and returns the square number. 
x is an instance of the SquareNumber class and also an instance of the int built-in type
In practice, you use the __new__() method when you want to tweak the object at the instantiated time.
'''

class SquareNumber(int):
    def __new__(cls, value):
        return super().__new__(cls, value ** 2)


x = SquareNumber(3)
print(x)  # FUNCIONA

'''
Note that you cannot do this by using the __init__() method because the __init__() method of the built-in int takes no argument. 
The following code will result in an error:
'''
class SquareNumber(int):
    def __init__(self, value):
        super().__init__(value ** 2)

try:
    x = SquareNumber(3)
except TypeError as e:
    print(isinstance(e, Exception))
    print(e)


'''
Typically, when you override the __new__() method, you don`t need to define the __init__() 
method because everything you can do in the __init__() method, you can do it in the __new__() method.
'''
class Person:
    def __new__(cls, first_name, last_name):
        # create a new object
        obj = super().__new__(cls)

        # initialize attributes
        obj.first_name = first_name
        obj.last_name = last_name

        # inject new attribute
        obj.full_name = f'{first_name} {last_name}'
        return obj


person = Person('John', 'Doe')
print(person.full_name)

print(person.__dict__)
