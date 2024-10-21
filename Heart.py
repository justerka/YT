import turtle

# Set up the turtle
turtle.setup(width=800, height=600)
turtle.bgcolor("white")
turtle.title("Heart Image")
turtle.speed(2)

# Draw the heart shape
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
turtle.color("red")
turtle.begin_fill()
turtle.left(140)
turtle.forward(224)
for _ in range(200):
    turtle.right(1)
    turtle.forward(2)
turtle.left(120)
for _ in range(200):
    turtle.right(1)
    turtle.forward(2)
turtle.forward(224)
turtle.end_fill()

# Hide the turtle
turtle.hideturtle()

# Exit on click
turtle.exitonclick()
