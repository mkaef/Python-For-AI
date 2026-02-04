

# Python for AI Engineers

A beginner-friendly repository covering core Python fundamentals required for anyone aiming to become an AI Engineer, Machine Learning Engineer, or Data Scientist.

This repository focuses on building a strong Python foundation, which is essential before diving into AI, ML, and Deep Learning frameworks.




## Python Installation
1. Go to python.org/downloads
2. Choose your operator system for example Windows and show the latest version 
3. Click the download button to get the installer
4. Save it to your download folder


## Verify installation
Open Terminal and type command:

python --version
## Code Editor
Choose your code editor, for this project I used Visual Studio Code (VS Code) which is the most popular code editor for Python development right now, including popular forks like Cursor and Windsurf.
It’s completely free and gives you everything you need to write professional Python code. No limitations, no trial periods, just a powerful tool that millions of developers use every day.
## Create a project folder
Create a folder called PythonProjects in your computer where you will store all your Python projects. nside your PythonProjects folder, create a new folder called python-for-ai (all lowercase). Create a new file in folder python-for-ai and use the extension .py telling the computer and VS Code what type of file you are working with.
## Packages and pip
Packages are collections of Python code that solve specific problems:

. requests - Download web pages and data

. pandas - Work with spreadsheets and data

. numpy - Fast mathematical operations

. openai - Connect to AI models

. beautifulsoup4 - Extract data from websites
## Python basics
Now you will learn the fundamental building blocks that every Python program uses. 

Think of it like learning a new language:

. First, you learn words (variables and data types)

. Then, you learn how to make sentences (operators and expressions)

. Finally, you learn grammar rules (control flow)

Data types: numbers, strings and booleans

Working with data: operators, string manipulation

Control flow: if statements, loops

Data structures: lists, dictionaries, tuples, sets
## Building with functions
Functions are reusable blocks of code that do specific tasks. Instead of writing the same code multiple times, you write it once as a function and call it whenever needed.

Think of functions like:

. A recipe you can follow multiple times

. A machine that takes input and produces output

. A named shortcut for complex operations

def greet():
    print("Hello, world!")
    
    print("Welcome to Python!")

### Call the function
greet()
## Parameters

Parameters let you pass data into functions. Instead of hardcoding values, you make functions flexible to work with different inputs.

### Without parameters 
def greet_alice():

    print("Hello, Andrew!")

### With parameters 
def greet(name):

    print(f"Hello, {name}!")

### Now it works for anyone
greet("Tica")

greet("Bob")

greet("Adea")
## Getting results from functions
So far, our functions have printed output. But often you want functions to calculate something and give you the result to use elsewhere.
### This function only prints
def add_print(a, b):

    print(a + b)

### This function returns a value
def add_return(a, b):

    return a + b

### Now you can use the result
result = add_return(5, 3)

print(f"The result is {result}")  # The result is 8
## Import packages
Python packages add new functionality to your programs. There are two types:

. Built-in: Come with Python (no installation needed)

. External: Need to install first with pip

### Built-in modules
#### Import entire module
import random

#### Use module functions
number = random.randint(1, 10)

choice = random.choice(["apple", "banana", "orange"])

### External packages need installation
#### Install a package
pip install requests

#### Install specific version
pip install requests==2.28.0

#### Install multiple packages
pip install pandas numpy matplotlib
## Working with APIs
An API (Application Programming Interface) is a way for different software applications to communicate with each other.
An API lets one program request data or services from another program in a structured and predictable way.

Think of an API like a waiter in a restaurant: 

. You (client) ask the waiter for food (request)

. The waiter takes the request to the kitchen (server)

. The kitchen prepares the food

. The waiter brings it back to you (response)

You don’t go into the kitchen — you just use the interface (menu + waiter).

import requests

response = requests.get("https://api.example.com/data")

data = response.json()

print(data)

## Error handling
Error handling is the process of detecting, managing, and responding to errors in a program so it doesn’t crash and behaves in a controlled, predictable way.

### Common Types of Errors

1️⃣ Syntax Errors

Mistakes in writing code (caught before running the program).

