from random import randint
from turtle import Screen, Turtle, colormode, bgcolor


turtle_1 = Turtle()
screen = Screen()

def move_forward():
    turtle_1.forward(10)

def turn_right():
    turtle_1.right(5)

def turn_left():
    turtle_1.left(5)

def move_backward():
    turtle_1.backward(10)

def clear():
    turtle_1.reset()


screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="c", fun=clear)




screen.exitonclick()