print("Welcome to the bill calculator")

print("This restaurant has a total tip percentage of 10%.")

bill_amount = float(input("Enter the bill amount: "))

def total_bill_calculator(bill_amount,tip_percentage=10):
    total = bill_amount * (1 + 0.01 * tip_percentage)
    total = round(total,2)
    print("The total bill is:",total)
total_bill_calculator(bill_amount)