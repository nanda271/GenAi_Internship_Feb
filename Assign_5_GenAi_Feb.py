#!/usr/bin/env python
# coding: utf-8

# In[1]:


#prblm1  Social Media-Post engagement Analyzer

def post_engagement():
    likes = [200, 150, 300, 250, 150]
    total = 0
    for i in likes:
        total = total + i
    print("Total Likes:", total)
    if total >= 1000:
        print("Post Status: Viral Post")
    else:
        print("Post Status: Normal Engagement")
post_engagement()


# In[2]:


#prblm2 Healthcare-Medicine Stock Alert System

def check_medicine_stock():
    stock = 6   
    print("Medicine Stock:", stock)
    if stock < 10:
        print("Status: Low Stock Alert")
    else:
        print("Status: Stock Sufficient")
check_medicine_stock()


# In[3]:


#prblm 3 Agriculture Rainfall Adequacy Checker

def rainfall_checker():
    rainfall_data = [70, 75, 80, 65, 70]   
    required_level = 70
    total = 0
    count = 0
    for value in rainfall_data:
        total = total + value
        count = count + 1
    average = total / count
    print("Average Rainfall:", int(average))
    if average >= required_level:
        print("Rainfall Status: Adequate Rainfall")
    else:
        print("Rainfall Status: Inadequate Rainfall")
rainfall_checker()


# In[4]:


#prblm 4 Social Media Duplicate Account detection

def check_duplicate_accounts():
    usernames = ["rahul123", "sneha45", "amit99", "rahul123"]   
    unique_users = set(usernames)
    if len(usernames) != len(unique_users):
        print("Duplicate Accounts Found: Yes")
    else:
        print("Duplicate Accounts Found: No")
check_duplicate_accounts()


# In[5]:


#prblm 5 Healthcare-Appointment Eligibilty Checker

def check_appointment_eligibility():
    age = 21   # example age
    print("Patient Age:", age)
    if age >= 18:
        print("Eligibility Status: Eligible")
    else:
        print("Eligibility Status: Not Eligible")
check_appointment_eligibility()


# In[6]:


#prblm 6 Agriculture-Premium Crop Price Filter

def premium_crop_filter():
    prices = [1500, 2500, 1800, 3200, 1900]   
    premium_list = []
    for price in prices:
        if price > 2000:
            premium_list.append(price)
    print("Premium Crops:", premium_list)
premium_crop_filter()


# In[7]:


#prblm 7 System monitoring Application with checker

def application_health_checker():
    errors = 7   
    print("Error Count:", errors)
    if errors == 0:
        print("System Status: Healthy")
    elif errors <= 5:
        print("System Status: Minor Issues")
    else:
        print("System Status: Critical Issues")
application_health_checker()


# In[8]:


#prblm 8 Banking daily transaction lomit checker

def check_transaction_limit():
    amount = 60000   
    daily_limit = 50000
    print("Transaction Amount:", amount)
    if amount <= daily_limit:
        print("Transaction Status: Approved")
    else:
        print("Transaction Status: Rejected")
check_transaction_limit()


# In[9]:


#prblm 9 E-Learning-Student Attendance Eligibility SYstem

def attendance_checker():

    attendance_record = [1, 1, 0, 1, 1]  
    total_classes = 0
    present_count = 0
    for status in attendance_record:
        total_classes = total_classes + 1
        if status == 1:
            present_count = present_count + 1
    percentage = (present_count / total_classes) * 100
    print("Attendance Percentage:", percentage)
    if percentage >= 75:
        print("Exam Eligibility: Eligible")
    else:
        print("Exam Eligibility: Not Eligible")
attendance_checker()


# In[11]:


#prblm 10 Smart Electricity Bill Analyzer

def electricity_bill(units):
    bill = 0
    if units <= 100:
        bill = units * 3
    elif units <= 200:
        bill = 100 * 3 + (units - 100) * 5
    else:
        bill = 100 * 3 + 100 * 5 + (units - 200) * 7
    if bill < 500:
        usage = "Low Usage"
    elif bill <= 1500:
        usage = "Moderate Usage"
    else:
        usage = "High Usage"
    return bill, usage
units_consumed = int(input("Enter the number of units consumed: "))
total_bill, usage_status = electricity_bill(units_consumed)
print("Total Bill: ₹", total_bill)
print("Usage Status:", usage_status)


# In[ ]:




