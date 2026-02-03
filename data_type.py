"""
Python has two ways to stores numabrs: Integers and Floats
"""
# Intgers whole number without  decimal
age = 25
score = - 10

# Foats - Number with decimal points
price = 20.95
temperature = -6.5
pi = 3.14159

# Basic math operations
total = 10 + 5
change = 10 - 3

# Multiplication and division
area = 3 * 4
half = 12 / 2 # always returns float

# Powers
squared = 6 ** 2
cubed = 7 ** 3

# Regular division (always float)
result = 10 / 3 # 3.3333333333333335

# Integer division (rounds down)
result = 10 // 3 # 3
"""
Note: all those result are displayed using online the variable 
on the interactive window, otherwie use print() to dispay result
on regular terminal
"""

# STRINGS
"""
Strings are text - any characters inside quotes. 
Python doesn’t care if you use single or double quotes, 
just be consistent.
"""

# Single quote
first = 'Python'

# Double quote
second = "Python"

# Triple quotes for multiple lines 

paragraph = """ This is
 a multi- line String
"""

# COMBINING STRINGS
# Joining String together with +:

first_name = "Tim"
last_name = "Luc"
# Concatenation
full_name = first_name + " " + last_name
print(full_name)

# Repitition
stars = "*" * 5
print(stars)

long_dash = "_" * 15
print(full_name)
print(long_dash)

# STRING LENGTH
# Use len() to count characters:

message = "Hello"
print(len(message))

empty = ""
print(len(empty))

# CONVERTING TO STRING
# Turn other types into strings with str():
age = 25
message = " I am " + str(age) + " years old "
print(message)

# Or use f-strings
message = f" I am {age} years old"
print(message)

# BOOLEANS
# Booleans often come from comparisons:
# Direct assignment
is_ready = True

# From comparaison
age = 18
can_vote = age >= 18 # true

score = 75
passed = score > 60  # true

# Comparison operators
# These operators compare values and return True or False:
age = 25
# Equality
print(age == 25)     # True - equals
print(age != 30)     # True - not equals

# Greater/Less than
print(age > 20)      # True - greater than
print(age < 30)      # True - less than
print(age >= 25)     # True - greater or equal
print(age <= 25)     # True - less or equal