#!/usr/bin/env python
# coding: utf-8

# In[5]:


import asyncio


async def call_api(message, result, delay=3):
    print(message)
    await asyncio.sleep(delay)
    return result


async def main():
    a, b, c, d, e, f = await asyncio.gather(
        call_api(message='Calling API 1 ...', result = 60, delay = 3),
        call_api(message='Calling API 2 ...', result = 2, delay = 4),
        call_api(message='Calling API 3 ...', result = 400, delay = 2),
        call_api(message='Calling API 4 ...', result = 20, delay = 1),
        call_api(message='Calling API 5 ...', result = 5, delay = 5),
        call_api(message='Calling API 6 ...', result = 2000, delay = 6)
    )
    print(a, b, c, d, e, f)
    
#     ou
#     a = await asyncio.gather(
#         call_api(message='Calling API 1 ...', result = 60, delay = 3),
#         call_api(message='Calling API 2 ...', result = 2, delay = 4),
#         call_api(message='Calling API 3 ...', result = 400, delay = 2),
#         call_api(message='Calling API 4 ...', result = 20, delay = 1),
#         call_api(message='Calling API 5 ...', result = 5, delay = 5),
#         call_api(message='Calling API 6 ...', result = 2000, delay = 6)
#     )
#     for res in a:
#         print(res)


# Esse código não vai funcionar dentro do Jupyter
# asyncio.run(main())

# Esse vai
await main()


# In[6]:


# Nesse exemplo, qualquer exceção irá derrubar a execução toda
import asyncio


class APIError(Exception):
    def __init__(self, message):
        self._message = message

    def __str__(self):
        return self._message


async def call_api_failed():
    await asyncio.sleep(3)
    raise APIError('API failed')


async def call_api(message, result, delay=3):
    print(message)
    await asyncio.sleep(delay)
    return result


async def main():
    a, b, c, d = await asyncio.gather(
        call_api('Calling API 1 ...', 100, 5),
        call_api('Calling API 2 ...', 200, 2),
        call_api_failed(),
        call_api('Calling API 4 ...', 100, 3),
    )
    print(a, b, c, d)


# Esse código não vai funcionar dentro do Jupyter
# asyncio.run(main())

# Esse vai
await main()


# In[8]:


# Nesse exemplo, qualquer exceção NÃO irá derrubar a execução toda
import asyncio


class APIError(Exception):
    def __init__(self, message):
        self._message = message

    def __str__(self):
        return self._message


async def call_api_failed():
    await asyncio.sleep(3)
    raise APIError('<API failed>')


async def call_api(message, result, delay=3):
    print(message)
    await asyncio.sleep(delay)
    return result


async def main():
    a, b, c, d = await asyncio.gather(
        call_api('Calling API 1 ...', 100, 5),
        call_api('Calling API 2 ...', 200, 2),
        call_api_failed(),
        call_api('Calling API 4 ...', 100, 3),
        return_exceptions=True
    )
    print(a, b, c, d)


# Esse código não vai funcionar dentro do Jupyter
# asyncio.run(main())

# Esse vai
await main()


# In[ ]:




