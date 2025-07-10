num = int(input("Enter a number whose factorial you want to find: "))

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
    
print(factorial(num))