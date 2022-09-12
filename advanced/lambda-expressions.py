#!/usr/bin/env python
# coding: utf-8

# In[1]:


def get_full_name(first_name, last_name, formatter):
    return formatter(first_name, last_name)

def first_last(first_name, last_name):
    return f"{first_name} {last_name}"

def last_first(first_name, last_name):
    return f"{last_name}, {first_name}"

full_name = get_full_name('John', 'Doe', first_last)
print(full_name) # John Doe

full_name = get_full_name('John', 'Doe', last_first)
print(full_name) #  Doe, John


# In[3]:


def get_full_name(first_name, last_name, formatter):
    return formatter(first_name, last_name)


full_name = get_full_name(
    'John',
    'Doe',
    lambda first_name, last_name: f"{first_name} {last_name}"
)
print(full_name)

full_name = get_full_name(
    'John',
    'Doe',
    lambda first_name, last_name: f"{last_name}, {first_name}"
)
print(full_name)


# In[4]:


def times(n):
    return lambda x: x * n

double = times(2)

result = double(5)
print(result)

result = double(13)
print(result)


# In[6]:


triple = times(3)

print(triple(21))  # 63
print(triple(37))  # 111


# In[7]:


# lambda in a loop

callables = []
for i in (1, 2, 3):
    callables.append(lambda a=i: a)

for f in callables:
    print(f())


# In[ ]:




