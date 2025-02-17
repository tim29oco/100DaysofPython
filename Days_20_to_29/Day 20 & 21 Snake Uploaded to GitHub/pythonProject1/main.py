from inspect import trace
from turtle import Screen, Turtle
from snake import Snake as Snake
from food import Food as Food
from scoreboard import Scoreboard as Scoreboard
import time

s = Screen()
s.setup(width=600, height=600)
s.bgcolor('black')
s.title(titlestring="SNAKEEEEEEE")
s.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
border = Turtle()

s.listen()
s.onkey(snake.up,key="Up")
s.onkey(snake.down,key="Down")
s.onkey(snake.left,key="Left")
s.onkey(snake.right,key="Right")

border.penup()
border.speed(0)
border.color('white')
border.goto(-280, 280)
border.pendown()

for _ in range(4):
    border.forward(560)
    border.right(90)

border.hideturtle()

snake_speed = 0.05

game_is_on = True
while game_is_on:
    s.update()
    time.sleep(snake_speed)
    snake.move()

    #Detect Collision with Food.
    if snake.head.distance(food) <= 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall
    if (snake.head.xcor() >= 290
            or snake.head.xcor() <= -290
            or snake.head.ycor() >= 290
            or snake.head.ycor() <= -290):
        scoreboard.reset()
        snake.reset()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <= 10:
            scoreboard.reset()
            snake.reset()

s.exitonclick()