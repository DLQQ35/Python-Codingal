class Employee():

    def __init__(self):
        print("Employees Created.")
    def __del__(self):
        print("Destructor Called.") 
    
def createobject():
    print("Making Object.")
    obj = Employee()
    print("Function Ended.")
    return obj

print("Calling Function 'createobject()'")
obj = createobject()
print("Program Ended.")