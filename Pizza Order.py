print("Hey Welcome to Pizzeria!!")
size = str(input("What size Pizza do you want? S, M and L\n"))
bill = 0
if size == "S": 
    bill = 300
elif size == "M": 
    bill = 450
else: 
    bill = 600

peperoni = input("Do you want peperoni?? yes or no\n")

if peperoni == "yes" and size == "S": 
    bill += 100
elif peperoni == "yes" and size == "M" or size == "L": 
    bill += 150
else: 
    bill = bill

cheese = input("Do you want Extra Cheese?? yes or no\n")

if cheese == "yes":
    bill += 200
else: 
    bill = bill

print(f"Your Total Bill = {bill}")