import turtle

turtle.Screen().bgcolor("black")
turtle.Screen().setup(width = 1.0, height = 1.0)

turtle.Screen().title("Spiral")

Spiral = turtle.Turtle()

Spiral.pencolor("white")

size = 0

while True:
    for i in range(4):
        Spiral.forward(size + 1)
        Spiral.left(90)
        size = size - 5
    size = size + 1
