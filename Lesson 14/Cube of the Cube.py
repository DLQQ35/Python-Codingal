number = int(input("Enter the number whose cube is to be calculated: "))

def cube(num):
    return num*num*num

def division(num):
    if num%3 == 0:
        return cube(num)
    else:
        return False

print(division(number))