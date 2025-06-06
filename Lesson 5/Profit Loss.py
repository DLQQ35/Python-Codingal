print("This program will calculate the profit(Enter in decimal format).")
cp = float(input("Enter the cost price: "))
sp = float(input("Enter the selling price: "))
if sp > cp:
    print("Profit")
    print("Profit =",sp-cp)
else:
    print("Loss")
    print("Loss =",cp-sp)
