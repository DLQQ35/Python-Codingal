import math

num = float(input("Enter a number in decimal form:"))

print("The Floor and Ceiling value of",num,"is",math.floor(num),"and",math.ceil(num))

x = float(input("Enter a number in decimal form for variable x:"))
y = float(input("Enter a number in decimal form for variable y with different sign:"))

print("The value of X after copying the sign of Y is",math.copysign(x,y))

print("Absolute Value of X:",math.fabs(x),"and Absolute Value of Y:",math.fabs(y))

print("The GCD(Greatest Common Divvisor) of X and Y is",math.gcd(int(x),int(y)),"after removing numbers after decimal point.")