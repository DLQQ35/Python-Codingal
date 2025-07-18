print("This program will create a Right-Angle Triangle from '*'")
t = int(input("Enter the Number of rows:"))

for i in range(t):
    for j in range(i+1):
        print("*", end=" ")
    print()
print("Not Complete!!!")