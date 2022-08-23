#!/usr/bin/env python
# coding: utf-8

# In[6]:


stocks = {
    'AAPL': 121,
    'AMZN': 3380,
    'MSFT': 219,
    'BIIB': 280,
    'QDEL': 166,
    'LVGO': 244
}


# In[7]:


# Sem dictionary-comprehension

new_stocks = {}
for symbol, price in stocks.items():
    new_stocks[symbol] = price*1.02

print(new_stocks)


# In[8]:


# Com dictionary-comprehension

new_stocks = {symbol: price * 1.02 for (symbol, price) in stocks.items()}

print(new_stocks)


# In[9]:


# Sem dictionary-comprehension

selected_stocks = {}
for symbol, price in stocks.items():
    if price > 200:
        selected_stocks[symbol] = price

print(selected_stocks)


# In[10]:


# Com dictionary-comprehension

selected_stocks = {s: p for (s, p) in stocks.items() if p > 200}

print(selected_stocks)

