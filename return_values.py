# RETURN VALUES
"""
So far, our functions have printed output. 
But often you want functions to calculate something 
and give you the result to use elsewhere.
"""

#  This function only prints
def add_print(a, b):
    print(a+b) 

# This function return a value
def add_return(a, b):
    return a + b  

# Now you can use the result 
result = add_return(7, 3)
print(f"The result is {result}") # The result is 10

# The return statement
# Use return to send a value back from a function
def calculated_area(width, height):
    area = width * height
    return area

# Store the returned value

room_area = calculated_area(5, 15)
print(f"Room size: {room_area} sq ft")  # Room size: 75 sq ft

# Using returned values
# Returned values can be used in many ways:

def double(number):
    return number * 2

# Store in variable
result = double(5)

# Use in expressions
total = double(5) + double(4)
print(total)       # 18

# Pass to other functions
print(double(20))  # 40

# Use in condition
if double(6) > 10:
    print("Big number!")

# Returning multiple values 
def get_min_max(numbers):
    return min(numbers), max(numbers) 

# Get both values
minimum, maximum = get_min_max([3, 7, 5, 2, 9, 12]) 
print(f"Min: {minimum}, Max: {maximum}")  # Min: 2, Max: 12

# Or as a tuple
result = get_min_max([3, 7, 5, 2, 9, 12])
print(result)   # (2, 12)

# Return vs print
# Understanding the difference is crucial

def get_greeting_print(name):
    print(f"Hello {name}!")  # Just displays

def get_greeting_return(name):
    return f"Hello {name}!"   # Give back value

# Can't use print version's output
message = get_greeting_print("Andrew") # Prints but returns None
print(message)  # none

# Can use return version's output
message = get_greeting_return("Tica")  # Returns the string
print(message.upper()) # hello Tica!

# Functions without return
# Functions without explicit return statements return None:

def greet(name):
    print(f"Hello {name}!")
    # No return statment

result = greet("Adea")   # Prints: Hello, Adea
print(result)  # None