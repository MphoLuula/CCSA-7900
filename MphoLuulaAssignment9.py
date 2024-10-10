# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 21:37:43 2024

@author: Mpho
"""

# -*- coding: utf-8 -*-
"""
Exploration of netCDF file: Precipitation Flux
"""
import os
import netCDF4 as nc
import xarray as xr

# Define the directory and file name explicitly
directory = r"C:\Users\Mpho\Downloads\CCSA 7900 Coding\Data" 
file_name = "C:/Users/Mpho/Downloads/CCSA 7900 Coding/Data/Precipitation-Flux_C3S-glob-agric_AgERA5_20240130_final-v1.1.area-subset.-20.15.-35.35.nc"
file_path = os.path.join(directory, file_name)

# Check if the file exists
if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
else:
    try:
        print("----------------------------------------------------------------")
        # Option 1: using netCDF4
        # Open the netCDF file
        with nc.Dataset(file_path, 'r') as datasetA:
             # Print dataset information
             print(f"Dataset information:\n{datasetA}")
             print("----------------------------------------------------------------")
             # Print dimensions only
             print("Dimensions:")
             for name, dim in datasetA.dimensions.items():
                 print(f"{name}: {dim.size}")
             print("----------------------------------------------------------------")
             # Print variables, type & dimensions
             print("Variables:")
             for name, var in datasetA.variables.items():
                 print(f"{name}: {var.datatype}, dimensions: {var.dimensions}, shape: {var.shape}")
                 # Print min and max values for numeric variables
                 # With netCDF4 you need to explicitly load the data using array slicing
                 # Loading large datasets can be inefficient and might cause memory issues
                 
        print("\n===============================================================")
    
        # Option 2: using xarray
        # Open the netCDF file
        datasetB = xr.open_dataset(file_path)
        # Print dataset information
        print(f"\nDataset information:\n{datasetB}")
        print("----------------------------------------------------------------")
        # Print dimensions only
        print("Dimensions:")
        for name, size in datasetB.dims.items():
            print(f"{name}: {size}")
        print("----------------------------------------------------------------")
        # Print variables, type & dimensions
        print("Variables:")
        for name, var in datasetB.variables.items():
            print(f"{name}: {var.dtype}, dimensions: {var.dims}, shape: {var.shape}")
            # Print min and max values for numeric variables
            if var.dtype.kind in 'fi':  # Check if the variable is float or integer
                print(f"  - Min: {var.min().values}, Max: {var.max().values}")
        print("----------------------------------------------------------------")
        # Print coordinates only
        print("Coordinates:", datasetB.coords)
        print("----------------------------------------------------------------")
        # Print attributes only
        print("Attributes:", datasetB.attrs)
        print("----------------------------------------------------------------")
        # Note: xarray uses lazy loading. To load the data into memory, call .load() on the dataset or specific variables

    except OSError as e:
        print(f"Error opening file: {e}")
       

import os
import xarray as xr

# Define the directory and file name explicitly
directory = r"C:\Users\Mpho\Downloads\CCSA 7900 Coding\Data" 
file_name = "C:/Users/Mpho/Downloads/CCSA 7900 Coding/Data/Precipitation-Flux_C3S-glob-agric_AgERA5_20240130_final-v1.1.area-subset.-20.15.-35.35.nc"
file_path = os.path.join(directory, file_name)

# Check if the file exists
if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
else:
    try:
        print("----------------------------------------------------------------")
        # Open the netCDF file
        dataset = xr.open_dataset(file_path)
        
        # Example 1: Extract the entire precipitation flux dataset
        pflux_data = dataset['Precipitation_Flux']  # Use the variable name from the dataset
        # Print basic information about the data
        print(f"Precipitation Data Shape: {pflux_data.shape}")
        print(f"Precipitation Data:\n{pflux_data}")
        print("----------------------------------------------------------------")
        # Example 2: Extract precipitation flux data for a specific time step (only 1 available in this case)
      #  pflux_at_time = pflux_data.sel(time='2024-01-01')
        # Print shape and data
       # print(f"Precipitation at 2024-01-01:\n{pflux_at_time}")
       # print("----------------------------------------------------------------")
        # Example 3: Extract temperature data for a specific location (e.g. lat = -29.11, lon = 26.19)
        pflux_at_location = pflux_data.sel(lat=-29.11, lon=26.19, method='nearest')
        actual_lat = pflux_at_location['lat'].values
        actual_lon = pflux_at_location['lon'].values
        # Print the temperature at specified location
        print(f"Precipitation at lat={actual_lat}, lon={actual_lon}:\n{pflux_at_location.values}")
        print("----------------------------------------------------------------")
        # Example 4: Extract temperature data for a specific region (e.g. Lesotho)
        pflux_region = pflux_data.sel(lat=slice(-28.57, -30.68), lon=slice(27.01, 29.45))
        # Print the extracted regional data
        print(f"Precipitation data for the region lat=-28.57 to -30.68 and lon=27.01 to 29.45:\n{pflux_region}")
    
    except OSError as e:
        print(f"Error opening file: {e}")


import xarray as xr
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define the file pattern with raw string notation
file_pattern = r"C:\Users\Mpho\Downloads\CCSA 7900 Coding\Data\Precipitation-Flux_C3S-glob-agric_AgERA5_{date}_final-v1.1.area-subset.-20.15.-35.35.nc"

# List to store precipitation flux data
precipitation_data = []

# Define start and end dates
start_date = datetime.datetime(2024, 1, 1)
end_date = datetime.datetime(2024, 12, 31)  

# Loop through each date in the range
current_date = start_date
while current_date <= end_date:
    date_str = current_date.strftime("%Y%m%d")
    file_path = file_pattern.format(date=date_str)
    
    try:
        with xr.open_dataset(file_path) as ds:
            precip_flux = ds["precipitation_flux"].values
            precipitation_data.append(precip_flux)
    except FileNotFoundError:
        print(f"File not found for date {date_str}. Skipping...")
    
    current_date += datetime.timedelta(days=1)

# Convert precipitation_data list to a NumPy array
precipitation_data_array = np.array(precipitation_data)

# Create time coordinate
times = pd.date_range(start=start_date, end=end_date, freq="D")

# Create DataArray with time, lat, lon dimensions
precip_data_da = xr.DataArray(
    precipitation_data_array, 
    dims=["time", "lat", "lon"], 
    coords={"time": times}
)

# Aggregate to monthly statistics
precip_monthly_total = precip_data_da.resample(time="M").sum()
precip_monthly_mean = precip_data_da.resample(time="M").mean()
precip_monthly_min = precip_data_da.resample(time="M").min()
precip_monthly_max = precip_data_da.resample(time="M").max()

# Store in Dataset
monthly_stats = xr.Dataset({
    "monthly_total": precip_monthly_total,
    "monthly_mean": precip_monthly_mean,
    "monthly_min": precip_monthly_min,
    "monthly_max": precip_monthly_max
})

# Save to NetCDF file
monthly_stats.to_netcdf("monthly_precipitation_statistics.nc")

# Plotting
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
precip_monthly_total.mean(dim="time").plot(ax=axs[0, 0], cmap="Blues")
axs[0, 0].set_title("Monthly Total Precipitation (Mean)")

precip_monthly_mean.mean(dim="time").plot(ax=axs[0, 1], cmap="Purples")
axs[0, 1].set_title("Monthly Mean Precipitation (Mean)")

precip_monthly_min.min(dim="time").plot(ax=axs[1, 0], cmap="Greens")
axs[1, 0].set_title("Monthly Minimum Precipitation")

precip_monthly_max.max(dim="time").plot(ax=axs[1, 1], cmap="Reds")
axs[1, 1].set_title("Monthly Maximum Precipitation")

plt.tight_layout()
plt.show()
