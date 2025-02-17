from turtle import Screen as S
from turtle import Turtle as T
from paddle import Paddle as Paddle
from ball import Ball as Ball
from scoreboard import Scoreboard, player_2, player_1

import time

BALL_UP = 10
BALL_DOWN = -10

s = S()

s.setup(width=800, height=600)
s.bgcolor("black")
s.title("PONG - Timothy O'Connor",)
s.tracer(0)

r_position = (350,0)
l_position = (-350, 0)

r_paddle = Paddle(r_position)
l_paddle = Paddle(l_position)

s.listen()
s.onkey(r_paddle.up, key= "Up")
s.onkey(r_paddle.down, key="Down")
s.onkey(l_paddle.up, key= "w")
s.onkey(l_paddle.down, key="s")

ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    s.update()
    ball.move()
    if ball.ycor() >= 282 or ball.ycor() <= -282:
        ball.bounce_y()
    if (ball.distance(r_paddle) < 60 and ball.xcor() > 320
            or (ball.distance(l_paddle) < 60 and ball.xcor() < -320)):
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

s.exitonclick()
