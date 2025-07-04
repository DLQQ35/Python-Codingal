import turtle

turtle.Screen().bgcolor("black")
turtle.Screen().setup(width = 1.0, height = 1.0)

square = turtle.Turtle()

square.pencolor("white")

nusides = 4
sidelength = 200
angle = 360 / nusides

for i in range(nusides):
    square.forward(sidelength)
    square.right(angle)
turtle.done()