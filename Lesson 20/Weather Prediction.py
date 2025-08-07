weather = (1,0,1,1,1,0,0,0,1,0)
sunny = 0
rainy = 0

for i in range(0,10):
    if weather[i] == 0:
        sunny += 1
    else:
        rainy += 1

if sunny>rainy:
    print("It is Good Weather")
elif sunny == rainy:
    print("It is a Moderate Weather")
else:
    print("It is a Bad Weather")