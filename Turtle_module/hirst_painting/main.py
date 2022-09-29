import colorgram
from random import randint
from turtle import Screen, Turtle, colormode, bgcolor


# List of the 12 most dominate colors
colors = colorgram.extract("F:\\100 days of code\\Turtle_module\\hirst_painting\\dots.jpg", 30)

# Move to a corner and creating turtle instance
screen = Screen()
turtle_1 = Turtle()
colormode(255)
bgcolor(colors[0].rgb)
turtle_1.penup()
turtle_1.goto(-200,-200)
turtle_1.pendown()

# Writing dots
def dot(turtle, number_dots):
    for _ in range(number_dots):
        turtle.dot(20,colors[randint(4,29)].rgb)
        turtle.penup()
        turtle.forward(50)
# Draws dots to screen
line_pos = -150
for _ in range(10):
    dot(turtle_1,10)
    turtle_1.penup()
    turtle_1.goto(-200, line_pos)
    turtle_1.pendown()
    line_pos += 50
    
   

screen.exitonclick()
