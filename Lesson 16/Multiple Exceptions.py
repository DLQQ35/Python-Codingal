try:
    num1,num2 = eval(input("Enter two numbers seperated by a comma:"))
    result = num1 / num2
    print("The result is: ", result)
except ZeroDivisionError:
    print("The number cannot be divided by zero!!!")
except SyntaxError:
    print("Comma is missing. Enter the two numbers seperated by a comma like this: 2,3!!!")
except:
    print("Wrong Input!!!")
else:
    print("No Exceptions!!!")
finally:
    print("This text will always appear no matter what!!!")