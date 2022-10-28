import turtle
from turtle import Turtle

FONT = ("Courier", 18, "normal")
ALIGN = "center"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def update_score(self):
        self.write(
            f"Score is: {self.score}",
            align=ALIGN,
            font=FONT
        )

    def game_over(self):
        self.goto(0, 0)
        self.write(
            f"Game over.",
            align=ALIGN,
            font=FONT
        )