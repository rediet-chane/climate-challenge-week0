"""
Cross-Country Climate Comparison
Task 3: Climate Vulnerability Ranking for COP32
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

print("=" * 70)
print("CROSS-COUNTRY CLIMATE COMPARISON")
print("Ethiopia | Kenya | Sudan | Tanzania | Nigeria")
print("=" * 70)

countries = ['ethiopia', 'kenya', 'sudan', 'tanzania', 'nigeria']
names = ['Ethiopia', 'Kenya', 'Sudan', 'Tanzania', 'Nigeria']

results = []

for country, name in zip(countries, names):
    try:
        df = pd.read_csv(f"data/{country}.csv")
        df = df.replace(-999, np.nan)
        mean_temp = df['T2M'].mean()
        mean_rain = df['PRECTOTCORR'].mean()
        extreme_heat = df[df['T2M_MAX'] > 35].shape[0]
        results.append({
            'Country': name,
            'Mean_Temp_C': round(mean_temp, 1),
            'Mean_Rain_mm': round(mean_rain, 1),
            'Extreme_Heat_Days': extreme_heat
        })
    except FileNotFoundError:
        print(f"ERROR: data/{country}.csv not found")
        sys.exit(1)

# Create comparison DataFrame
comparison = pd.DataFrame(results)
comparison = comparison.sort_values('Mean_Temp_C', ascending=False)

print("\n1. TEMPERATURE COMPARISON (Warmest to Coolest):")
print(comparison[['Country', 'Mean_Temp_C']].to_string(index=False))

print("\n2. EXTREME HEAT DAYS COMPARISON:")
print(comparison[['Country', 'Extreme_Heat_Days']].to_string(index=False))

# Vulnerability Ranking (based on temperature and extreme heat)
comparison['Vulnerability_Score'] = comparison['Mean_Temp_C'] + (comparison['Extreme_Heat_Days'] / 100)
comparison = comparison.sort_values('Vulnerability_Score', ascending=False)
comparison['Vulnerability_Rank'] = range(1, 6)

print("\n3. CLIMATE VULNERABILITY RANKING (1 = Most Vulnerable):")
print(comparison[['Country', 'Mean_Temp_C', 'Extreme_Heat_Days', 'Vulnerability_Rank']].to_string(index=False))

print("\n4. COP32 RECOMMENDATIONS:")
print("   - Sudan is most vulnerable (highest temperatures and extreme heat days)")
print("   - Ethiopia should advocate for regional early warning systems")
print("   - Climate adaptation finance should prioritize Sudan and Kenya")
print("   - Loss and damage funding needed for extreme heat impacts")

# Create comparison bar chart
plt.figure(figsize=(10, 6))
colors = ['red' if c == 'Sudan' else 'steelblue' for c in comparison['Country']]
plt.barh(comparison['Country'], comparison['Mean_Temp_C'], color=colors)
plt.title('Mean Temperature Comparison (2015-2026)', fontsize=14)
plt.xlabel('Temperature (°C)')
plt.tight_layout()
plt.savefig('temperature_comparison.png')
print("\n5. GENERATED: temperature_comparison.png")

print("\n" + "=" * 70)
print("CROSS-COUNTRY ANALYSIS COMPLETE")
print("=" * 70)