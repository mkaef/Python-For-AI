# PARAMETERS
"""
Parameters let you pass data into functions. 
Instead of hardcoding values, you make functions flexible 
to work with different inputs.
"""
# Without parameters (inflexible)
def greet_andrew():
    print("Hello, Andrew!")

# With parameters (flexible)
def greet(name):
    print(f"Hello, {name}!")

greet("Andrew!") 
greet("Adea!")
greet("Tica!")

# Basic parameters
# Add parameters inside the parentheses when defining a function:

def introduce(name, age):
    print(f"My name is {name}")
    print(f"I am {age} years old")

introduce("Andrew", 25)  # My name is Andrew
                         #I am 25 years old


introduce("Tica", 32)  # My name is Tica
                       #I am 32 years old

# Multiple parameters

def calculate_total(price, tax_rate, discount):
    tax = price * tax_rate
    final_price = price + tax - discount
    print(f"Total: ${final_price}")  

# Order matter
calculate_total(100, 0.025, 10)   # Total: $92.5

# Default values
# Give parameters default values for optional arguments

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Use default
    greet("Andrew")  # Hello, Andrew!
    greet("Tica")    # Hello, Tica!

# Override defaultss
greet("Tim", "Hi")   # Hi, Tim!
greet("Adea", "Hi")  # Hi, Adea!

# Keyword arguments
# Call functions using parameter names for clarity:

def create_profile(name, age, city):
    print(f"{name}, {age}, {city}")

# Positional arguments (order matters)
create_profile("Andrew", 25,"Odessa")   

# Keyword arguments (order doesn't matter)
create_profile(city="lubbock", name="Tica", age=32) # Tica, 32, lubbock