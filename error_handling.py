# TYPES OF ERRORS
# Syntax errors happen when Python can't undurstand your code:

# Missing colon
if x > 5  # SyntaxError
    print("Big number")

# Runtime errors happen when your code runs:
 # Division by zero
result = 10 / 0  # ZeroDivisionError

# Variable doesn't exist
print(score)  # NameError

# Wrong type
"hello" + 5  # TypeError  

# This will crash if the file doesn't exist
with open('data.txt', 'r') as f:
    content = f.read()
print("Done!")  # Never reaches here if file missing

# This keeps running even if file doesn't exist
try:
    with open('data.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("Could not find data.txt")
    content = "default data"
print("Done!")  # Always reaches here