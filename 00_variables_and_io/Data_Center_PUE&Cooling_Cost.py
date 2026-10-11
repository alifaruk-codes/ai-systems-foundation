"""
Task;
Calculate the Power Usage Effectiveness (PUE) and the daily cooling cost of an AI Data Center.
PUE is the ratio of total facility poweer to IT equipment power.
Ideal PUE is 11.0 (meaning 0 energy wasted on cooling).

Input Format:
Line 1 (float): IT Equipment Power (Megawatts).
Line 2 (float): Cooling System Power (Megawatts).
Line 3 (float): Cost Of 1 Megawatt-hour (MW/h) in USD.

Constraints:
IT POwer > 0

Output Format:
Print the PUE ratio.
Print the total daily (24h) cost of the facility in USD.
"""
#Solution
IT_equipment_power = float(input("Enter the IT Equipment Power (Megawatts): "))
Cooling_system_power = float(input("Enter the Cooling System Power (Megawatts): "))
Cost_of_megawatt_hour = float(input("Enter the Cost of 1 Megawatt-hour in USD: "))

total_power = IT_equipment_power + Cooling_system_power
pue = total_power / IT_equipment_power
daily_cost = total_power * Cost_of_megawatt_hour * 24

print(f"PUE Ratio: {pue}")
print(f"Total Daily (24h) Cost of the Facility: ${daily_cost:,}")
