#!/usr/bin/env python
# coding: utf-8

# In[79]:


import json

xy = json.load(open('profiles.json'))
xy


# In[10]:


type(xy)


# - Total number of users: 19

# In[58]:


num_users = len(xy)


# - Number of active users: 9

# In[16]:


active = 0
for user in xy:
    if user['isActive'] == True:
        active += 1
print(active)


# - Number of inactive users: 10

# In[18]:


inactive = 0
for user in xy:
    if user['isActive'] == False:
        inactive += 1
print(inactive)


# - Grand total of balances for all users: $52,667.02

# In[80]:


balances = []
collector = ''
cleaned_balances = []

for user in xy:
    balances.append(user['balance'])
for el in balances:
    for ch in el:
        if ch.isdigit() or ch == '.':
            collector += ch
    cleaned_balances.append(float(collector))
    collector = ''
print(sum(cleaned_balances))


# - Average balance per user: $2,771.95

# In[81]:


round((sum(cleaned_balances) / num_users), 2)


# - User with the lowest balance: Avery Flynn ($1,214.10)

# In[95]:


collect = ''
lowest_balance = ['name',1000000]
for user in xy:
    for ch in user['balance']:
        if ch.isdigit() or ch == '.':
            collect += ch
            
    if float(collect) < float(lowest_balance[1]):
        lowest_balance[0] = user['name']
        lowest_balance[1] = collect
    collect = ''

print(lowest_balance) 


# - User with the highest balance: Fay Hammond ($3,919.64)

# In[98]:


collect = ''
highest_balance = ['name', .01]
for user in xy:
    for ch in user['balance']:
        if ch.isdigit() or ch == '.':
            collect += ch
            
    if float(collect) > float(highest_balance[1]):
        highest_balance[0] = user['name']
        highest_balance[1] = collect
    collect = ''

print(highest_balance) 


# - Most common favorite fruit: strawberry

# In[105]:


fruits = {}

for user in xy:
    if user['favoriteFruit'] in fruits.keys():
        fruits[user['favoriteFruit']] += 1
    else:
        fruits[user['favoriteFruit']] = 1

print(max(fruits, key = fruits.get))


# - Least most common favorite fruit: apple

# In[107]:


print(min(fruits, key = fruits.get))


# - Total number of unread messages for all users: 210

# In[111]:


unread_messages = 0
for user in xy:
    for str in user['greeting'].split():
        if str.isdigit():
            unread_messages += int(str)
print(unread_messages)


# In[ ]:




