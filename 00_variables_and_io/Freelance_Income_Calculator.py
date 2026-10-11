hourly_rate = float(input("Enter Hourly Rate: "))
hours_worked = float(input("Enter Total Hours Worked: "))

gross_income = hourly_rate * hours_worked
tax_deduction = gross_income * 0.20
net_income = gross_income - tax_deduction

print(f"\nThe Gross Income: {gross_income}")
print(f"Tax Amount: {tax_deduction}")
print(f"Final Net Income: {net_income}")