"""
Task:
Write a simple calculator to split a restaurant bill among friends.
The program should take the total bill amount and the number of people,
add a 10% service charge, and calculate how much each person needs to pay.

Input Format:
The first line is a float: total bill amount.
The second line is an integer: number of people.

Output Format:
Print the total amount including the service charge, and the cost per person.

Sample Input:
500.0
4

Sample Output:
Total Bill (with 10% tip): $550.0
Amount Per Person: $137.5
"""
Bill_amount = float(input("Enter the bill amount: "))
Number_of_people = int(input("Enter the number of people: "))

Total_bill_with_tip = Bill_amount * 1.10
Amount_per_person = Total_bill_with_tip / Number_of_people

print(f"Total Bill (with 10% tip): ${Total_bill_with_tip}")
print(f"Amount Per Person: ${Amount_per_person}")