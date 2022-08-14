#!/usr/bin/env python
# coding: utf-8

# In[9]:


import time

def task(n=100_000_000):
    while n:
        n -= 1

if __name__ == '__main__':
    start = time.perf_counter()
    task()
    task()
    finish = time.perf_counter()

    print(f'It took {finish-start: .2f} second(s) to finish')


# In[10]:


import time
import multiprocessing
from task_sample import task

if __name__  ==  '__main__':
    start = time.perf_counter()

    p1 = multiprocessing.Process(target=task)
    p2 = multiprocessing.Process(target=task)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    finish = time.perf_counter()

    print(f'It took {finish-start: .2f} second(s) to finish')


# In[ ]:





# In[ ]:




