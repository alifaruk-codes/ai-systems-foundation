"""
Task:
Calculate a freelancer's net income for a project.
The user inputs their hourly rate and total hours worked.
The system calculates the gross income, deducts a standart %20 tax,
and prints the final net income.

Input Format:
Line 1 (float): Hourly Rate.
Line 2 (float): Total Hours Worked.

Output Format:
Print th gross income, tax amount and final net income. 
"""
#Solution
hourly_rate = float(input("Enter Hourly Rate: "))
hours_worked = float(input("Enter Total Hours Worked: "))

gross_income = hourly_rate * hours_worked
tax_deduction = gross_income * 0.20
net_income = gross_income - tax_deduction

print(f"\nThe Gross Income: {gross_income}")
print(f"Tax Amount: {tax_deduction}")
print(f"Final Net Income: {net_income}")