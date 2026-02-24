#!/usr/bin/env python
# coding: utf-8

# In[1]:


#prblm 1 Smart Parking Lot Management System

def smart_parking_system(capacity, logs):
    parked = 0
    peak = 0
    for log in logs:
        if log == "IN":
            parked += 1
            if parked > peak:
                peak = parked
        elif log == "OUT":
            if parked > 0:
                parked -= 1
    print("Currently Parked Vehicles:", parked)
    print("Peak Parking Usage:", peak)

    if parked > capacity:
        print("Parking Status: Exceeded Capacity")
    elif parked == capacity:
        print("Parking Status: Full")
    else:
        print("Parking Status: Available")
capacity = 50
vehicle_logs = ["IN", "IN", "IN", "OUT", "IN", "IN", "OUT"]
smart_parking_system(capacity, vehicle_logs)


# In[4]:


#prblm 2 Online Food Delivery time estimator

def estimate_delivery_time(distance, traffic, weather):
    # assuming average city delivery speed is 15 km per hour
    avg_speed = 15  
    base_time = (distance / avg_speed) * 60  
    if traffic.lower() == "high":
        base_time += 15
    elif traffic.lower() == "medium":
        base_time += 10
    elif traffic.lower() == "low":
        base_time += 5
    if weather.lower() == "rainy":
        base_time += 8
    elif weather.lower() == "stormy":
        base_time += 20
    elif weather.lower() == "clear":
        base_time += 0
    final_time = round(base_time)
    print("Estimated Delivery Time:", final_time, "minutes")
distance = 8
traffic_level = "High"
weather_condition = "Rainy"
estimate_delivery_time(distance, traffic_level, weather_condition)


# In[5]:


#prblm 3 Movie Theatre Seat occupancy

def analyze_seat_occupancy(total_seats, booked_seats):
    booked_count = len(booked_seats)

    occupancy = (booked_count / total_seats) * 100
    print("Occupancy:", int(occupancy), "%")

    if occupancy == 100:
        print("Show Status: Housefull")
        print("Suggestion: Open additional show")
    elif occupancy >= 75:
        print("Show Status: Almost Full")
    else:
        print("Show Status: Seats Available")
total_seats = 200
booked_seats = [1] * 150
analyze_seat_occupancy(total_seats, booked_seats)


# In[6]:


#prblm 4 cloud server load classificaiton system

def classify_server_load(cpu_readings):
    total = 0
    for value in cpu_readings:
        total += value    
    average = total / len(cpu_readings) 
    print("Average CPU Load:", int(average), "%")
    if average < 50:
        print("Server Status: Normal")
    elif average <= 80:
        print("Server Status: Warning")
    else:
        print("Server Status: Critical")

cpu_data = [45, 60, 70, 85, 90]
classify_server_load(cpu_data)


# In[7]:


#prblm 5 Smart classroom resource usage monitor

def monitor_resource_usage(resource_data):
    overused = []

    limit = 8

    for resource in resource_data:
        hours = resource_data[resource]
        if hours > limit:
            overused.append(resource)

    if overused:
        print("Overused Resources:", ", ".join(overused))
        print("Energy Alert: Yes")
    else:
        print("Overused Resources: None")
        print("Energy Alert: No")

resources = {
    "Projector": 6,
    "AC": 9,
    "Lights": 4
}
monitor_resource_usage(resources)


# In[8]:


#prblm 6 Online event registration capacity controller

def manage_event_registration(capacity, total_registrations):
    confirmed = 0
    waitlisted = 0

    for i in range(total_registrations):
        if confirmed < capacity:
            confirmed += 1
        else:
            waitlisted += 1
    print("Confirmed Registrations:", confirmed)
    print("Waitlisted Users:", waitlisted)

    if confirmed >= capacity:
        print("Registration Status: Closed")
    else:
        print("Registration Status: Open")

event_capacity = 100
registrations = 105
manage_event_registration(event_capacity, registrations)


# In[ ]:




