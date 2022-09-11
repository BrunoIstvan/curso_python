'''
If a class uses a non-data descriptor, Python will search the attribute in instance attributes first (instance.__dict__). 
If Python doesn`t find the attribute in the instance attributes, it`ll use the data descriptor.
'''

import os


class FileCount:
    def __get__(self, instance, owner):
        print('The __get__ was called')
        return len(os.listdir(instance.path))

class Folder:
    count = FileCount()

    def __init__(self, path):
        self.path = path

folder = Folder('/')
print('file count: ', folder.count)



