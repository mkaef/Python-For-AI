# TUPLES
"""
Tuples are like lists, but they can’t be changed once created. They’re immutable (unchangeable) sequences.
Use tuples for data that shouldn’t change:
Coordinates (x, y)
RGB colors (255, 0, 0)
Database records
Function return values
"""
# Creating tuples
empty_tuples = ()

# Tuple with items
point = (5, 7)
colors = ("red", "green", "bleu")

# Single item tuple needs comma!
single = (53,)         # Note the comma
not_tuple = (53)       # This is just 42 in parentheses

# Without parentheses (implicit)
coordinates = 30, 50

# Accessing items
point = (5, 7)
colors = ("red", "green", "bleu")

print(point[0])
print(colors[-1])

# Slicing 
print(colors[0:2])
print(colors[2:])

# Tuple unpacking
# Unpack values
point = (5, 7)
x, y = point  # x = 5, y = 7

# Multiple assigment
a, b, c = 1, 2, 3  # Same as (1, 2, 3)

# Swap variables elegantly
x, y = y, x  # Swaps values!