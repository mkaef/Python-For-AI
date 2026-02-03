# LISTS
# Works with ordered collections
"""
Lists are Python’s most versatile data structure. 
They’re like containers that can hold multiple items in a specific order.
Think of a list like:
A shopping list (milk, eggs, bread)
A to-do list (tasks in order)
A playlist (songs in sequence)
"""
# Creating lists
# Empty list
empty_list = []

# List with items
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 23, True, 2.14]

# Accessing items
# Lists are indexed sterting at 0:

fruits = ["apple", "banana", "orange"]
print(fruits[0])
print(fruits[1])
print(fruits[2])
"""
output:
apple
banana
orange
"""
# Slicing
print(fruits[0:2]) # ['apple', 'banana']
print(fruits[1:])  # ['banana', 'orange']

# Changing lits
# Lists are mutable - you can change them:

fruits = ["apple", "banana", "orange"]
# Cange an item
fruits[0] = "mango"
print(fruits) # ['mango', 'banana', 'orange']

# Add items
fruits.append("grape") # Add to the ends
print(fruits)  # ['mango', 'banana', 'orange', 'grape']
fruits.insert(2, "tomato") # Insert at position
print(fruits)  # ['mango', 'banana', 'tomato', 'orange', 'grape']

# Remove items
fruits.remove("mango") # Remove by value
print(fruits)
last = fruits.pop() # Remove and return last
print(fruits)

del fruits[0] # Remove by index
print(fruits)

# List methods

numbers = [3, 1, 4, 1, 5, 9]

# Information
print(len(numbers))      # 6 (length)
print(numbers.count(1))  # 2 (count occurrences)
print(numbers.index(5))  # 4 (find position)

# Sorting
numbers.sort()           # Sort in place
print(numbers)           # [1, 1, 3, 4, 5, 9]

numbers.reverse()        # Reverse order
print(numbers)           # [9, 5, 4, 3, 1, 1]

# Copy

new_list = numbers.copy() # Create a copy
print(new_list)           # [9, 5, 4, 3, 1, 1]

# Checking lists
fruits = ["apple", "banana", "orange"]

# check if item exist
if "apple" in fruits:
    print("Apple exist!")

# check if list empty
if fruits:
   print("List has items")
else:
    print("List is empty")    

