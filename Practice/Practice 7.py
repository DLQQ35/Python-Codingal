def start_game():
    print("Welcome to The Forest Adventure")

    name = input("Type Your Name:")
    print("Hello ", name, ". So, lets start the game!")

    print("You are standing on a road in between of the forest.")
    side = input("Which way will you move right or left:")
    side.lower()
    if side == "right":
        print("There is now a Cave in front of you.")
        cave = input("Do you want to enter the cave yes or no?")
        cave.lower()
        if cave == "yes" or "y":
            print("You felt that a wild animal is near you.You turn behind and see that a tiger is coming to eat you.There is a river in front of you and a tree.")
            shore = input("Would you jump in river or climb tree(write river or tree):")
            shore.lower()
            if shore == "tree":
                print("The tiger broke the tree because the tree was thin and you died!")
            else:  
                print("You survived from the tiger but you are severly injured.There are fruits on the tree.")
                fruits = input("Do you want to eat the fruits yes or no:")
                fruits.lower()
                if fruits == "yes" or "y":
                    print("You can now see smoke far away, which means that you have to travel till there to reach till humans.")
                    print("There is a car passing by but you can hear roar of lions.")
                    lion = input("Do you want to go near the Car yes or no?")
                    lion.lower()
                    if lion == "yes" or "y":
                        print("There you see that 3 lions are chasing the car.")
                        print("You can either jump and enter the car while trusting the driver or you can run away from the car.")
                        car = input("Do you want to enter the car yes or no?")
                        car.lower()
                        if car == "yes" or "y":
                            print("You survived and safely got out of Jungle!")
                        else:
                            print("You have been eaten by the lions and you died!")
                    else :
                        print("You starved and died!")
                else:
                    print("You died because you have been injured and didn't eat the fruits.")
    else:
        print("You can see a highway 2km  away.")
        highway = input("Do you want to go to highway yes or no?")
        highway.lower()
        if highway == "yes" or "y":
            print("You moved forward and never came back and no evidence was found of your body!!")


start_game()