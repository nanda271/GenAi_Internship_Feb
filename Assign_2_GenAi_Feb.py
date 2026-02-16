#!/usr/bin/env python
# coding: utf-8

# In[2]:


sentence=input("Enter the sentence: ")
words=sentence.split()
unique_words=set(words)
print("Words count",len(unique_words))
print("Unique words",unique_words)


# In[3]:


#Problem 1
sentence=input("Enter the sentence: ")
words=sentence.split()
unique_words = []
for word in words:
    if word not in unique_words:
        unique_words.append(word)
print("Words count",len(unique_words))
print("Unique words",unique_words)


# In[4]:


#Problem 2
employees={}
n=int(input("Enter number of employees: "))
for i in range(n):
    name=input("Enter employee name: ")
    salary=int(input("Enter salary: "))
    employees[name]=salary
max_salary=max(employees.values())
for name, salary in employees.items():
    if salary == max_salary:
        print("Highest Salary:", name, "-", salary)


# In[6]:


#Problem 3
numbers=[]
n=int(input("How many numbers: "))
for i in range(n):
    num=int(input("Enter number: "))
    numbers.append(num)
max=numbers[0]
min=numbers[0]
for num in numbers:
    if num>max:
        max=num
    if num<min:
        min=num
print("List:", numbers)
print("Max:", max)
print("Min:", min)


# In[7]:


#Problem 4
prices = []
num_products = int(input("enter the no of products: "))
for i in range(num_products):
    p = int(input("Enter price: "))
    prices.append(p)
above_1000 = 0
for price in prices:
    if price > 1000:
        above_1000 = above_1000 + 1
print("Products above 1000:", above_1000)


# In[9]:


#Problem 5
attendance = []
n=int(input("Enter total number of days: "))
for i in range(n):
    status = input("Enter 'P' for Present or 'A' for Absent: ")
    attendance.append(status)
present_days = 0
for day in attendance:
    if day == "P":
        present_days = present_days + 1
attendance_percentage = (present_days / n) * 100
print("Attendance Percentage:", attendance_percentage)


# In[10]:


#Problem 6
phone_numbers = []
n = int(input("Enter number of phone numbers: "))
for i in range(n):
    num = int(input("Enter phone number: "))
    phone_numbers.append(num)
unique_numbers = []
for num in phone_numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print("Unique phone numbers:", unique_numbers)


# In[11]:


#Problem 7
text = input("Enter a string: ")
char_count = {}
for char in text:
    if char in char_count:
        char_count[char] = char_count[char] + 1
    else:
        char_count[char] = 1
print(char_count)


# In[12]:


#Problem 8
numbers = []
n = int(input("How many numbers: "))
for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)
numbers_tuple = tuple(numbers)
print("Tuple:", numbers_tuple)


# In[13]:


#Problem 9
employees = {}
n = int(input("Enter number of employees: "))
for i in range(n):
    name = input("Enter employee name: ")
    salary = int(input("Enter salary: "))
    employees[name] = salary
key_to_check = input("Enter employee name to check: ")
if key_to_check in employees:
    print("Employee exists")
else:
    print("Employee does not exist")


# In[14]:


#Problem 10
marks = []
n = int(input("Enter number of subjects: "))
for i in range(n):
    m = float(input("Enter marks: "))
    marks.append(m)
total = 0
for mark in marks:
    total = total + mark
average = total / n
print("Average Marks:", average)


# In[ ]:




