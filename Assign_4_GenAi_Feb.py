#!/usr/bin/env python
# coding: utf-8

# In[1]:


# prblm 1 : MObile Recharge Validation System

valid_plans = [199, 299, 399, 599]
while True:
    amount = int(input("Enter recharge amount: "))

    if amount < 50:
        print("Amount should be at least ₹50")
    elif amount not in valid_plans:
        print("Invalid plan. Available plans are 199, 299, 399, 599")
    else:
        print("Recharge Successful")
        break
    print("Try again\n")


# In[2]:


#prblm 2 Inventory Reorder Alert System

def check_inventory(stock):
    for product, quantity in stock.items():
        if quantity < 15:
            print(product, "- Reorder Alert")
        else:
            print(product, "- Stock OK")
products = {
    "Pen": 12,
    "Notebook": 25,
    "Pencil": 8,
    "Eraser": 30
}

check_inventory(products)


# In[3]:


# Student Result Processing System

def check_result(marks):
    total = 0
    
    for m in marks:
        total = total + m
    
    average = total / len(marks)
    
    if average >= 50:
        return "Pass"
    else:
        return "Fail"
    
student_marks = [60, 45, 70, 55]
result = check_result(student_marks)
print("Average:", sum(student_marks)/len(student_marks))
print("Result:", result)


# In[4]:


# prblm 3 Student Result Processing System

def check_result(marks):
    total = 0  
    for m in marks:
        total = total + m  
    average = total / len(marks)
    if average >= 50:
        return average, "Pass"
    else:
        return average, "Fail"

marks = []
n = int(input("Enter number of subjects: "))
for i in range(n):
    mark = int(input("Enter mark: "))
    marks.append(mark)
    
avg, result = check_result(marks)
print("Average:", avg)
print("Result:", result)


# In[5]:


#prblm 4 cab fare estimator with retry option

def calculate_fare(distance, peak):
    fare = 50 + (12 * distance)
    
    if peak == "yes":
        fare = fare + (fare * 0.25)
    
    return round(fare, 2)
while True:
    distance = float(input("Enter distance in km: "))
    peak = input("Is it peak hour? (yes/no): ")
    
    total_fare = calculate_fare(distance, peak.lower())
    
    print("Total Fare: ₹", total_fare)
    
    choice = input("Do you want to calculate again? (yes/no): ")
    if choice.lower() != "yes":
        break


# In[7]:


#prblm 5 Employee Attendance ELigibilty checker

def check_eligibility(attendance_list):
    total_days = len(attendance_list)
    present_days = 0
    
    for day in attendance_list:
        if day == "P":
            present_days += 1
    
    attendance_percentage = (present_days / total_days) * 100
    print("Attendance Percentage: {:.2f}%".format(attendance_percentage))
    
    if attendance_percentage >= 75:
        return "Eligible"
    else:
        return "Not Eligible"

attendance = input("Enter attendance list (P for present, A for absent, separated by spaces): ").split()
result = check_eligibility(attendance)
print("Employee is:", result)



# In[9]:


#prblm 6 Password Strenghth Checker

def check_password_strength(password):
    special_chars = "@#$"
    has_digit = False
    has_special = False
    
    if len(password) < 8:
        return False
    
    for char in password:
        if char.isdigit():
            has_digit = True
        if char in special_chars:
            has_special = True
    
    if has_digit and has_special:
        return True
    else:
        return False
while True:
    password = input("Enter password to check strength: ")
    
    if check_password_strength(password):
        print("Strong Password ✅")
        break
    else:
        print("Weak Password ❌, try again")


# In[ ]:




