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

for line in json_data:
    

jsonfile.close()


