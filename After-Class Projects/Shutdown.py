import os

choice = input("Do you want to shutdown your computer? (y/n)")

if choice == "y":
    os.system("shutdown /s /t 1")
else:
    print("Shutdown cancelled")