from turtle import Turtle as T

UP = 90
DOWN = 270
MOVE_DISTANCE = 20

class Paddle(T):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.setup_paddle(position)

    def setup_paddle(self, position):
        self.setheading(UP)
        self.goto(position)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.forward(MOVE_DISTANCE * -1)