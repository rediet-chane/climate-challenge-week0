"""
Complete Climate Analysis for All 5 Countries
Ethiopia, Kenya, Sudan, Tanzania, Nigeria
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

countries = [
    ('ethiopia', 'Ethiopia'),
    ('kenya', 'Kenja'),
    ('sudan', 'Sudan'),
    ('tanzania', 'Tanzania'),
    ('nigeria', 'Nigeria')
]

print("=" * 60)
print("CLIMATE ANALYSIS FOR ALL 5 COUNTRIES")
print("=" * 60)

for file_name, country_name in countries:
    data_path = f"data/{file_name}.csv"
    
    if not os.path.exists(data_path):
        print(f"WARNING: {data_path} not found. Skipping {country_name}.")
        continue
    
    print(f"\nProcessing {country_name}...")
    
    # Load data
    df = pd.read_csv(data_path)
    df = df.replace(-999, np.nan)
    df = df.drop_duplicates()
    
    # Convert dates
    df['DATE'] = pd.to_datetime(df['YEAR'].astype(str) + df['DOY'].astype(str).str.zfill(3), format='%Y%j')
    df['MONTH'] = df['DATE'].dt.month
    
    # Monthly averages
    monthly = df.groupby('MONTH').agg({
        'T2M': 'mean',
        'PRECTOTCORR': 'sum'
    }).reset_index()
    
    # Plot 1: Temperature
    plt.figure(figsize=(10, 4))
    plt.bar(monthly['MONTH'], monthly['T2M'], color='coral')
    plt.title(f'{country_name}: Monthly Average Temperature (2015-2026)', fontsize=12)
    plt.xlabel('Month')
    plt.ylabel('Temperature (°C)')
    plt.xticks(range(1, 13), ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    plt.tight_layout()
    plt.savefig(f'{file_name}_temperature.png')
    plt.close()
    
    # Plot 2: Precipitation
    plt.figure(figsize=(10, 4))
    plt.bar(monthly['MONTH'], monthly['PRECTOTCORR'], color='steelblue')
    plt.title(f'{country_name}: Monthly Total Precipitation (2015-2026)', fontsize=12)
    plt.xlabel('Month')
    plt.ylabel('Precipitation (mm)')
    plt.xticks(range(1, 13), ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    plt.tight_layout()
    plt.savefig(f'{file_name}_precipitation.png')
    plt.close()
    
    print(f"   Created: {file_name}_temperature.png and {file_name}_precipitation.png")

print("\n" + "=" * 60)
print("DONE! All country charts created.")
print("=" * 60)

# Create comparison chart
print("\nCreating comparison chart...")
all_temps = []
all_rain = []

for file_name, country_name in countries:
    data_path = f"data/{file_name}.csv"
    if os.path.exists(data_path):
        df = pd.read_csv(data_path)
        df = df.replace(-999, np.nan)
        all_temps.append({
            'Country': country_name,
            'Mean_Temp': df['T2M'].mean(),
            'Mean_Rain': df['PRECTOTCORR'].mean()
        })

comparison = pd.DataFrame(all_temps)
comparison = comparison.sort_values('Mean_Temp', ascending=False)

# Bar chart of mean temperatures
plt.figure(figsize=(8, 5))
colors = ['red' if c == 'Sudan' else 'steelblue' for c in comparison['Country']]
plt.barh(comparison['Country'], comparison['Mean_Temp'], color=colors)
plt.title('Mean Temperature Comparison (2015-2026)', fontsize=14)
plt.xlabel('Temperature (°C)')
plt.tight_layout()
plt.savefig('temperature_comparison.png')
plt.close()

print("Created: temperature_comparison.png")
print("\nAll files ready!")
df.to_csv("data/ethiopia_clean.csv", index=False)
print("Saved cleaned data to data/ethiopia_clean.csv")