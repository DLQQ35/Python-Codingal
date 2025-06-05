Amount = int(input("Please enter the amount you have:"))

note1 = Amount // 100
note2 = (Amount % 100) // 50
note3 = ((Amount % 100)%50) //10

print("The number of note of 100:",note1)
print("The number of note of 50: ",note2)
print("The number of note of 10: ",note3)
