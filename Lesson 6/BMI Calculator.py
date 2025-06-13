feet = float(input("Enter your height in feet:"))
weight = float(input("Enter your weight in kg:"))
metre = feet * 0.3048


BMI = weight / (metre * metre)

print("Your BMI is", BMI)

if BMI<=18.4:
    print("You are under weight")
elif BMI<=24.9:
    print("You are healthy")
elif BMI<=29.9:
    print("You are over weight")
elif BMI<=34.9:
    print("You are severely over weight")
elif BMI<=39.9:
    print("You are obese")
else:
    print("You are severely obese")
