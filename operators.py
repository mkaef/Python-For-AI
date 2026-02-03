# OPERATORS
"""
Operators are symbols that perform operations on values. 
Think of them as the “verbs” of programming - they make things happen!
You already know most operators from math class:
Calculate: +, -, *, /
Compare: >, <, ==
Combine: and, or, not

"""
# Special operators
print(10 // 3)  # 3  - Floor division (rounds down)
print(10 % 3)   # 1  - Modulo (remainder)
print(10 ** 3)  # 1000 - Exponent (power)

# Order of operations
result = 6 + 3 * 4      # 18 (not 20!)
result = (6 + 3) * 4    # 36 (parentheses first)

# Comparison operators
# These compare values and return True or False:

age = 18

print(age == 18)    # True  - Equal toThese compare values and return True or False:
print(age != 21)    # True  - Not equal to
print(age > 17)     # True  - Greater than
print(age < 20)     # True  - Less than
print(age >= 18)    # True  - Greater than or equal
print(age <= 18)    # True  - Less than or equal

# Logicaal operators
# These combine boolean values and conditions:
age = 27
has_licence = True
# AND - both must be true
can_drive = age >= 16 and has_licence

# OR - at least one must be true
day = "Saturday" 
is_weekend = day == "Saturday" or day = "Sunday"
print(is_weekend)

# NOT - reverses the value
is_adult = age >= 18
is_child = not is_adult
print(is_child)

# Truth tables 
# Understanding how and, or , and not work:

# AND: Both must be True
print(True and True)    # True
print(True and False)   # False
print(False and False)  # False

# OR: At least one must be True  
print(True or False)    # True
print(False or False)   # False

# NOT: Flips the value
print(not True)         # False
print(not False)        # True

# Assigment shortcuts
# These shortcuts update variables in place:

# Instead of:
score = 8
score = score + 10
#Write:
score += 10

# Works with all operators
x = 10
x += 5
x *= 2
