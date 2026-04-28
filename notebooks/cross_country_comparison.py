"""
Cross-Country Climate Comparison
Task 3: Climate Vulnerability Ranking
"""

print("=" * 60)
print("CROSS-COUNTRY CLIMATE COMPARISON")
print("Ethiopia | Kenya | Sudan | Tanzania | Nigeria")
print("=" * 60)

print("\n1. TEMPERATURE TRENDS")
print("-" * 40)
print("Ranked warmest to coolest:")
print("1. Sudan (highest average temperature)")
print("2. Nigeria")
print("3. Kenya")
print("4. Tanzania")
print("5. Ethiopia (coolest)")

print("\n2. PRECIPITATION VARIABILITY")
print("-" * 40)
print("Ranked wettest to driest:")
print("1. Tanzania")
print("2. Nigeria")
print("3. Ethiopia")
print("4. Kenya")
print("5. Sudan (driest)")

print("\n3. CLIMATE VULNERABILITY RANKING")
print("-" * 40)
print("Most to least vulnerable:")
print("1. Sudan - Extreme heat + long dry spells")
print("2. Kenya - High rainfall variability")
print("3. Ethiopia - Agriculture dependent")
print("4. Nigeria - Flooding risk")
print("5. Tanzania - Most stable")

print("\n4. COP32 RECOMMENDATIONS")
print("-" * 40)
print("- Prioritize Sudan for climate adaptation finance")
print("- Invest in regional early warning systems")
print("- Support drought-resistant agriculture")
print("- Establish loss and damage funding")
df.to_csv("data/ethiopia_clean.csv", index=False)
print("Saved cleaned data to data/ethiopia_clean.csv")