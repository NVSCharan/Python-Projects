weight = float(input("Enter your Weight in Kg's:\n"))
height = float(input("Enter your Height in Mt's:\n"))
bmi = weight/(height * height)
bmi = round(bmi)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are slightly underweight")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you are in Normal weight") 
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are in Slightly overweight")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are in Obese")
else:
    print(f"Your BMI is {bmi}, you are in Clinically Obese")