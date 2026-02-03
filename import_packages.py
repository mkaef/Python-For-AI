# IMPORT PACKAGES
"""
Using packages
Python packages add new functionality to your programs. There are two types:
Built-in: Come with Python (no installation needed)
External: Need to install first with pip
​
Understanding the terminology
Let’s clarify what these terms mean:
Module: A single Python file (like math.py)
Package: A folder containing multiple modules
Function: A reusable block of code (like print() or sqrt())
Class: A blueprint for creating objects (we’ll cover this later)
Think of it like this:
A module is like a toolbox
A package is like a garage with multiple toolboxes
A function is like a specific tool (hammer, screwdriver)
A class is like a blueprint for building tools
"""
# Import pattern explained
# Pattern1: Import the whole module
import math
math.sqrt(25) # 5.0

# Pattern 2: Import specific items from a module
from math import sqrt, pi
sqrt(100)  # 10.0

# Build-in modules
# Import entire module
import random

# Use module functions
number = random.randint(1, 10)

choice = random.choice(["apple", "banana", "orange"])

# Common built-in modules
# Date and time
import datetime
today = datetime.date.today()
print(today) # 2026-01-24

# Operating system
import os
current_dir = os.getcwd()
print(current_dir)    # c:\PythonProjects\python-for-ai

# JSON data
import json
data = {"name": "Andrew", "age": 25}
json_string = json.dumps(data)   # '{"name": "Andrew", "age": 25}'

# Import methods
# Import entire module
import math
result = math.sqrt(25)

# Import specific function
from math import sqrt, pi
result = sqrt(36)
circle_area = pi * radius ** 2

# Import with alias
import pandas as pd
df = pd.DataFrame(data)

# form everything (avoid this)
from math import *

# Using external packages
import requests

response = requests.get("https://api.example.com/data")
data = response.json()

# Data analysis
import pandas as pd

# Create a simple DataFrame
data = {
    'name':['Tim', 'Andrew', 'Tica'],
    'age':[40, 25, 32],
    'city':['Libreville', 'Odessa', 'Lubbock']
    }
df = pd.DataFrame(data)
print(df)