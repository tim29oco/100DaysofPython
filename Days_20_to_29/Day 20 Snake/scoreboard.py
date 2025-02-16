from pickle import FALSE
from turtle import Turtle as Turtle

ALIGN = 'left'
FONT = ('Arial', 14, 'normal')
MOVE = False

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as highscore:
            self.high_score = int(highscore.read())
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(x=-290, y=280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=MOVE, align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(x = -60, y = 0)
    #     self.write("Game Over", align=ALIGN, font=FONT)
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as highscore:
                highscore.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()


