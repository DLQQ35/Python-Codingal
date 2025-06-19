n = int(input("Enter the Whole Number whose sum you want to find: "))

sum = 0

for i in range(1, n+1):
    sum = sum + i
    print("\nsum =",sum)