from turtle import Turtle

FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-235,270)
        self.write(f"Score: {self.score}", move=False, align="center",font=FONT)

    def addScore(self):
        self.clear()
        self.goto(-235,270)
        self.score += 1
        self.write(f"Score: {self.score}", move=False, align="center",font=FONT)