"""
Ethiopia Climate Data Analysis
Task 2: Data Profiling, Cleaning & EDA
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

print("=" * 60)
print("ETHIOPIA CLIMATE DATA ANALYSIS")
print("=" * 60)

# Check if data file exists
data_path = "data/ethiopia.csv"
if not os.path.exists(data_path):
    print(f"ERROR: Cannot find {data_path}")
    print("Make sure your CSV file is in the 'data' folder")
    exit(1)

# 1. LOAD DATA
print("\n1. LOADING DATA...")
df = pd.read_csv(data_path)
print(f"   Loaded {len(df)} rows, {len(df.columns)} columns")

# 2. CLEAN DATA
print("\n2. CLEANING DATA...")
df = df.replace(-999, np.nan)
print(f"   Replaced -999 with NaN")

duplicates = df.duplicated().sum()
print(f"   Duplicate rows: {duplicates}")
df = df.drop_duplicates()

# Convert dates
df['DATE'] = pd.to_datetime(df['YEAR'].astype(str) + df['DOY'].astype(str).str.zfill(3), format='%Y%j')
df['MONTH'] = df['DATE'].dt.month
df['COUNTRY'] = 'Ethiopia'
print(f"   Date range: {df['DATE'].min()} to {df['DATE'].max()}")

# 3. CREATE MONTHLY AVERAGES
monthly = df.groupby('MONTH').agg({
    'T2M': 'mean',
    'PRECTOTCORR': 'sum'
}).reset_index()

# 4. PLOT 1: Monthly Temperature
print("\n3. GENERATING PLOT 1: Monthly Temperature...")
plt.figure(figsize=(12, 5))
plt.bar(monthly['MONTH'], monthly['T2M'], color='coral')
plt.title('Ethiopia: Monthly Average Temperature (2015-2026)', fontsize=14)
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.xticks(range(1, 13), ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
plt.tight_layout()
plt.savefig('ethiopia_temperature.png')
print("   Saved: ethiopia_temperature.png")

# 5. PLOT 2: Monthly Precipitation
print("\n4. GENERATING PLOT 2: Monthly Precipitation...")
plt.figure(figsize=(12, 5))
plt.bar(monthly['MONTH'], monthly['PRECTOTCORR'], color='steelblue')
plt.title('Ethiopia: Monthly Total Precipitation (2015-2026)', fontsize=14)
plt.xlabel('Month')
plt.ylabel('Precipitation (mm)')
plt.xticks(range(1, 13), ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
plt.tight_layout()
plt.savefig('ethiopia_precipitation.png')
print("   Saved: ethiopia_precipitation.png")

# 6. PLOT 3: Temperature Trend Over Time
print("\n5. GENERATING PLOT 3: Daily Temperature Trend...")
plt.figure(figsize=(14, 5))
plt.plot(df['DATE'][:500], df['T2M'][:500], 'r-', linewidth=0.5)
plt.title('Ethiopia: Daily Temperature Trend (First 500 days)', fontsize=14)
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.tight_layout()
plt.savefig('ethiopia_trend.png')
print("   Saved: ethiopia_trend.png")

print("\n" + "=" * 60)
print("DONE! Check your folder for PNG files.")
print("=" * 60)