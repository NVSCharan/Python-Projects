a = int(input("Enter the Year:\n"))
b = a % 4
c = a % 100
d = a % 400
if b == 0:
    if c == 0:
        if d == 0:
            print("leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Leap Year")
else:
    print("Not a Leap Year")