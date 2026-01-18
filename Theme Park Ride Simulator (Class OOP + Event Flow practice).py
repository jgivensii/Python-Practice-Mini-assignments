# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 12:15:03 2026

@author: jgive

Theme Park Ride Simulator — Data Persistence + Event Flow
This script builds a simple but expandable theme‑park ride simulator. It collects a guest’s name 
and favorite ride, stores that information in a persistent CSV file, and then processes each guest
through a sequence of ride‑related events. 
The program uses:

- pandas for data storage

- Queue for event sequencing

- Custom event classes to model arrival, line entry, ride start, and ride exit

- CSV persistence so the attendance list grows across multiple runs

Each time the script runs, it appends a new guest to ride_attendance.csv and 
then simulates the full ride experience for every guest stored so far.
"""

import pandas as pd
import numpy as np
from queue import Queue as que
import os

Person = input("Input a name: ")
Coaster = input("Input a theme park ride: ")

if os.path.exists("ride_attendance.csv"):
    Ride_attendance = pd.read_csv("ride_attendance.csv")
    Ride_attendance.loc[len(Ride_attendance)] = {"name": Person, "coaster": Coaster}
    Ride_attendance.to_csv("ride_attendance.csv", index=False)
else:
    Ride_attendance = pd.DataFrame(columns = ["name", "coaster"])
    Ride_attendance.loc[len(Ride_attendance)] = {"name": Person, "coaster": Coaster}
    Ride_attendance.to_csv("ride_attendance.csv", index=False)
   
class ArrivalEvent:
    def __init__(self,guest):
        self.guest = guest
    
    def welcome(self):
        return f"{self.guest} has arrived."
        
    
class RideRequestEvent:
    def __init__(self, ride):
        self.ride = ride 
        
    def getInLine(self, guest):

        return f"{guest} is getting in line for the {self.ride}."    
        
class RideStartEvent:
        
    def takeoff(self):
        return "Weeeeeeeeeee"
    
class RideEndEvent:
    
    def getOff(self, guest, ride):
        return f"{guest} has got off {ride}."
    
line = que()
for i in range(len(Ride_attendance)):
    line.put(Ride_attendance.loc[i])

while not line.empty():
    current = line.get()
    print(ArrivalEvent(current['name']).welcome())
    print(RideRequestEvent(current['coaster']).getInLine(current['name']))
    print(RideStartEvent().takeoff())
    print(RideEndEvent().getOff(current['name'], current['coaster']))

"""
This version of the simulator shows real progress in structuring a small event‑driven system. 
A few strengths stand out:

-Persistent storage: Using os.path.exists and CSV read/write logic ensures the DataFrame survives across runs.
 This is a major conceptual step — you’ve moved from ephemeral scripts to a program that accumulates state over time.

-Clear event modeling: Each event class has a single responsibility and returns a clean, readable message. 
 This mirrors real event‑driven architecture and sets you up for more complex simulations later.

-Queue‑based flow: Using Queue() to process each guest in order is a strong design choice. 
 It mirrors real‑world ride lines and keeps the logic scalable.

-Correct DataFrame row insertion: Using .loc[len(df)] = {...} shows you’ve internalized how pandas handles row creation, 
 which is a foundational skill for data‑driven simulations.

There’s also a natural path forward. You could expand this into multi‑ride systems, timed events, ride capacity limits, 
or even a full simulation loop. But as it stands, the script is clean, readable, and demonstrates a solid grasp of 
object‑oriented thinking combined with data persistence.

If you want to build a markdown section that documents the event flow or outlines future improvements, 
I can help shape that next.
"""