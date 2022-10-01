from turtle import Screen
import time
from food import Food
from snake import Snake
from text_to_screen import *

REFRESH_RATE = 0.1


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
# Objects
food = Food()
snake = Snake()
text_to_screen = Text_To_Screen()
# Listening to key presses
def listen_keypress():
    screen.listen()
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down,"Down")
    screen.onkey(snake.right,"Right")
    screen.onkey(snake.left,"Left")




def main():
    
    listen_keypress()
    food_displayed = False
    play_game = True
    text_to_screen.display_score()
    while play_game:
        
     
        screen.update()
        time.sleep(REFRESH_RATE)
        snake.move()

        # Places food on screen when their is no food
        if food_displayed == False:
            food.display_food()
            food_displayed = True
        
        # Snake eats
        # When food coordinates are equal to the head of the snake snake length increase
        if snake.head.distance(food) < 1:
            snake.add_snake_body_piece()
            food_displayed = False # So not another food item is spawned
            food.remove_food()
            text_to_screen.score += 1
            text_to_screen.display_score()

        # If snake hits a wall
        if (snake.coordinates()[0] == -320 or snake.coordinates()[1] == -320) or (snake.coordinates()[0] == 320 or snake.coordinates()[1] == 320):
            text_to_screen.game_over()
            play_game = False

        # If snake hits its tail
        for segment in snake.snake_body[1:]:
            if snake.head.distance(segment) < 10:
                text_to_screen.game_over()
                play_game = False

if __name__ == "__main__":
    main()

screen.exitonclick()

