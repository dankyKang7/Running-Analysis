#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 18:29:01 2019

@author: admin
"""

#This script will open the json location history file and find when I'm running.
#This will be a multi=step process to open the data. 
# Step 1: explore the json data to find my targets
# Step 2: find the locaiton history and generate data of run occurences by
# and distance
# Step 3: anlayze the run data for performance. 
# Step 4: iterate!

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json


# Get the json data into python

os.chdir('/Users/admin/Blog_Data/Takeout/Location History')

# get teh json file
file = "Location History.json"

with open(file,'r') as jsonfile:
    lochist = jsonfile.read()
    
json_data = json.loads(lochist)

# this is one large dictionary with 1 key -> Locations
# let's dump melt that into another dictionary called points..

#this creates a list of dictionaries
location_history = json_data['locations']
running_history = []
#Get the length of the dictionary 
for locdict in location_history:
    running_history.append()
   # for location_point,location_value in locdict.items():
   #     location_hist = pd.DataFrame.from_dict()
        
        
        
        


#points = [1]

    
    
    

    

jsonfile.close()


