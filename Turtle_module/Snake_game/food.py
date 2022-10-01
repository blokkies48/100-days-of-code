from random import randrange
from turtle import Turtle

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.food_x = 0
        self.food_y = 0

    def display_food(self):
        self.food_x = randrange(-260,260,20)
        self.food_y = randrange(-260,260,20)
        self.shape("circle")
        self.penup()
        self.color("red")
        self.shapesize(0.5,0.5)
        self.goto(self.food_x, self.food_y)

    def remove_food(self):
        self.clear()

    def coordinates(self):
        return [self.food_x, self.food_y]

    
        

    