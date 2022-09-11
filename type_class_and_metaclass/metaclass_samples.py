'''
A metaclass is a class that creates other classes. 
By default, Python uses the type metaclass to create other classes.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

The explicit Person class definition looks like this:

class Person(object, metaclass=type):
    def __init__(self, name, age):
        self.name = name
        self.age = age        

The metaclass argument allows you to specify which metaclass class to use to define the class. 
Therefore, you can create a custom metaclass that has its own logic to create other classes. 
By using a custom metaclass, you can inject functionality into the class creation process.

Python metaclass example

'''

from pprint import pprint

# First, define a custom metaclass called Human that has the freedom attribute sets to True by default:
class Human(type):
    def __new__(mcs, name, bases, class_dict):
        class_ = super().__new__(mcs, name, bases, class_dict)
        class_.freedom = True
        return class_

# Note that the __new__ method returns a new class or a class object.

# Second, define the Person class that uses the Human metaclass:
class Person(object, metaclass=Human):
    def __init__(self, name, age):
        self.name = name
        self.age = age

# The Person class will have the freedom attribute as shown in the class variables:
pprint(Person.__dict__)        

'''
Metaclass Parameters

To pass parameters to a metaclass, you use the keyword arguments. 
For example, the following redefine the Human metaclass that accepts keyword arguments, where each argument becomes a class variable:
'''

class Human(type):
    def __new__(mcs, name, bases, class_dict, **kwargs):
        class_ = super().__new__(mcs, name, bases, class_dict)
        class_.freedom = True
        if kwargs:
            for name, value in kwargs.items():
                setattr(class_, name, value)
        return class_

# The following uses the Human metaclass to create a Person class with the country and freedom class variables set to USA and True respectively:

class Person(object, metaclass=Human, country='BRASIL', freedom=True):
    def __init__(self, name, age):
        self.name = name
        self.age = age

# The Person class will have the attributes as shown in the class variables:
pprint(Person.__dict__)  


# =======================================
# Metaclass sample

"""
The following defines a Person class with two attributes name and age:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __hash__(self):
        return hash(f'{self.name, self.age}')

    def __str__(self):
        return f'Person(name={self.name},age={self.age})'

    def __repr__(self):
        return f'Person(name={self.name},age={self.age})'
Code language: Python (python)

Typically, when defining a new class, you need to:

    Define a list of object`s properties.
    Define an __init__ method to initialize object`s attributes.
    Implement the __str__ and __repr__ methods to represent the objects in human-readable and machine-readable formats.
    Implement the __eq__ method to compare objects by values of all properties.
    Implement the __hash__ method to use the objects of the class as keys of a dictionary or elements of a set.

As you can see, it requires a lot of code.

Imagine you want to define a Person class like this and automagically has all the functions above:

class Person:
    props = ['first_name', 'last_name', 'age']

To do that, you can use a metaclass.

"""


class Data(type):
    def __new__(mcs, name, bases, class_dict):
        class_obj = super().__new__(mcs, name, bases, class_dict)

        # create property
        Data.define_property(class_obj)

        # define __init__
        setattr(class_obj, '__init__', Data.init(class_obj))

        # define __repr__
        setattr(class_obj, '__repr__', Data.repr(class_obj))

        # define __eq__ & __hash__
        setattr(class_obj, '__eq__', Data.eq(class_obj))
        setattr(class_obj, '__hash__', Data.hash(class_obj))

        return class_obj

    @staticmethod
    def eq(class_obj):
        def _eq(self, other):
            if not isinstance(other, class_obj):
                return False

            self_values = [getattr(self, prop) for prop in class_obj.props]
            other_values = [getattr(other, prop) for prop in other.props]

            return self_values == other_values

        return _eq

    @staticmethod
    def hash(class_obj):
        def _hash(self):
            values = (getattr(self, prop) for prop in class_obj.props)
            return hash(tuple(values))

        return _hash

    @staticmethod
    def repr(class_obj):
        def _repr(self):
            prop_values = (getattr(self, prop) for prop in class_obj.props)
            prop_key_values = (f'{key}={value}' for key, value in zip(class_obj.props, prop_values))
            prop_key_values_str = ', '.join(prop_key_values)
            return f'{class_obj.__name__}({prop_key_values_str})'

        return _repr

    @staticmethod
    def init(class_obj):
        def _init(self, *obj_args, **obj_kwargs):
            if obj_kwargs:
                for prop in class_obj.props:
                    if prop in obj_kwargs.keys():
                        setattr(self, prop, obj_kwargs[prop])

            if obj_args:
                for kv in zip(class_obj.props, obj_args):
                    setattr(self, kv[0], kv[1])

        return _init

    @staticmethod
    def define_property(class_obj):
        for prop in class_obj.props:
            attr = f'_{prop}'
            prop_obj = property(
                fget=Prop(attr).get,
                fset=Prop(attr).set,
                fdel=Prop(attr).delete
            )
            setattr(class_obj, prop, prop_obj)

        return class_obj

class Prop:
    def __init__(self, attr):
        self._attr = attr

    def get(self, obj):
        return getattr(obj, self._attr)

    def set(self, obj, value):
        return setattr(obj, self._attr, value)

    def delete(self, obj):
        return delattr(obj, self._attr)


    
class Personal(metaclass=Data):
    props = ['name', 'age', 'city']    

print(Personal.__dict__)

personal = Personal(name='Bruno', age=39, city='São Paulo')
print(personal.__dict__)
print(personal.name)
print(personal.age)
print(personal)

p1 = Personal(name='Bruno', age=39, city='São Paulo')
p2 = Personal(name='Carlos', age=39, city='São Paulo')
 
print(p1 == p2)  # False

p2.name = 'Bruno'
print(p1 == p2)  # True


# =======================================================================================

class Employee(metaclass=Data):
    props = ['name', 'job_title']


if __name__ == '__main__':
    e = Employee(name='John Doe', job_title='Python Developer')
    print(e)


# usando decorator para reduzir o codigo na criação de uma classe
def data(cls):
    return Data(cls.__name__, cls.__bases__, dict(cls.__dict__))

# aqui está o decorator
@data
class Employee:
    props = ['name', 'job_title']

if __name__ == '__main__':
    e = Employee(name='Bruno', job_title='Software Enginner')
    print(e)