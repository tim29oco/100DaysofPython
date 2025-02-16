from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.speed(1)
        self.goto(x=0,y=0)
        self.color("white")
        self.shape("circle")
        self.left(40)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.04

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x,y=new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        if self.move_speed > 0.02:
            self.move_speed *= 0.5

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.04
        self.bounce_x()


