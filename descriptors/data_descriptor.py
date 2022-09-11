'''
When a class has a data descriptor, Python will look for an instance`s attribute in the data descriptor first. 
If Python doesn`t find the attribute, it`ll look for the attribute in the instance dictionary (__dict__)
'''

class Coordinate:
    def __get__(self, instance, owner):
        print('The __get__ was called')

    def __set__(self, instance, value):
        print('The __set__ was called')

class Point:
    x = Coordinate()
    y = Coordinate()

p = Point()
p.x = 10
p.x




