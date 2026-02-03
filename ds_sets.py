# SETS
"""
Sets are collections that only store unique values. 
They automatically remove duplicates.
Think of sets like:
A bag of unique marbles
Guest list (each person once)
Unique tags or categories
"""
# Creating sets
"""
 You can create sets two ways: with set() 
 or with curly braces {} (but only when it has values).
 """
# Empty set (careful!)
empty_set = set()  # NOT {} - that's a dict!

# Set with values - both ways work
numbers = {1, 2, 3, 4, 5}
fruits = set(["apple", "banana", "orange"])

# From a list (removes duplicates)
scores = [88, 92, 88, 93, 90]
unique_scores = set(scores)  # {88, 90, 92, 93}
print(unique_scores)

# Basics operations 
colors = {"red", "blue"}

# Add items
colors.add("green")
print(colors)     # {'green', 'bleu', 'red'}

# Remove items
colors.remove("blue")  # Error if not found
print(colors)   # {'green', 'red'}
colors.discard("yellow")  # No error if not found

# Check memberships
if "red" in colors:
    print("Red is avalable")

# Remove duplicates
names = ["Tim", "Andrew","Tica","Andrew"]
unique_names = list(set(names))
print(unique_names)     # ['Tim', 'Tica', 'Andrew']

# Fast membership testing
allowed_users = {"Eric", "Raoul", "Bob"}

if "Eric" in allowed_users:
    print("Access granted")
