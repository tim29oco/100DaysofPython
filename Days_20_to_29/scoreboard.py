from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(x=-280, y=260)
        self.write(f"Score: {self.score}", font= FONT)
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", font= FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER. TOTAL POINTS {self.score}", align="center", font=FONT)

