import random

def game():
    options = ["Rock", "Paper", "Scissors"]

    user = input("Enter your choice: Rock, Paper, or Scissors: ")

    computer = random.choice(options)

    print("3")
    print("2")
    print("1")
    print("We have got the results from you and your opponent.")
    print("You chose ",user)
    print("\n \n \nAND,")
    print("\n \n \nYour opponent chose ",computer)

    if user == computer:
        print("It's a tie!")
    elif user == "Rock" and computer == "Scisssors":
        print("Your Rock smashed the opponent's Scissors! You Win!!")
    elif user == "Paper" and computer == "Rock":
        print("Your Paper covered the opponent's Rock! You Win!!")
    elif user == "Scissors" and computer == "Paper":
        print("Your Scissors tore the opponent's Paper! You Win!!")

    elif computer == "Rock" and user == "Scisssors":
        print("Your opponent's Rock smashed your Scissors! You Lose!!")
    elif computer == "Paper" and user == "Rock":
        print("Your opponent's Paper covered your Rock! You Lose!!")
    elif user == "Scissors" and computer == "Paper":
        print("Your opponent's Scissors tore your Paper! You Lose!!")
    else:
        print("You entered an invalid option. Please try again.")

while True:
    game()
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        print("Thank you for playing!")
        break