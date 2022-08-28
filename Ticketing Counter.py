print("Welcome to Rollercoaster!!")
height = int(input("May I know your Height in cm's:\n"))
bill = 0
if height <= 120:
    print("Sorry, You Can't ride!!!")
else:
    print("Yes,You Can Ride!!!")
    age = int(input("May I know your Age:\n"))
    if age >= 18:
        bill = 1200
        print("You Need to Pay 1200/-")
    elif age > 12 and age < 18:
        bill = 700
        print("You Need to pay 700/-")
    else:
        bill = 500
        print("You need to pay 500/-")

    pics = input("Do you want any pic's? yes or no:\n")
    if pics == "yes":
        bill +=  300
        print(f"Your Bill is {bill}")
    else:
        print(f"Your bill is {bill}")
