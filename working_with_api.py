# WORKING WITH APIs
"""
An API (Application Programming Interface) is like a waiter at a restaurant. 
You tell it what you want, and it brings you the data.
But APIs do more than just fetch information. 
They’re the bridges that connect your code to other systems. With APIs, you can:
Pull customer data from your CRM (Salesforce, HubSpot)
Get order information from Shopify or WooCommerce
Send messages through Slack or email services
Use AI models from OpenAI or Anthropic
In the context of AI, APIs are essential. 
They let you connect AI capabilities to real business data and systems.
"""
# API call
import requests
# We need coordinates to get weather data
latitude = 31.84       # Odessa Texas latitude
longitude = 102.36     # Odessa Texas longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request

response = requests.get(url)
data = response.json()

print(data)


type(data)
data.keys()
data["current"]
temperature =data["current"]["temperature_2m"]

# Understanding the response

{'latitude': 31.875,
 'longitude': 102.375,
 'timezone': 'GMT',
 'elevation': 3910.0,
 'current_units': {'time': 'iso8601',
  'temperature_2m': '°C'
  },
 'current': {
     'time': '2026-01-25T01:45',
     'temperature_2m': 1.3
    }
  
  }

# The temperature is nested inside current, so to get it:
temperature =data["current"]["temperature_2m"]
print(f"Temperature in Odesa Texas: {temperature}°C")
# Output: Temperature in Odesa Texas: 1.3°C

# Extract what you need

import requests

def get_weather(latitude, longityude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m")
    data = response.json()
    return data['current']['temperature_2m']

# Get temperature for different cities
odessa_temp = get_weather(31.87, 102.37)
sherman_temp = get_weather(33.63, 96.60)
new_york_temp = get_weather(40.71, 74.00)
paris_temp = get_weather(48.85, 2.35)
london_temp = get_weather(51.50, -0.12)
tokyo_temp = get_weather(35.68, 139.69)

print(f"Odessa Texas: {odessa_temp}°C")
print(f"Sherman Texas: {sherman_temp}°C")
print(f"New York: {new_york_temp}°C")
print(f"Paris: {paris_temp}°C")
print(f"London: {london_temp}°C")
print(f"Tokyo: {tokyo_temp}°C")