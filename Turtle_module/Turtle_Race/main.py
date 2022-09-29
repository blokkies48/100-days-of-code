from random import randint
from turtle import Screen, Turtle, colormode, speed

screen = Screen()
screen.setup(width=500,height=400)

users_choice = screen.textinput(title="Make your bet!", prompt="Select a color you want to bet on:\nRed, Green, Blue, Purple").lower()

# Could use for loops to generate all the turtles but felt here I wanted to take another approach 

# Creating instances of turtles
turtle_1 = Turtle()
turtle_2 = Turtle()
turtle_3 = Turtle()
turtle_4 = Turtle()

# Setting the positions to zero this is done to check for the winner in while loop
turtle_1_position = 0
turtle_2_position = 0
turtle_3_position = 0
turtle_4_position = 0

# Need the pen up the whole time
turtle_1.penup()
turtle_2.penup()
turtle_3.penup()
turtle_4.penup()

# Setting the shape of each turtle
turtle_1.shape("turtle")
turtle_2.shape("turtle")
turtle_3.shape("turtle")
turtle_4.shape("turtle")

# Giving each turtle a color
turtle_1.color("red")
turtle_2.color("green")
turtle_3.color("blue")
turtle_4.color("purple")

# Moving each turtle to its starting spot
turtle_1.goto(-250,100)
turtle_2.goto(-250,50)
turtle_3.goto(-250,0)
turtle_4.goto(-250,-50)


# Race logic
while True:
    
    speed_of_t_1 = randint(1,10)
    turtle_1.speed(speed_of_t_1)
    turtle_1_position += speed_of_t_1
    turtle_1.forward(speed_of_t_1)

    speed_of_t_2 = randint(1,10)
    turtle_2.speed(speed_of_t_2)
    turtle_2_position += speed_of_t_2
    turtle_2.forward(speed_of_t_2)

    speed_of_t_3 = randint(1,10)
    turtle_3.speed(speed_of_t_3)
    turtle_3_position += speed_of_t_3
    turtle_3.forward(speed_of_t_3)

    speed_of_t_4 = randint(1,10)
    turtle_4.speed(speed_of_t_4)
    turtle_4_position += speed_of_t_4
    turtle_4.forward(speed_of_t_4)

    # Win conditions with user input
    if turtle_1_position > 480:
        turtle_1.write("Winner",align="center")
        if users_choice == "red":
            screen.title("You Win")
            
        else:
            screen.title("You Lose")
        break
    if turtle_2_position > 480:
        turtle_2.write("Winner",align="center")
        if users_choice == "green":
            screen.title("You Win")
        else:
            screen.title("You Lose")
        break
    if turtle_3_position > 480:
        turtle_3.write("Winner", align="center")
        if users_choice == "blue":
            screen.title("You Win")
        else:
            screen.title("You Lose")
        break
    if turtle_4_position > 480:
        turtle_4.write("Winner",align="center")
        if users_choice == "purple":
            screen.title("You Win")
        else:
            screen.title("You Lose")
        break

screen.exitonclick()


        
        
