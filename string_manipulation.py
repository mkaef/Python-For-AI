# STRING MANIPULATION

# Working with text
# String operations - Concatenation (joining)

first_name = "Ben"
last_name = "Nzengui"

full_name = first_name + " " + last_name

# Using f-strings (modrern Python way)

greeting = f"Hello {first_name}!"

# Multiple variable

age = 30

intro = f"I am {full_name} I am {age} years old"

# Repetition

star = "*"
stars = star * 15
separator = "-" * 10

# String methods
"""
Python strings come with many built-in methods - functions you can call directly on any string. 
These methods let you transform text, search for patterns, and clean up data. 
The best part? You can often guess what they do from their names - upper() makes text uppercase, 
replace() replaces text, and so on.

"""
# Changing case
text = "Python Programing"

print(text.lower())  # "python programming"
print(text.upper())  # "PYTHON PROGRAMMING"
print(text.title())  # "Python Programming"

# Cleaning Strings

messy = " Hello World "
print(messy.strip())  # "hello world" (removes whitespace)

price = "$20.97"
print(price.split("$")) # "20.97"

# Finding and replacing 

message = "I love Python programming with Python"

# Check if something exists
print("Python" in message)         #True
print(message.startswith("I"))     #True
print(message.endswith("Python"))  #True

# Find position
print(message.find("Python"))      # 7 (first occurrence)
print(message.count("Python"))     # 2 (number of times)

# Replace 
new_message = message.replace("Python", "JavaScript")
print(new_message)  # "I love JavaScript programming with JavaScript"