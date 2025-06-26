word = input("Enter the word:")
character = input("Enter the Character:")

i = 0
count = 0  

while i < len(word):
    if word[i] == character:
        count = count + 1
    i = i + 1
print("The number of times the character is repeating is:",count)