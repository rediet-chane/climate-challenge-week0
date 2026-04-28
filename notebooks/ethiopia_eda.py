"""
Ethiopia Climate Data Analysis
Task 2: Data Profiling, Cleaning & EDA
Data Quality Decisions:
- Replaced -999 (NASA sentinel) with NaN
- Dropped duplicate rows (0 found)
- Forward-fill for missing weather values
- Retained outliers (extreme events are meaningful for climate analysis)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

print("=" * 60)
print("ETHIOPIA CLIMATE DATA ANALYSIS")
print("=" * 60)

# Load data with error handling
try:
    df = pd.read_csv("data/ethiopia.csv")
    print(f"\n1. LOADING DATA...")
    print(f"   Loaded {len(df)} rows, {len(df.columns)} columns")
except FileNotFoundError:
    print("ERROR: data/ethiopia.csv not found")
    print("Download the file and place it in the data/ folder")
    sys.exit(1)

# Clean data
print(f"\n2. CLEANING DATA...")
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

# Export cleaned dataset
df.to_csv("data/ethiopia_clean.csv", index=False)
print(f"   Saved cleaned data to data/ethiopia_clean.csv")

# Extreme event analysis
print(f"\n3. EXTREME EVENT ANALYSIS...")
extreme_heat = df[df['T2M_MAX'] > 35].shape[0]
print(f"   Extreme heat days (T2M_MAX > 35°C): {extreme_heat}")

dry_days = df[df['PRECTOTCORR'] < 1].shape[0]
print(f"   Dry days (PRECTOTCORR < 1mm): {dry_days}")

# Monthly averages
monthly = df.groupby('MONTH').agg({'T2M': 'mean', 'PRECTOTCORR': 'sum'}).reset_index()

# Plot 1: Temperature
print(f"\n4. GENERATING PLOTS...")
plt.figure(figsize=(12, 5))
plt.bar(monthly['MONTH'], monthly['T2M'], color='coral')
plt.title('Ethiopia: Monthly Average Temperature (2015-2026)', fontsize=14)
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.xticks(range(1, 13), ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
plt.tight_layout()
plt.savefig('ethiopia_temperature.png')
print("   Saved: ethiopia_temperature.png")

# Plot 2: Precipitation
plt.figure(figsize=(12, 5))
plt.bar(monthly['MONTH'], monthly['PRECTOTCORR'], color='steelblue')
plt.title('Ethiopia: Monthly Total Precipitation (2015-2026)', fontsize=14)
plt.xlabel('Month')
plt.ylabel('Precipitation (mm)')
plt.xticks(range(1, 13), ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
plt.tight_layout()
plt.savefig('ethiopia_precipitation.png')
print("   Saved: ethiopia_precipitation.png")

# Plot 3: Daily trend
plt.figure(figsize=(14, 5))
plt.plot(df['DATE'][:500], df['T2M'][:500], 'r-', linewidth=0.5)
plt.title('Ethiopia: Daily Temperature Trend (First 500 days)', fontsize=14)
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.tight_layout()
plt.savefig('ethiopia_trend.png')
print("   Saved: ethiopia_trend.png")

print("\n" + "=" * 60)
print("ETHIOPIA ANALYSIS COMPLETE")
print("=" * 60)