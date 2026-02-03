# FUNCTIONS
"""
Functions are reusable blocks of code that do specific tasks. 
Instead of writing the same code multiple times, 
you write it once as a function and call it whenever needed.
Think of functions like:
A recipe you can follow multiple times
A machine that takes input and produces output
A named shortcut for complex operations
"""
# Definition
"""
A function is a named block of code that performs a specific task. 
You define it once, then call it whenever you need that task done.
"""
def greet():
    print("Hello World!")
    print("Welcome Home!")

# Call the function
greet()  #Hello World!
         #Welcome Home!

# Function syntax
def function_name():
    # Code goes here
    # Must be indented
    pass 

# Naming functions

# Good names
def calculate_total():
    pass

def send_email():
    pass

def validate_password():
    pass

# Bad names
def func1():  # Not descriptive
    pass

def Calculate():  # Should be lowercase
    pass

# Functions with logic
def check_weather():
    temperature = 25
    if temperature > 30:
        print("It is hot!")
    else:
        print("Nice weather!")  
# Use the function
check_weather()   # Nice weather!

# Variable scope: Local vs Global
""" Variables in Python have a “scope” - 
where they can be accessed and used.
"""
# Local variable
# Variables created inside a function only exist within that function:

def calculate_price():
    price = 100
    tax = price * 0.0825
    print(f"Total: {price + tax}")

calculate_price()  # Total: 108.25

# This fails - price doesn't exist outside the function
print(price)  # NameError: name 'price' is not defined

# Global variables
# Variables created outside functions can be accessed anywhere:
discount_rate = 0.15 # Global variable

def apply_discount(price):
    discount = price * discount_rate # Can read global variable
    return price - discount
result = apply_discount(100)
print(result) # 85.0

# Without using return
discount_rate = 0.15 

def apply_discount():
    price = 100
    discount = price * discount_rate # Can read global variable
    print(f"discount_price: {price - discount}")
    apply_discount()

# Modifying global variables
# To change a global variable inside a function, use the global keyword:

counter = 0 # Global variable

def increment():
    global counter  # Declare we want to modify the global variable
    counter += 1

increment() 
increment()
increment() 
print(counter)  # 3

# Best practice: Use parameters and returns
# Bad - using global variable
total = 0

def add_to_total(amount):
    global total
    total += amount

# Good - using parameters and return
def add_amounts(current_total, amount):
    return current_total + amount

total = 0
total = add_amounts(total, 50)   
total = add_amounts(total, 60) 
print(total)   # 110
