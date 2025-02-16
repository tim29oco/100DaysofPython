from turtle import Turtle as T
from turtle import Screen as S
import random

s = S()
s.setup(width=500,height=400)
s.bgcolor("gray")
user_bet = s.textinput(title="Make your bet", prompt="Which Turtle will win the race?! Enter a Color ROYGBP").lower()
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []

y_cord = -80
for _ in colors:
    new_turtle = T(shape="turtle")
    new_turtle.color(_)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_cord)
    y_cord += 30
    all_turtles.append(new_turtle)

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 200:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won. The {winner} turtle is the winner!")
            else:
                print(f"You've lost. The {winner} turtle is the winner!")
        rand_distance = random.randint(0, 15)
        turtle.forward(rand_distance)


s.exitonclick()
