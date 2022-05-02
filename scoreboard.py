FONT = ("Courier", 14, "normal")
from turtle import *


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-260, 260)
        self.hideturtle()
        self.write("Your Score is: 0", align="center", font=FONT)

    def score_update(self, score):
        self.clear()
        self.write(f"Your Score is: {score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)
