from random import randint
from turtle import Screen, Turtle, colormode

turtle_1 = Turtle()
colormode(255)
turtle_1.color(randint(0,255), randint(0,255), randint(0,255))


def main():
    spirograph(turtle_1,100,200)

# Passing turtle object then the length of the line and the number of dashes wanted
def dashed_line(turtle,length_of_dash, number_dashes):
    for _ in range(number_dashes):
        turtle.pencolor(randint(0,255), randint(0,255), randint(0,255))
        turtle.forward(length_of_dash)
        turtle.penup()
        turtle.forward(length_of_dash)
        turtle.color()
        turtle.pendown()

# Used to draw shape
def draw_shape(sides):
    angle = 360/sides
    for _ in range(sides):
        dashed_line(turtle_1, 5, 10)
        turtle_1.right(angle) 

# Method draws random shapes. ## Run in main()   
def draw_shapes():
    drawn_shapes = [] # Save drawn shapes
    for shape_side in range(3,8):
        while True: # Make sure no repeated shapes
            shape_side = randint(3,10)
            if shape_side not in drawn_shapes:
                draw_shape(shape_side)
                drawn_shapes.append(shape_side)
                break

# Random walk into a random direction ## Run in main
def random_walk(turtle_object,amount_of_turns, length):
    for _ in range(amount_of_turns):
        turn = randint(1,5)
        turtle_object.pencolor(randint(0,255), randint(0,255), randint(0,255))
        turtle_object.width(10)
        turtle_object.speed(5)

        if turn == 1:
            turtle_object.forward(length)
        if turn == 2:
            turtle_object.backward(length)
        if turn == 3:
            turtle_object.forward(length)
            turtle_object.right(90)
        if turn == 4:
            turtle_object.forward(length)
            turtle_object.left(90)

# Spirograph ## Run in main
def spirograph(turtle_object, radius, num_of_circles):
    angle = 360/num_of_circles
    turtle_object.speed("fastest")
    for _ in range(num_of_circles):
        turtle_object.pencolor(randint(0,255), randint(0,255), randint(0,255))
        turtle_object.left(angle)
        turtle_object.circle(radius)

if __name__ == "__main__":
    main()




screen = Screen()
screen.exitonclick()