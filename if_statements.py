# IF STATEMENTS
"""
If statements let your program make decisions. 
They check if something is true or false, then act accordingly.
Real-life logic:
IF it’s raining THEN take umbrella
IF battery < 20% THEN charge phone
IF password correct THEN allow access

"""
# Basic if statement
age = 18

if age >= 18:
    print("you can vote")
    print("You are an adult")

# if-else statements

temperature = 25

if temperature > 30:
    print("It is hot!")
else:
    print("Nice weather!")

max_speed = 80

if max_speed > 75:
    print("You are over speed limit")
elif max_speed == 75:
    print("You are respecting speed limit")
else:
    print("you are below speed limit")

# if-elif-else chains   
score = 85

if score >= 90:
    print(" A - Excellent!")
elif score >= 80:
    print(" B - Good job!")
elif score >= 70:
    print(" C - keep it up!")
else:
    print(" You need improvement!")

# Multiple conditions
# Combine conditions with and, or, not:

age = 27
has_license = True
# Both must be true
if age >= 18 and has_license:
    print(" You can drive! ")

# At least one must be true
weekend = True   # define so if can be printed
holiday = True   # define so if can be printed
if weekend or holiday:
   print("No work today")

# Reverse the condition
raining = False
if not raining:
    print("Let go outside!")   

# Nested if statements
# Put if statements inside other if statements:
has_ticket = True
age = 16

if has_ticket:
    if age >= 18:
        print("Enjoy the movie!")
    else:
        print("Need adult supervision")
else:
        print("Buy a ticket first")

# LOOPS
"""
Loops let you repeat code without writing it multiple times. 
Instead of copying and pasting, you tell Python to repeat the code for you.
""" 
# Without loops:
print("Hello World!") 
print("Hello World!") 
print("Hello World!") 
print("Hello World!") 
print("Hello World!")  

# With loops:
for i in range (5):
    print("Hello World!")

# For Loops
"""
The for loop is the most common loop in Python. 
Let’s start simple:
"""
# Repeat a specific number of times 
# Print numbers o through 4
for i in range (5):
    print(i)

# Count from different starting points
# Count from 1 to 5
for i in range (1,6):
    print(i)  

# Count by 2s
for i in range (0, 10, 2):
    print(i) 

# Loop through text
# You can loop through each character in a string:
name = "Python" 
for letter in name:
    print(letter)
"""
Output:
P
y
t
h
o
n
"""        

# Loop through a list (previous)
colors = ["red", "blue", "green"]
for color in colors:
    print(color) 
"""
output:
red
blue
green
""" 
# While loops
# A while loop continues as long as a condition is true:

count = 0
while count < 5:
    print(f"Count is {count}") 
    count = count + 1 # increase count by 1