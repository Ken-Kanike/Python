import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create some sample data
dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
temperature = np.random.normal(loc=25, scale=5, size=len(dates))
humidity = np.random.normal(loc=60, scale=10, size=len(dates))

# Create a DataFrame
df = pd.DataFrame({'date': dates, 'temperature': temperature, 'humidity': humidity})

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# Line plot
ax1.plot(df['date'], df['temperature'], label='Temperature')
ax1.set_title('Daily Temperature Over a Year')
ax1.set_xlabel('Date')
ax1.set_ylabel('Temperature (°C)')
ax1.legend()

# Scatter plot
ax2.scatter(df['temperature'], df['humidity'], alpha=0.5)
ax2.set_title('Temperature vs Humidity')
ax2.set_xlabel('Temperature (°C)')
ax2.set_ylabel('Humidity (%)')

# Adjust layout and display the plot
plt.tight_layout()
plt.show()

# Save the figure
plt.savefig('weather_plots.png')