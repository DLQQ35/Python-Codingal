try:
    num = int(input("Enter a number:"))
    print("The number is", num)
except ValueError as e:
    print("Exception:",e)