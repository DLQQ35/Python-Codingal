import random

playing = True
number = str(random.randint(10,20))

print("I WILL GENERATE A NUMBER BETWEEN 10-20 AND YOU HAVE TO GUESS IT.")
print("THE GAME ENDS WHEN YOU GUESS RIGHT.")

while playing:
    guess = input("GIVE ME YOUR BEST GUESS! :")
    if number == guess:
        print("THE NUMBER WAS",number)
        print("You WON!!!!!!")
        break
    else:
        print("YoUr GuEsS wAs WrOnG!")
        print("TRY AGAIN!!!!!!!!!!!!!")