bill = float(input("Enter the total bill amount: "))
tip_percentage = float(input("Enter the tip percentage you would like to give (e.g., 15 for 15%): "))
tip_amount = bill * (tip_percentage / 100)  
people = int(input("Enter the number of people to split the bill: "))
total_amount = bill + tip_amount
amount_per_person = total_amount / people
print(f"Each person should pay: ${amount_per_person:.2f}")