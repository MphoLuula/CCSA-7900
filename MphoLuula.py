# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 21:46:02 2024

@author: Mpho
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the CSV file into a dataframe
df = pd.read_csv('C:/Users/Mpho/Downloads/CCSA 7900 Coding/FAOSTAT_data.csv')

# Extract the oranges data to a new dataframe
oranges_df = df[df['Item'] == 'Oranges']

# Extract the "Area harvested" and "Yield" columns to a new dataframe
oranges_harvest_yield_df = oranges_df[['Year', 'Area harvested', 'Yield']]

# Convert the filtered data to a NumPy array
oranges_harvest_yield_array = oranges_harvest_yield_df.to_numpy()

# Identify the years with the maximum and minimum yield
max_yield_year = oranges_harvest_yield_array[np.argmax(oranges_harvest_yield_array[:, 2])]
min_yield_year = oranges_harvest_yield_array[np.argmin(oranges_harvest_yield_array[:, 2])]

print("Max yield year:", max_yield_year)
print("Min yield year:", min_yield_year)

# Calculate the annual deviations (anomalies) for "Yield"
yield_anomalies = oranges_harvest_yield_array[:, 2] - np.mean(oranges_harvest_yield_array[:, 2])

# Save the yield anomalies to a new CSV file
np.savetxt('oranges_yield_anomalies.csv', yield_anomalies)

# Plot a time series of the area harvested
plt.plot(oranges_harvest_yield_array[:, 0], oranges_harvest_yield_array[:, 1])
plt.xlabel('Year')
plt.ylabel('Area harvested')
plt.title('Oranges Area Harvested')
plt.show()

# Plot a time series of yield anomalies
plt.plot(oranges_harvest_yield_array[:, 0], yield_anomalies)
plt.xlabel('Year')
plt.ylabel('Yield anomalies')
plt.title('Oranges Yield Anomalies')
plt.show()
