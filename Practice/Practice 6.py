import os
print("I can tell the name of the user logged in in this device!")

variable = os.environ.get("PATH")
print(os.getlogin())