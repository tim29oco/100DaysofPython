from turtle import Turtle
from turtle import Screen

player_1 = 0
player_2 = 0
FONT = ('Arial', 72, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.update_scoreboarD()

    def update_scoreboarD(self):
        self.clear()
        self.goto(x=-100, y=200)
        self.write(f"{self.l_score}",
                   align="center", font=FONT)
        self.goto(x=100, y=200)
        self.write(f"{self.r_score}", align="center", font=FONT)
        self.hideturtle()

    def l_point(self):
        self.l_score += 1
        self.update_scoreboarD()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboarD()
