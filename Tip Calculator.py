print("Welcome to Tip Calculator!!!")
bill = float(input("Enter the toatal Amount of Bill:\n"))
tip = int(input("Enter the tip Amount that you want to give\na)10\nb)15\nc)20\n"))
people = int(input("How many people to split the bill?\n"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")
