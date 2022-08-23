#!/usr/bin/env python
# coding: utf-8

# # Set Comprehension

# In[2]:


tags = {'Django', 'Pandas', 'Numpy'}


# In[3]:


# Sem Set-Comprehension

lowercase_tags = set()
for tag in tags:
    lowercase_tags.add(tag.lower())

print(lowercase_tags)


# In[4]:


# Com Lambda e Sem Set-Comprehension

lowercase_tags = set(map(lambda tag: tag.lower(), tags))

print(lowercase_tags)


# In[5]:


# Com Set-Comprehension

lowercase_tags = {tag.lower() for tag in tags}

print(lowercase_tags)


# In[6]:


# Set-Comprehension com filtro

new_tags = {tag.lower() for tag in tags if tag != 'Numpy'}

print(new_tags)


# # Set Union

# In[10]:


s1 = {'Python', 'Java'}
s2 = {'C#', 'Java'}

s = s1.union(s2)

print(s)


# In[11]:


s1 = {'Python', 'Java'}
s2 = {'C#', 'Java'}

s = s1 | s2

print(s)


# In[9]:


# In fact, the union() method accepts one or more iterables, converts the iterables to sets, and performs the union.

rates = {1, 2, 3}
ranks = [2, 3, 4]

ratings = rates.union(ranks)

print(ratings)


# In[12]:


# However, the union operator (|) only allows sets, not iterables like the union() method.

rates = {1, 2, 3}
ranks = [2, 3, 4]

ratings = rates | ranks


# # Intersection

# In[14]:


s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}

s = s1.intersection(s2)

print(s)


# In[15]:


s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}

s = s1 & s2

print(s)


# In[16]:


# The following example uses the intersection() method to intersect a set with a list:
numbers = {1, 2, 3}
scores = [2, 3, 4]

numbers = numbers.intersection(scores)

print(numbers)


# In[17]:


# If you use the set intersection operator (&) instead, you’ll get an error:
numbers = {1, 2, 3}
scores = [2, 3, 4]

numbers = numbers & scores

print(numbers)


# # Set Difference

# In[18]:


s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}
s = s1.difference(s2)

print(s)


# In[19]:


s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}
s = s2.difference(s1)

print(s)


# In[20]:


s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}
s = s1 - s2

print(s)


# In[21]:


s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}
s = s2 - s1

print(s)


# In[22]:


# The following shows how to use the set difference() method with a list:
scores = {7, 8, 9}
numbers = [9, 10]
new_scores = scores.difference(numbers)

print(new_scores)


# In[23]:


# However, if you use the set difference operator (-) with iterables, you’ll get an error:
scores = {7, 8, 9}
numbers = [9, 10]
new_scores = scores - numbers

print(new_scores)


# # Set Symmetric Difference

# In[24]:


s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}

s = s1.symmetric_difference(s2)

print(s)


# In[25]:


s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}

s = s1 ^ s2

print(s)


# In[27]:


# The following example shows how to use the symmetric_difference() method to find the symmetric difference between a set and a list:
scores = {7, 8, 9}
ratings = [8, 9, 10]
new_set = scores.symmetric_difference(ratings)

print(new_set)


# In[28]:


# However, the symmetric difference operator (^) only applies to sets. If you use it with the iterables which aren’t sets, you’ll get an error. For example:
scores = {7, 8, 9}
ratings = [8, 9, 10]
new_set = scores ^ ratings

print(new_set)


# In[ ]:




