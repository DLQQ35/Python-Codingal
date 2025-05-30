name = input("Enter your name:")
print("Hello", name)
print("Data Type of your name is", type(name))

age = int(input("Enter your age:"))
print("Age:",age)
print("Data Type of your age is", type(age))

weight = input("Enter your weight:")
print("Weight:",weight)
print("Data Type of your weight is", type(weight))

is_student = input("Are you a student? (yes/no):")
print(is_student)
print("Data Type of is_student is", type(is_student))

print("\n")

print("After Typecasting: \n")

name = float(name)
print("Data Type of your name is", type(name))

age = str(age)
print("Data Type of your age is", type(age))

weight = bool(weight)
print("Data Type of your weight is", type(weight))

is_student = int(is_student)
print("Data Type of is_student is", type(is_student))


