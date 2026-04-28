"""
Sudan Climate Data Analysis
Task 2: Data Profiling, Cleaning & EDA
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

print("=" * 60)
print("SUDAN CLIMATE DATA ANALYSIS")
print("=" * 60)

try:
    df = pd.read_csv("data/sudan.csv")
    print(f"\n1. LOADING DATA...")
    print(f"   Loaded {len(df)} rows, {len(df.columns)} columns")
except FileNotFoundError:
    print("ERROR: data/sudan.csv not found")
    sys.exit(1)

print(f"\n2. CLEANING DATA...")
df = df.replace(-999, np.nan)
df = df.drop_duplicates()
df['DATE'] = pd.to_datetime(df['YEAR'].astype(str) + df['DOY'].astype(str).str.zfill(3), format='%Y%j')
df['MONTH'] = df['DATE'].dt.month
df['COUNTRY'] = 'Sudan'
df.to_csv("data/sudan_clean.csv", index=False)
print(f"   Saved cleaned data to data/sudan_clean.csv")

print(f"\n3. EXTREME EVENT ANALYSIS...")
extreme_heat = df[df['T2M_MAX'] > 35].shape[0]
dry_days = df[df['PRECTOTCORR'] < 1].shape[0]
print(f"   Extreme heat days (>35°C): {extreme_heat}")
print(f"   Dry days (<1mm rain): {dry_days}")

monthly = df.groupby('MONTH')['T2M'].mean().reset_index()

print(f"\n4. GENERATING PLOTS...")
plt.figure(figsize=(12, 5))
plt.bar(monthly['MONTH'], monthly['T2M'], color='coral')
plt.title('Sudan: Monthly Average Temperature (2015-2026)', fontsize=14)
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.xticks(range(1, 13), ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
plt.tight_layout()
plt.savefig('sudan_temperature.png')
print("   Saved: sudan_temperature.png")

print("\n" + "=" * 60)
print("SUDAN ANALYSIS COMPLETE")
print("=" * 60)