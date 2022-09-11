'''
Modo comum de criar uma classe

class Person:
    def __init__(self, name, age, iq=100):
        self.name = name
        self.age = age
        self.iq = iq

Agora usando o decorator dataclass 

'''

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    iq: int = 100

p1 = Person('John', 25)
p2 = Person('John', 25)
print(p1 == p2)

'''
Note that the order of the attributes declared in the class will determine the orders of the parameters in the __init__ method.

Convert to a tuple or a dictionary
'''

from dataclasses import astuple, asdict

p = Person('John Doe', 25)

print(astuple(p))
print(asdict(p))

'''
Create immutable objects

To create readonly objects from a dataclass, you can set the frozen argument of the dataclass decorator to True. For example:
'''

from dataclasses import FrozenInstanceError

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    iq: int = 100

try:
    q = Person('Jane Doe', 25)
    q.iq = 120
except FrozenInstanceError as e: 
    print(e)

'''
Customize attribute behaviors

If you want to initialize an attribute that depends on the value of another attribute, you can use the __post_init__ method. 
As its name implies, Python calls the __post_init__ method after the __init__ method.
'''

from dataclasses import dataclass, field

@dataclass
class Personallity:
    name: str
    age: int
    iq: int = 100
    can_vote: bool = field(init=False)

    def __post_init__(self):
        print('called __post_init__ method')
        self.can_vote = 18 <= self.age <= 70

p = Personallity(name='Jane Doe', age=25)
print(p)

p = Personallity(name='Peter Doe', age=15)
print(p)

'''
Sort objects
'''

from dataclasses import dataclass, field


@dataclass(order=True)
class Person:
    sort_index: int = field(init=False, repr=False)

    name: str
    age: int
    iq: int = 100
    can_vote: bool = field(init=False)

    def __post_init__(self):
        self.can_vote = 18 <= self.age <= 70
        # sort by age
        self.sort_index = self.age

members = [
    Person(name='Bob', age=35),
    Person(name='John', age=25),
    Person(name='Alice', age=30)
]

sorted_members = sorted(members)
for member in sorted_members:
    print(f'{member.name}(age={member.age})')