#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install Pillow')


# In[7]:


# WITHOUT MULTIPROCESSING
import time
import os
from PIL import Image, ImageFilter

filenames = [
    'images/1.jpg',
    'images/2.jpg',
    'images/3.jpg',
    'images/4.jpg',
    'images/5.jpg',
]

def create_thumbnail(filename, size=(100,100), thumb_dir ='thumbs'):
    img = Image.open(filename)
    img = img.filter(ImageFilter.GaussianBlur())
    img.thumbnail(size)
    img.save(f'{thumb_dir}/{os.path.basename(filename)}')
    print(f'{filename} was processed...')


if __name__ == '__main__':
    start = time.perf_counter()

    for filename in filenames:
        create_thumbnail(filename)
        
    finish = time.perf_counter()

    print(f'It took {finish-start: .2f} second(s) to finish')


# In[8]:


# WITH MULTIPROCESSING
import time
import os
import multiprocessing
from PIL import Image, ImageFilter
from task_sample import create_thumbnail

filenames = [
    'images/1.jpg',
    'images/2.jpg',
    'images/3.jpg',
    'images/4.jpg',
    'images/5.jpg',
]

if __name__ == '__main__':
    start = time.perf_counter()

    # create processes
    processes = [multiprocessing.Process(target=create_thumbnail, args=[filename]) 
                for filename in filenames]

    # start the processes
    for process in processes:
        process.start()

    # wait for completion
    for process in processes:
        process.join()

    finish = time.perf_counter()

    print(f'It took {finish-start: .2f} second(s) to finish')


# In[10]:


# WITH PROCESSPOOLEXECUTOR
import time
import os
from concurrent.futures import ProcessPoolExecutor
from PIL import Image, ImageFilter
from task_sample import create_thumbnail

filenames = [
    'images/1.jpg',
    'images/2.jpg',
    'images/3.jpg',
    'images/4.jpg',
    'images/5.jpg',
]

if __name__ == '__main__':
    start = time.perf_counter()

    with ProcessPoolExecutor() as executor:
        executor.map(create_thumbnail, filenames)
   
    finish = time.perf_counter()

    print(f'It took {finish-start: .2f} second(s) to finish')


# In[ ]:




