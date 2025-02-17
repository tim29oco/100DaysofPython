from turtle import Turtle as Turtle
import random

FOOD_LOC = (-280, 280)

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('cyan')
        self.speed('fastest')
        random_x = random.randint(*FOOD_LOC)
        random_y = random.randint(*FOOD_LOC)
        self.goto(x= random_x, y=random_y)
        self.refresh()

    def refresh(self):
        random_x = random.randint(*FOOD_LOC)
        random_y = random.randint(*FOOD_LOC)
        self.goto(x=random_x, y=random_y)