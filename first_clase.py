# HOW CLASES WORK
"""
Working with classes follows a simple pattern:
Define the class - Create a blueprint with the class keyword
Add an __init__ method - Set up initial data when objects are created
Create instances - Make actual objects from your class
Access the data - Use the attributes you defined
Let’s go through each step to build your first class.
"""
# Basic class structure
# Every class starts with the class keyword:

class Dog:  # Note: class names use PascalCase
    pass  # Empty class

# Adding an initializer
# The __init__ method runs when you create a new object:

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

# Create dog objects - using positional arguments
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Beagle")

# Or with named arguments (clearer)
dog3 = Dog(name="Charlie", breed="Poodle")

print(dog1.name)   # Buddy
print(dog2.breed)  # Beagle
print(dog3.name, dog3.breed)  # Charlie Poodle

# Understanding self
# self refers to the current object. It’s how an object keeps track of its own data:

class Dog:
    def __init__(self, name):
        self.name = name  # self.name belongs to this specific dog

# Using positional argument
dog1 = Dog("Buddy")

# Using named argument (same result)
dog2 = Dog(name="Max")

# Each dog has its own name
print(dog1.name)  # Buddy
print(dog2.name)  # Max

# Real-world example: configuration
# Here’s a practical class for AI engineering:

class APIConfig:
    def __init__(self, api_key, model="gpt-3.5-turbo", max_tokens=100):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.base_url = "https://api.openai.com/v1"

# Create different configurations
# Using positional for required arg, named for optional
dev_config = APIConfig("sk-dev-key", max_tokens=50)

# Using all named arguments (clearest)
prod_config = APIConfig(api_key="sk-prod-key", model="gpt-4", max_tokens=1000)

# Access the configuration
print(dev_config.model)        # gpt-3.5-turbo
print(prod_config.model)       # gpt-4
print(prod_config.max_tokens)  # 1000

# Class vs instance
"""
Class: The blueprint (like a recipe)
Instance/Object: What you create from the class (like a cake from the recipe)
"""
# APIConfig is the class
# config1 and config2 are instances
config1 = APIConfig(api_key="key1", max_tokens=50)
config2 = APIConfig(api_key="key2", max_tokens=200)

# Each instance has its own data
print(config1.max_tokens)  # 50
print(config2.max_tokens)  # 200

# Changing one doesn't affect the other
config1.max_tokens = 75
print(config1.max_tokens)  # 75
print(config2.max_tokens)  # 200 (unchanged)