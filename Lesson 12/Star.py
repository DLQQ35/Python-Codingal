import turtle

turtle.Screen().bgcolor("black")
turtle.Screen().setup(width = 1.0, height = 1.0)

Star = turtle.Turtle()

Star.color("white")
Star.fillcolor("white")
Star.begin_fill()

Star.forward(100)
Star.left(120)
Star.forward(100)
Star.left(120)
Star.forward(100)

Star.penup()

Star.right(150)
Star.forward(50)

Star.pendown()

Star.right(90)
Star.forward(100)
Star.right(120)
Star.forward(100)
Star.right(120)
Star.forward(100)

Star.end_fill()

turtle.done()