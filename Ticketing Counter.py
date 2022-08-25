height = int(input("Enter your Height in Cm's:\n"))
if height >= 120:
    print("Yes You Can Ride!!!")
    age = int(input("Please Enter your Age:\n"))
    if age >= 18: 
        print("Please Pay 1000/-")
    elif age >= 12 and age < 18:
        print("Please Pay 600/-")
    else:
        print("Please Pay 400/-")
else:
    print("Sorry you Cant Ride")