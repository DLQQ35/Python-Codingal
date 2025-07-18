print("This program will calculate the due amount for the Bill.")

print("This is a buffet restaurant. The total price is 1500 per person.")
bill = 1500

amount_given = float(input("How much money did you give? "))

bill_left = (bill-amount_given)

print("You have to pay",bill_left,"to the restaurant.")