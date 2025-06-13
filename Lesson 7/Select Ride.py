print("Select Your Ride in Number:")
print("1.Two-Wheeler")
print("2.Four-Wheeler")

choice = int(input("Enter Your Choice:"))

if choice == 1:
    print("What type of Two-Wheeler?")
    print("1.Bike")
    print("2.Scooter\n")
    choice2 = int(input("Enter Your Choice:"))
    if choice2 == 1:
        print("You have selected Bike")
    else:
        print("You have selected Scooter")
elif choice == 2:
    print("What type of Four-Wheeler?")
    print("1.Sedan")
    print("2.XUV\n")
    choice3 = int(input("Enter Your Choice:"))
    if choice3 == 1:
        print("You hav selected Sedan")
    else:
        print("You have selected XUV")
else:
    print("Wrong Choice")
