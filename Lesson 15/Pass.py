for num in range(20):
    if num % 20 == 0:
        print("This number is divisible by 20.")
    elif num % 15 == 0:
        pass
    elif num % 10 == 0:
        print("This number is divisible by 10")
    elif num % 5 == 0:
        print("This number is divisible by 5")
    elif num % 3 == 0:
        print("This number is divisible by 3")
    elif num % 2 == 0:
        print("This number is divisible by 2")
    else:
        print(num)