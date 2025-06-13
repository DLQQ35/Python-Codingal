medical_cause = input("Did you have medical cause Y or N:")

attendance = int(input("Enter your Attendance:"))


if medical_cause == "Y":
    print("You are allowed")
else:
    if attendance>=75:
        print("You are allowed")
    else:
        print("You are not allowed")
