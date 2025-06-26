num = int(input("Enter a number:"))

t = num
numlen = 0

while t > 0:
    numlen += 1
    t = t // 10
    
if numlen >= 4:
    numlen = int(numlen/2)
    check = 0
    while num > 0:
        rem = num % 10
        if check == numlen:
            midone = rem
        elif check == (numlen-1):
            midtwo = rem
        check += 1
        num = int(num / 10)
    product = midone * midtwo
    print("The middle product is:", product)
else:
    print("The number is not long enough to have a middle product.")
