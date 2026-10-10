"""
Task:
Calculate the total fuel cost for a road trip.
The program asks for the total distance in kilometers, the car's fuel consumption 
(liters per 100 km), and the current price of 1 liter of fuel.

Input Format:
Line 1 (float): Distance in km.
Line 2 (float): Fuel consumption per 100 km.
Line 3 (float): Fuel price per liter.

Output Format:
Print the total liters of fuel required and the total estimated cost.
"""

distance = float(input("Enter the distance(km): "))
consumption_per_100km = float(input("Enter the fuel consumption per 100 km (L): "))
fuel_price = float(input("Enter the fuel price per liter: "))

total_fuel_needed = (distance / 100) * consumption_per_100km
total_fuel_cost = total_fuel_needed * fuel_price

print(f"\nTotal Fuel Required: {total_fuel_needed:.2f} L")
print(f"Total Estimated Cost: ${total_fuel_cost:.2f}")