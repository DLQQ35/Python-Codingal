import turtle
t = turtle.Pen()
screen = turtle.Screen()
t.speed(1)

bg = input("Enter the background color:")
if bg == "red":
    screen.bgcolor("red")
elif bg == "blue":
    screen.bgcolor("blue")
elif bg == "green":
    screen.bgcolor("green")
elif bg == "black":
    screen.bgcolor("black")
elif bg == "white":
    screen.bgcolor("white")
elif bg == "yellow":
    screen.bgcolor("yellow")
elif bg == "light yellow":
    screen.bgcolor("light yellow")
elif bg == "light blue":
    screen.bgcolor("light blue")
elif bg == "light red":
    screen.bgcolor("light red")
elif bg == "light green":
    screen.bgcolor("light green")
elif bg == "cyan":
    screen.bgcolor("cyan")
elif bg == "grey":
    screen.bgcolor("grey")
elif bg == "pink":
    screen.bgcolor("pink")
elif bg == "orange":
    screen.bgcolor("orange")
elif bg == "magenta":
    screen.bgcolor("magenta")
elif bg == "violet":
    screen.bgcolor("violet")
elif bg == "indigo":
    screen.bgcolor("indigo")
elif bg == "lime":
    screen.bgcolor("lime")
elif bg == "emerald":
    screen.bgcolor("emerald")
elif bg == "gold":
    screen.bgcolor("gold")

p = input("Select Pen Shape:")
if p == "spuare":
    t.shape("square")
elif p == "circle":
    t.shape("circle")
elif p == "triangle":
    t.shape("triangle")
elif p == "turtle":
    t.shape("turtle")
elif p == "arrow":
    t.shape("arrow")

while True:
    w = input("Select Turtle Widht(1,25,50,75,100,125,150,175,200,225,250,275,300,325,350,375,400,425,450,475,500,525,550,575,600,625,650):")

    if w == "1":
        t.width(1)
    elif w == "25":
        t.width(25)
    elif w == "50":
        t.width(50)
    elif w == "75":
        t.width(75)
    elif w == "100":
        t.width(100)
    elif w == "125":
        t.width(125)
    elif w == "150":
        t.width(150)
    elif w == "175":
        t.width(175)
    elif w == "200":
        t.width(200)
    elif w == "225":
        t.width(225)
    elif w == "250":
        t.width(250)
    elif w == "275":
        t.width(275)
    elif w == "300":
        t.width(300)
    elif w == "":
        t.width()