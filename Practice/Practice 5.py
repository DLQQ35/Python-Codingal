import os
print("This Program will show that which user is logged in your computer")

variable = os.environ.get("PATH")
print(os.getlogin())