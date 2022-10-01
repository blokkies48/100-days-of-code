from turtle import Turtle


class Text_To_Screen(Turtle):
    
    def __init__(self):
        self.score = 0
        super().__init__()
        
        
    def display_score(self):
        self.color("white")
        self.penup()
        self.ht()
        self.clear()
        self.goto(0,250)
        self.write(f"Score = {self.score}", True, align="center", font=("Courier", 20, "normal"),)

    def game_over(self):
        self.score
        self.goto(0,0)
        self.color("white")
        self.penup()
        self.ht()
        self.write(f"Game Over!", True, align="center",font = ("Arial",40,"bold"))
        self.goto(0,-40)
        self.write(f"Your score was {self.score}", align="center",font = ("Courier",20,"bold"))