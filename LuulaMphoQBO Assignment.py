# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 19:42:56 2024

@author: Mpho
"""

import numpy as np
import matplotlib.pyplot as plt
import json

# Step 1: Read the data from the file
file_path = r'C:\Users\Mpho\Downloads\CCSA 7900 Coding\QBO script.txt'

# Initialize lists
monthly_values = []
years = []

# Read the file and parse the data
with open(file_path, 'r') as file:
    for line in file:
        if line.strip() and not line.startswith('#'):  # Skip header and empty lines
            values = line.split()
            year = int(values[0])
            indices = [float(x) for x in values[1:] if float(x) != -999.90]  # Ignore missing values (-999.90)
            
            if len(indices) == 12:
                monthly_values.append(indices)
                years.append(year)

monthly_values = np.array(monthly_values)

# Step 2: Calculate the Average Index Value for Each Month
monthly_mean = np.mean(monthly_values, axis=0)

# Step 3: Calculate the Standard Deviation of the Index Value for Each Month
monthly_std = np.std(monthly_values, axis=0)

# Step 4: Identify the Years with Maximum and Minimum Index Value for Each Month
max_years = []
min_years = []

for i in range(12):
    max_year = years[np.argmax(monthly_values[:, i])]
    min_year = years[np.argmin(monthly_values[:, i])]
    max_years.append(max_year)
    min_years.append(min_year)

# Step 5: Calculate the Average Index Value for Each Year
yearly_mean = np.mean(monthly_values, axis=1)

# Step 6: Plot the Time Series of the Monthly Index Values
plt.figure(figsize=(10, 6))
for i in range(12):
    plt.plot(years, monthly_values[:, i], label=f'Month {i+1}')
plt.title('Time Series of Monthly Index Values')
plt.xlabel('Year')
plt.ylabel('QBO Index Value')
plt.legend(loc='best')
plt.grid(True)
plt.show()

# Step 7: Plot the Monthly Mean Index Values
plt.figure(figsize=(8, 6))
plt.plot(range(1, 13), monthly_mean, 'o-', label='Monthly Mean')
plt.fill_between(range(1, 13), monthly_mean - monthly_std, monthly_mean + monthly_std, alpha=0.2)
plt.title('Monthly Mean QBO Index Values')
plt.xlabel('Month')
plt.ylabel('QBO Index Value')
plt.grid(True)
plt.show()

# Step 8: Plot the Annual Mean Index Values
plt.figure(figsize=(10, 6))
plt.plot(years, yearly_mean, 'o-', label='Annual Mean')
plt.title('Annual Mean QBO Index Values')
plt.xlabel('Year')
plt.ylabel('QBO Index Value')
plt.grid(True)
plt.show()

# Save the results to a file
output_data = {
    'monthly_mean': monthly_mean.tolist(),
    'monthly_std': monthly_std.tolist(),
    'max_years': max_years,
    'min_years': min_years,
    'yearly_mean': yearly_mean.tolist()
}

output_file = r'C:\Users\Mpho\Downloads\CCSA 7900 Coding\qbo_results.json'
with open(output_file, 'w') as f:
    json.dump(output_data, f, indent=4)

print(f"Results saved to {output_file}")