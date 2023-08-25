weight=float(input("Enter your weight(in kgs):"))
height=float(input("Enter your height(in m):"))

bmi=weight/(height*2)

bmi=round(bmi,1)

if bmi<18.0:
    idealweight=18.0*(height**2)
    print(f"Your BMI is {bmi}.You are underweight!")
    print(f"You should reach atleast {idealweight}kg to become healthy!")
elif 18.0<=bmi<=24.9:
    print(f"Your BMI is {bmi}.You are healthy!")
elif 25.0<=bmi<=29.9:
    idealweight=24.9*(height**2)
    print(f"Your BMI is {bmi}.You are overweight!")
    print(f"You should reach atleast {idealweight}kg to become healthy!")
else:
    idealweight=24.9*(height**2)
    print(f"Your BMI is {bmi}.You are obese!")
    print(f"You should reach atleast {idealweight}kg to become healthy!")
