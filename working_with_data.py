# WORKING WITH DATA
"""
Building on APIs
Let’s take the weather API from the previous page and create something useful. 
We’ll get weather data for the past 7 days, analyze it, visualize it, and save it.
This brings together everything you’ve learned: 
APIs, data processing, file handling, and visualization.
"""

# Get 7 days of weather
import requests
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os

# Calculate dates
today = datetime.now()
week_ago = today - timedelta(days=7)

# Format dates for API (YYYY-MM-DD)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

#Get Odessa Texas weather for past week
url = f"https://api.open-meteo.com/v1/forecast?latitude=31.84&longitude=102.36&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"
response = requests.get(url)
data = response.json()
print(data)

# Load into pandas
# Extract the daily data
 
daily_data = data['daily']

# Create a DataFrame
df = pd.DataFrame({
    'date': daily_data['time'],
    'max_temp': daily_data['temperature_2m_max'],
    'min_temp': daily_data['temperature_2m_min']
})

# Convert date strings to datetime
df['date'] = pd.to_datetime(df['date'])

print(df)
"""
Output:

date  max_temp  min_temp
0  2026-01-18       9.6      -3.3
1  2026-01-19       9.0      -5.8
2  2026-01-20       8.8      -6.5
3  2026-01-21       9.3      -8.6
4  2026-01-22       6.1      -9.5
5  2026-01-23       8.7      -7.1
6  2026-01-24      11.9      -3.5
7  2026-01-25      10.2      -6.8
"""

# Visualize the data

# Create the plot 
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Odessa Texas Weather - Past 7 Days')
plt.legend()

# Rotate x-axis labels for readability
plt.xticks(rotation=45)
plt.tight_layout()

# save the plot
plt.savefig('weather_chart.png')
plt.show()

# Save to CSV

# Create data folder if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Save to CSV
df.to_csv('data/odessa_texas_weather.csv', index=False) 
print("Data saved to data/odessa_texas_weather.csv")   