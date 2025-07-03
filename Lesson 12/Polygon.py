import turtle

turtle.Screen().bgcolor("red")
turtle.Screen().setup(width = 1.0, height = 1.0)

polygon = turtle.Turtle()

nusides = 6
sidelength = 70
angle = 360 / nusides

for i in range(nusides):
    polygon.forward(sidelength)
    polygon.right(angle)
turtle.done()