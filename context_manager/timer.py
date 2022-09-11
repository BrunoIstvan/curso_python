'''

Python with statement

Here is the typical syntax of the with statement:

with context as ctx:
    # use the the object 

# context is cleaned up
Code language: Python (python)

How it works.

    When Python encounters the with statement, it creates a new context. The context can optionally return an object.
    After the with block, Python cleans up the context automatically.
    The scope of the ctx has the same scope as the with statement. It means that you can access the ctx both inside and after the with statement.

Python context manager protocol

Python context managers work based on the context manager protocol.

The context manager protocol has the following methods:

    __enter__() - setup the context and optionally return some object
    __exit__() - cleanup the object.

The __enter__() method

In the __enter__() method, you can carry the necessary steps to setup the context.

Optionally, you can returns an object from the __enter__() method.
The __exit__() method

Python always executes the __exit__() method even if an exception occurs in the with block.

The __exit__() method accepts three arguments: exception type, exception value, and traceback object. 
All of these arguments will be None if no exception occurs.

Python context manager applications

As you see from the previous example, the common usage of a context manager is to open and close files automatically.

However, you can use context managers in many other cases:
1) Open - Close

If you want to open and close a resource automatically, you can use a context manager.

For example, you can open a socket and close it using a context manager.
2) Lock - release

Context managers can help you manage locks for objects more effectively. They allow you to acquire a lock and release it automatically.
3) Start - stop

Context managers also help you to work with a scenario that requires the start and stop phases.

For example, you can use a context manager to start a timer and stop it automatically.
3) Change - reset

Context managers can work with change and reset scenario.

For example, your application needs to connect to multiple data sources. And it has a default connection.

To connect to another data source:

    First, use a context manager to change the default connection to a new one.
    Second, work with the new connection
    Third, reset it back to the default connection once you complete working with the new connection.

'''

from time import perf_counter


class Timer:
    def __init__(self):
        self.elapsed = 0

    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.stop = perf_counter()
        self.elapsed = self.stop - self.start
        return False


def fibonacci(n):
    f1 = 1
    f2 = 1
    for i in range(n-1):
        f1, f2 = f2, f1 + f2

    return f1


with Timer() as timer:
    for _ in range(1, 1000):
        fibonacci(100)

print(timer.elapsed)