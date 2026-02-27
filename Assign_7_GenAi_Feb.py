#!/usr/bin/env python
# coding: utf-8

# In[3]:


#prblm 1 Smart light controller

class SmartLight:
    def __init__(self, name):
        self.name = name
        self.status = "OFF"   
    def turn_on(self):
        self.status = "ON"
    def turn_off(self):
        self.status = "OFF"
    def show_status(self):
        print(self.name + " is " + self.status)

light_name = input("Light Name: ")
action = input("Action: ")
my_light = SmartLight(light_name)

if action.upper() == "ON":
    my_light.turn_on()
elif action.upper() == "OFF":
    my_light.turn_off()
else:
    print("Invalid Action")

my_light.show_status()


# In[4]:


#prblm 2 Employee ID card system

class Employee:   
    def __init__(self, name, emp_id, department):
        self.name = name
        self.emp_id = emp_id
        self.department = department
    
    def display_id_card(self):
        print("\n----- Employee ID Card -----")
        print("Employee Name :", self.name)
        print("Employee ID   :", self.emp_id)
        print("Department    :", self.department)
        print("----------------------------")
name = input("Employee Name: ")
emp_id = input("Employee ID: ")
dept = input("Department: ")

emp1 = Employee(name, emp_id, dept)
emp1.display_id_card()


# In[5]:


#prblm 3 Mobile Contact Record

class Contact:   
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone   
    def display_contact(self):
        print("\nContact Saved")
        print("Name:", self.name)
        print("Phone:", self.phone)

contact_name = input("Contact Name: ")
phone_number = input("Phone Number: ")

contact1 = Contact(contact_name, phone_number)
contact1.display_contact()


# In[6]:


#prblm 4 Product price tag generator

class Product:   
    def __init__(self, name, price):
        self.name = name
        self.price = price  
    def print_price_tag(self):
        print("\nProduct:", self.name)
        print("Price: ₹" + str(self.price))

product_name = input("Product Name: ")
product_price = input("Price: ")

item1 = Product(product_name, product_price)
item1.print_price_tag()


# In[7]:


#prblm 5 Movie rating display system

class Movie:   
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating   
    def show_details(self):
        print("\nMovie Details")
        print("Movie Name :", self.name)
        print("Rating     :", self.rating)

movie_name = input("Movie Name: ")
movie_rating = input("Rating: ")
movie1 = Movie(movie_name, movie_rating)
movie1.show_details()


# In[8]:


#prblm 6 Delivery adress manager

class Delivery:   
    def __init__(self, customer_name, address):
        self.customer_name = customer_name
        self.address = address    
    def print_details(self):
        print("\nDelivery Details")
        print("Customer:", self.customer_name)
        print("Address:", self.address)

name = input("Customer Name: ")
addr = input("Address: ")
delivery1 = Delivery(name, addr)
delivery1.print_details()


# In[ ]:




