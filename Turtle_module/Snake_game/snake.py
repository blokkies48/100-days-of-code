from turtle import Turtle
from math import ceil
   
START_POSITION_XY = [0,0]
MOVE_DISTANCE = 20
DIRECTIONS = "right" # Game starts where snake goes right


class Snake:
   
   def __init__(self):
      # Creating snake
      self.snake_body = []
      self.create_snake()
      self.current_direction = DIRECTIONS # Setting current_direction
      self.head = self.snake_body[0]


   def create_snake(self):
      snake_length = 3
      for _ in range(snake_length):
         snake_body_piece = Turtle("square")
         snake_body_piece.penup()
         snake_body_piece.color("white")
         snake_body_piece.goto(START_POSITION_XY[0],START_POSITION_XY[1])
         self.snake_body.append(snake_body_piece)
         START_POSITION_XY[0] -= 20 # Setting start position to -20 pixels behind the previous snake piece


   def move(self):
      
         # Logic for changing position of each snake piece
         for index in range(len(self.snake_body) - 1, 0, -1): # This will be range from the last index in the snake body list. e.g if the snake is 5 pieces, then it will in from index 4 to 0 and so on...
            # get the coordinates of the next snake piece
            new_x = self.snake_body[index - 1].xcor()
            new_y = self.snake_body[index - 1].ycor()
            # move the snake piece to the new position
            self.snake_body[index].goto(new_x,new_y)
            # Example of this is if the snake is 5 pieces long then the 2nd piece will take the 1st piece's position and the 3rd piece will take the 2nd piece's position and so on. 
         
         self.head.forward(MOVE_DISTANCE)
         

   def up(self):
      # Can only move up if you are going left or right   
      if self.current_direction == "right" or self.current_direction == "left":
         self.head.setheading(90)
         self.current_direction = "up"

   def down(self):
      # Can only move down if you are going left or right
      if self.current_direction == "right" or self.current_direction == "left":
         self.head.setheading(270)
         self.current_direction = "down"


   def right(self):
      # Can only move right if you are going up or down
      if self.current_direction == "up":
         self.head.right(90)
         self.current_direction = "right" 

      if self.current_direction == "down":
         self.head.left(90)
         self.current_direction = "right" 

   def left(self):
      # Can only move left if you are going up or down
      if self.current_direction == "up":
         self.head.left(90)
         self.current_direction = "left"

      if self.current_direction == "down":
         self.head.right(90)
         self.current_direction = "left"

   def add_snake_body_piece(self):
      self.snake_body.append(self.snake_body[1].clone())
      print("Piece added successfully")

   
   def coordinates(self):
      return [MOVE_DISTANCE * (round(self.head.xcor()/MOVE_DISTANCE)), MOVE_DISTANCE * (round(self.head.ycor()/MOVE_DISTANCE))]