print("Hello"

2️⃣ Runtime Errors (Exceptions)

Errors that occur while the program is running:

. Dividing by zero

. Accessing a non-existing file

. Using the wrong data type

x = 10 / 0   # ZeroDivisionError

3️⃣ Logical Errors

The program runs, but gives wrong results due to incorrect logic.

#### Incorrect logic
average = total / (count - 1)

### Try and except
The try block contains code that might fail. The except block runs if an error happens:

try:

    # Code that might cause an error
    risky_operation()
except:

    # Code that runs if there's an error
    print("Something went wrong")
Handle different errors differently:

try:
    
    # Read a number from a file
    with open('number.txt', 'r') as f:
        text = f.read()
    number = int(text)
    result = 100 / number
    print(f"Result: {result}")
except FileNotFoundError:

    print("Could not find number.txt")
except ValueError:

    print("File doesn't contain a valid number")
except ZeroDivisionError:

    print("Cannot divide by zero")
## Classes
### Object-oriented programming.
Object-oriented programming (OOP) is a way to organize code by grouping related data and functions together. Instead of having separate variables and functions scattered around, you bundle them into objects.

Think of it like organizing a toolbox:

. Without OOP: Tools scattered everywhere

. With OOP: Tools organized in labeled compartments

### What is a class?

A class is a blueprint for creating objects. It defines:

Attributes: What data the object stores

Methods: What the object can do

### Without classes - data and functions separate
name = "OpenAI"

model = "gpt-4o-mini"

def generate_response(prompt):

    # Process prompt...
    return response

### With classes - everything bundled together
class OpenAIClient:

    def __init__(self, name, model):
        self.name = name
        self.model = model
    
    def generate_response(self, prompt):
        # Process prompt...
        return response

### Methods and attributes
Attributes are variables that belong to an object. There are two types:
Instance attributes (unique to each object):

class APIClient:

    def __init__(self, api_key, base_url):
        self.api_key = api_key      # Each client has its own key
        self.base_url = base_url    # Each client has its own URL
        self.request_count = 0      # Track requests per client

#### Creating instances with named arguments
client1 = APIClient(api_key="key1", base_url="https://api1.com")
client2 = APIClient(api_key="key2", base_url="https://api2.com")  

### Methods: adding behavior
Methods are functions that belong to a class. They always have self as the first parameter, but you don’t pass it when calling:

class DataValidator:

    def __init__(self):
        self.errors = []
    
    def validate_email(self, email):
        if "@" not in email:
            self.errors.append(f"Invalid email: {email}")
            return False
        return True
    
    def validate_age(self, age):
        if age < 0 or age > 150:
            self.errors.append(f"Invalid age: {age}")
            return False
        return True
    
    def get_errors(self):
        return self.errors

#### Use the validator
validator = DataValidator()

#### Notice: we don't pass self, just the email
validator.validate_email(email="bad-email")
validator.validate_age(age=200)

#### Or using positional arguments
validator.validate_email("another-bad-email")
validator.validate_age(150)

print(validator.get_errors())
#### ['Invalid email: bad-email', 'Invalid age: 200', 'Invalid email: another-bad-email']

## Inheritance
Inheritance lets you create new classes based on existing ones. The new class (child) gets everything from the parent class, plus can add its own stuff.

Think of it like this:

All dogs are animals (dogs inherit from animals)
Dogs have everything animals have, plus dog-specific things

### Basic inheritance example
#### Parent class - general animal
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        return f"{self.name} is eating"
    
    def sleep(self):
        return f"{self.name} is sleeping"

#### Child class - specific animal
class Dog(Animal):
    def bark(self):
        return f"{self.name} says woof!"

#### Create a dog - using positional argument
my_dog = Dog("Buddy")
#### Or with named argument
my_dog2 = Dog(name="Max")

#### Dog can do animal things (inherited)
print(my_dog.eat())    # Buddy is eating
print(my_dog.sleep())  # Buddy is sleeping

#### Dog can also do dog things
print(my_dog.bark())   # Buddy says woof!

### Adding attributes in child classes
Child classes can have their own attributes too:

class Animal:

    def __init__(self, name):
        self.name = name
        self.is_pet = True

class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)  # Pass name to parent's __init__
        self.breed = breed      # Dog-specific attribute
    
    def describe(self):
        return f"{self.name} is a {self.breed}"

#### Create dogs with breeds - positional arguments
golden = Dog("Buddy", "Golden Retriever")

#### Or with named arguments (clearer)
poodle = Dog(name="Max", breed="Poodle")

print(golden.describe())  # Buddy is a Golden Retriever
print(golden.is_pet)      # True (inherited from Animal)

### Overriding methods
Child classes can change how parent methods work:

class Animal:

    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        return f"{self.name} makes a sound"

class Dog(Animal):

    def make_sound(self):  # Override parent method
        return f"{self.name} barks: Woof!"

class Cat(Animal):

    def make_sound(self):  # Override parent method
        return f"{self.name} meows: Meow!"

#### Different animals, different sounds

generic = Animal(name="Something")

dog = Dog(name="Buddy")

cat = Cat(name="Whiskers")

print(generic.make_sound())  # Something makes a sound

print(dog.make_sound())      # Buddy barks: Woof!

print(cat.make_sound())      # Whiskers meows: Meow!
## Resource
www.python.org › downloads

code.visualstudio.com › download

https://python.datalumina.com/
