#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Employee performance bonus eleigibility

employees = {}
n = int(input("Enter number of employees: "))
for i in range(n):
    name = input("Enter employee name: ")
    score = int(input("Enter performance score: "))
    employees[name] = score
highest_score = max(employees.values())
top_performers = []
for name in employees:
    if employees[name] == highest_score:
        top_performers.append(name)
print("Top Performers Eligible for Bonus:", ", ".join(top_performers), "(Score:", highest_score, ")")


# In[3]:


#Prgm 2 Search Query Keyword Analysis

query = input("Enter search query: ")
query = query.lower()
for ch in ".,!?;:":
    query = query.replace(ch, "")
words = query.split()
count = {}
for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
result = {}

for word in count:
    if count[word] > 1:
        result[word] = count[word]
print(result)


# In[5]:


#prgm 3 Sensor Data Validation

sensor_readings = [3, 4, 7, 8, 10, 12, 5]
valid_readings = []
for i in range(len(sensor_readings)):
    if sensor_readings[i] % 2 == 0:
        valid_readings.append((i, sensor_readings[i]))
print("Valid Sensor Readings (Hour, Value):")
print(valid_readings)


# In[7]:


#prgm 4 Email domain usage analysis

emails = [
    "ravi@gmail.com",
    "anita@yahoo.com",
    "kiran@gmail.com",
    "suresh@gmail.com",
    "meena@yahoo.com"
]
domain_count = {}
for email in emails:
    parts = email.split("@")
    domain = parts[1]

    if domain in domain_count:
        domain_count[domain] = domain_count[domain] + 1
    else:
        domain_count[domain] = 1
total = len(emails)
for domain in domain_count:
    percent = (domain_count[domain] / total) * 100
    print(domain + ":", int(percent), "%")


# In[8]:


#prgm 5 Sales Spike Detection

sales = [1200, 1500, 900, 2200, 1400, 3000]
total = 0
for s in sales:
    total = total + s
average = total / len(sales)
limit = average + (0.30 * average)
for i in range(len(sales)):
    if sales[i] > limit:
        print("Day", i + 1, ":", sales[i])


# In[10]:


#prgm 6 duplicate used id detection

user_ids = ["user1", "user2", "user1", "user3", "user1", "user3"]
count = {}
for uid in user_ids:
    if uid in count:
        count[uid] = count[uid] + 1
    else:
        count[uid] = 1
for uid in count:
    if count[uid] > 1:
        print(uid, "→", count[uid], "times")


# In[ ]:




