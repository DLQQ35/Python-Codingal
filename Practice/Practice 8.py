import os
print("This Program will show that which user is logged in your computer")
print("This will do it by hacking your computer/laptop!")

variable = os.environ.get("PATH")
print(os.getlogin())