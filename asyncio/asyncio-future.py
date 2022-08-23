#!/usr/bin/env python
# coding: utf-8

# In[1]:


import asyncio
from asyncio import Future


async def main():
    my_future = Future()
    print(my_future.done())  # False

    my_future.set_result('Bright')

    print(my_future.done())  # True

    print(my_future.result())


# Esse código não vai funcionar dentro do Jupyter
# asyncio.run(main())

# Esse vai
await main()


# In[3]:


from asyncio import Future
import asyncio


async def plan(my_future):
    print('Planning my future...')
    await asyncio.sleep(4)
    my_future.set_result('Bright')


def create() -> Future:
    my_future = Future()
    asyncio.create_task(plan(my_future))
    return my_future


async def main():
    my_future = create()
    result = await my_future

    print(result)


# Esse código não vai funcionar dentro do Jupyter
# asyncio.run(main())

# Esse vai
await main()


# In[ ]:




