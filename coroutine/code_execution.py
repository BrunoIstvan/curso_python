#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install asyncio')


# In[2]:


# Ocorre erro pois é retornado uma coroutine que nunca é aguardada

async def square(number: int) -> int:
    return number*number


result = square(10)
print(square)


# In[14]:


# Essa versão a função é enviada para um loop no método asyncio.run e é aguardado o retorno para prosseguir
import asyncio

async def square(number: int) -> int:
    return number*number

# Esse código não vai funcionar dentro do Jupyter
#result = asyncio.run(square(10))

# Esse vai
result = await square(10)

print(result)


# In[15]:


import asyncio

async def square(number: int) -> int:
    return number*number

async def main() -> None:
    x = await square(10)
    print(f'x={x}')

    y = await square(5)
    print(f'y={y}')

    print(f'total={x+y}')
    
# Esse código não vai funcionar dentro do Jupyter
# asyncio.run(main())

# Esse vai
await main()


# In[17]:


# usando asyncio.sleep
import asyncio
import time


async def call_api(message, result=1000, delay=3):
    print(message)
    await asyncio.sleep(delay)
    return result


async def main():
    start = time.perf_counter()

    price = await call_api('Get stock price of GOOG...', 300)
    print(price)

    price = await call_api('Get stock price of APPL...', 400)
    print(price)

    end = time.perf_counter()
    print(f'It took {round(end-start,0)} second(s) to complete.')

# Esse código não vai funcionar dentro do Jupyter
# asyncio.run(main())

# Esse vai
await main()


# In[18]:


# usando asyncio.create_task
import asyncio
import time


async def call_api(message, result=1000, delay=3):
    print(message)
    await asyncio.sleep(delay)
    return result


async def main():
    start = time.perf_counter()

    task_1 = asyncio.create_task(
        call_api('Get stock price of GOOG...', 300)
    )

    task_2 = asyncio.create_task(
        call_api('Get stock price of APPL...', 300)
    )

    price = await task_1
    print(price)

    price = await task_2
    print(price)

    end = time.perf_counter()
    print(f'It took {round(end-start,0)} second(s) to complete.')


# Esse código não vai funcionar dentro do Jupyter
# asyncio.run(main())

# Esse vai
await main()


# In[19]:


import asyncio
import time


async def call_api(message, result=1000, delay=3):
    print(message)
    await asyncio.sleep(delay)
    return result


async def show_message():
    for _ in range(3):
        await asyncio.sleep(1)
        print('API call is in progress...')


async def main():
    start = time.perf_counter()

    message_task = asyncio.create_task(
        show_message()
    )

    task_1 = asyncio.create_task(
        call_api('Get stock price of GOOG...', 300)
    )

    task_2 = asyncio.create_task(
        call_api('Get stock price of APPL...', 300)
    )

    price = await task_1
    print(price)

    price = await task_2
    print(price)

    await message_task

    end = time.perf_counter()
    print(f'It took {round(end-start,0)} second(s) to complete.')


# Esse código não vai funcionar dentro do Jupyter
# asyncio.run(main())

# Esse vai
await main()


# In[26]:


# USANDO cancel PARA CANCELAR UMA TASK
import asyncio
from asyncio import CancelledError


async def call_api(message, result=1000, delay=3):
    print(message)
    await asyncio.sleep(delay)
    return result


async def main():
    task = asyncio.create_task(
        call_api('Calling API...', result=2000, delay=5)
    )

    time_elapsed = 0
    while not task.done():
        time_elapsed += 1
        await asyncio.sleep(1)
        print('Task has not completed, checking again in a second')
        if time_elapsed == 3:
            print('Cancelling the task...')
            task.cancel()
            break

    try:
        print(await task)
    except CancelledError:
        print('Task has been cancelled.')


# Esse código não vai funcionar dentro do Jupyter
# asyncio.run(main())

# Esse vai
await main()


# In[30]:


# USANDO wait_for PARA CANCELAR UMA TASK APOS TIMEOUT
import asyncio
from asyncio.exceptions import TimeoutError


async def call_api(message, result=1000, delay=3):
    print(message)
    await asyncio.sleep(delay)
    return result


async def main():
    task = asyncio.create_task(
        call_api('Calling API...', result=2000, delay=5)
    )

    MAX_TIMEOUT = 3
    try:
        print(await asyncio.wait_for(task, timeout=MAX_TIMEOUT))
    except TimeoutError:
        print('The task was cancelled due to a timeout')

# Esse código não vai funcionar dentro do Jupyter
# asyncio.run(main())

# Esse vai
await main()


# In[32]:


# USANDO shield PARA EVITAR O CANCELAMENTO E AVISAR SOBRE A DEMORA DA EXECUCAO
import asyncio
from asyncio.exceptions import TimeoutError


async def call_api(message, result=1000, delay=3):
    print(message)
    await asyncio.sleep(delay)
    return result


async def main():
    task = asyncio.create_task(
        call_api('Calling API...', result=2000, delay=5)
    )

    MAX_TIMEOUT = 3
    try:
        print(await asyncio.wait_for(asyncio.shield(task), timeout=MAX_TIMEOUT))
    except TimeoutError:
        print('The task took more than expected and will complete soon.')
        result = await task
        print(result)

# Esse código não vai funcionar dentro do Jupyter
# asyncio.run(main())

# Esse vai
await main()


# In[ ]:




