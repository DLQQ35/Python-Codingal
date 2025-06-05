print("Enter the marks obtained in the following subjects: ")

maths = int(input("Maths:"))
science = int(input("Science:"))
english = int(input("English:"))
hindi = int(input("Hindi:"))
sst = int(input("Social Studies:"))

sum = maths + science + english + hindi + sst

print("Sum of all 4 subjects: ", sum)

percentage = (sum/500)*100
print("Percentage is: ", percentage)