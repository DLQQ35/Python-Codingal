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
    elif w == "325":
        t.width(325)
    elif w == "350":
        t.width(350)
    elif w == "375":
        t.width(375)
    elif w == "400":
        t.width(400)
    elif w == "425":
        t.width(425)
    elif w == "450":
        t.width(450)
    elif w == "475":
        t.width(475)
    elif w == "500":
        t.width(500)
    elif w == "525":
        t.width(525)
    elif w == "550":
        t.width(550)
    elif w == "575":
        t.width(575)
    elif w == "600":
        t.width(600)
    elif w == "625":
        t.width(625)
    elif w == "650":
        t.width(650)
    c = input("Select Pen Color:")
    if c == "red":
        t.pencolor("red")
    elif c == "blue":
        t.pencolor("blue")
    elif c == "green":
        t.pencolor("green")
    elif c == "black":
        t.pencolor("black")
    elif c == "white":
        t.pencolor("white")
    elif c == "yellow":
        t.pencolor("yellow")
    elif c == "light yellow":
        t.pencolor("light yellow")
    elif c == "light blue":
        t.pencolor("light blue")
    elif c == "light red":
        t.pencolor("light red")
    elif c == "light green":
        t.pencolor("light green")
    elif c == "cyan":
        t.pencolor("cyan")
    elif c == "grey":
        t.pencolor("grey")
    elif c == "brown":
        t.pencolor("brown")
    elif c == "magenta":
        t.pencolor("magenta")
    elif c == "orange":
        t.pencolor("orange")
    elif c == "pink":
        t.pencolor("pink")
    elif c == "purple":
        t.pencolor("purple")
    elif c == "violet":
        t.pencolor("violet")
    elif c == "indigo":
        t.pencolor("indigo")
    elif c == "turquoise":
        t.pencolor("turquoise")
    elif c == "lime":
        t.pencolor("lime")
    elif c == "aqua":
        t.pencolor("aqua")
    elif c == "maroon":
        t.pencolor("maroon")
    elif c == "gold":
        t.pencolor("gold")
    d = input("Select the direction and steps taken by the turtle:")
    if d == "f1":
        t.fd(1)
    elif d == "f10":
        t.fd(10)
    elif d == "f20":
        t.fd(20)
    elif d == "f30":
        t.fd(30)
    elif d == "f40":
        t.fd(40)
    elif d == "f50":
        t.fd(50)
    elif d == "f60":
        t.fd(60)
    elif d == "f70":
        t.fd(70)
    elif d == "f80":
        t.fd(80)
    elif d == "f90":
        t.fd(90)
    elif d == "f100":
        t.fd(100)
    elif d == "b1":
        t.back(1)
    elif d == "b10":
        t.back(10)
    elif d == "b20":
        t.back(20)
    elif d == "b30":
        t.back(30)
    elif d == "b40":
        t.back(40)
    elif d == "b50":
        t.back(50)
    elif d == "b60":
        t.back(60)
    elif d == "b70":
        t.back(70)
    elif d == "b80":
        t.back(80)
    elif d == "b90":
        t.back(90)
    elif d == "b100":
        t.back(100)
    elif d == "r45":
        t.rt(45)
    elif d == "r90":
        t.rt(90)
    elif d == "r135":
        t.rt(135)
    elif d == "r180":
        t.rt(180)
    elif d == "r225":
        t.rt(225)
    elif d == "r270":
        t.rt(270)
    elif d == "r315":
        t.rt(315)
    elif d == "r360":
        t.rt(360)
    elif d == "45":
        t.lt(45)
    elif d == "90":
        t.lt(90)
    elif d == "1135":
        t.lt(135)
    elif d == "180":
        t.lt(180)
    elif d == "225":
        t.lt(225)
    elif d == "270":
        t.lt(270)
    elif d == "315":
        t.lt(315)
    elif d == "360":
        t.lt(360)
    elif d == "c10":
        t.circle(10)
    elif d == "c20":
        t.circle(20)
    elif d == "c30":
        t.circle(30)
    elif d == "c40":
        t.circle(40)
    elif d == "c50":
        t.circle(50)
    elif d == "c60":
        t.circle(60)
    elif d == "c70":
        t.circle(70)
    elif d == "c80":
        t.circle(80)
    elif d == "c90":
        t.circle(90)
    elif d == "c100":
        t.circle(100)
    elif d == "sc10":
        t.circle(10, 180)
    elif d == "sc20":
        t.circle(20, 180)
    elif d == "sc30":
        t.circle(30, 180)
    elif d == "sc40":
        t.circle(40, 180)
    elif d == "sc50":
        t.circle(50, 180)
    elif d == "sc60":
        t.circle(60, 180)
    elif d == "sc70":
        t.circle(70, 180)
    elif d == "sc80":
        t.circle(80, 180)
    elif d == "sc90":
        t.circle(90, 180)
    elif d == "sc100":
        t.circle(100, 180)
    elif d == "pu":
        t.penup()
    elif d == "pd":
        t.pendown()
    elif d == "sf":
        t.begin_fill()
    elif d == "ef":
        t.end_fill()