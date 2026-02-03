# DICTIONARIES
"""
Dictionaries store data in key-value pairs. Think of them like a real dictionary 
where you look up a word (key) to find its definition (value).
Real-world examples:
Phone book: name > phone number
Menu: dish > price
User profile: username > user info
"""
# Create dictionaries
# Empty dictionary
empty_dict = {}

# Dictionary with data

person = {
    "name" : "Tim",
    "age"  : 27,
    "city" : "Odessa"
}

print(person)

# Different ways to create
scores = dict(math= 98, english= 89, science=95)
print(scores)

# Changing dictionaries
person = {"name" : "Tim","age"  : 27}

#Add or update
person["emal"] = "tim@gmail.com"
person["age"] = 29

print(person) # {'name': 'Tim', 'age': 29, 'emal': 'tim@gmail.com'}

# Remove items
del person["emal"]            # Remove by key 
print(person)                 # {'name': 'Tim'}
age = person.pop("age")       # Remove and return
print(person)                 # {"name" : "Tim"}
person.clear()                # Remove all items
print(person)                 # {}

# Dictionary methods

person = {"name" : "Tim","age"  : 27,"city" : "Odessa"}

# Getting all keys, values or items
print(person.keys())      # dict_keys(['name', 'age', 'city'])
print(person.values())    # dict_values(['Tim', 27, 'Odessa'])
print(person.items()) # dict_items([('name', 'Tim'), ('age', 27), ('city', 'Odessa')])

# Update multiple values
person.update({"age" : 32, "job" : "engineer"})
print(person)

# Nested dictionaries
# Dictionary of dictionaries
students = {
    "Tim": {"age" : 21, "grade" : "A"},
    "Andrew" : {"age" : 18, "grade" : "B"},
    "Tica" : {"age" : 22, "grade" : "A"}
}

# Access nested data
print(students["Tica"]["grade"])  # A