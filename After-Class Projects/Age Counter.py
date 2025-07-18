age  = int(input("Enter your age: "))

if(age>=18):
    if(age%2==0):
        print("Your age is even")
    else:
        print("Your age is odd")
else:
    print("You are a kid")