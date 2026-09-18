## Input we need from user
# Total rent
# Total food order for snacking
# Electricity units spend
# Charger per unit
# persons living in room/flat

# Output
# Total amount you have to  pay

rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter the amount of food order = "))
electricity_spend = int(input("Enter the total of electricity spend = "))
charger_per_unit = int(input("Enter the charger per unit = "))
persons = int(input("Enter the number of persons living in room/flat = "))

total_bill = electricity_spend * charger_per_unit

output = (food + rent + total_bill)
print("Each person will pay = ", output)