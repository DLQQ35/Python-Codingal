string = input("Please enter the text you want to reverse:")

string2 = ''

for i in string:
    string2 = i + string2
print("The text you entered is: ", string)
print("The reversed text is: ", string2)