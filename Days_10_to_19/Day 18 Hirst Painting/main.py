import colorgram
from turtle import  *
import random

turtle = Turtle()
screen = Screen()
turtle.hideturtle()
screen.colormode(255)
turtle.screen.title('Day 18 Hirst Painting')
x_cord = -220
y_cord = -200
turtle_speed = 0
number_of_colors = 20
image = 'image.jpg'
new_color_list = []
vertical_spacing_btwn_colors = 50

def start_position():
    turtle.penup()
    turtle.speed(turtle_speed)
    turtle.goto(x_cord, y_cord)

colors = colorgram.extract(image, number_of_colors)

for color in colors:
    rgb_color = color.rgb
    new_color_list.append((rgb_color.r, rgb_color.g, rgb_color.b))

start_position()
def draw_dots():
    for _ in range(0,10):
        left_to_right()
        move_up(x_cord=x_cord)

def left_to_right():
    for _ in range(0, 10):
        #Pick Random Color
        random_color_tuple = random.choice(new_color_list)
        turtle.pendown()

        turtle.dot(20, random_color_tuple)
        turtle.penup()
        turtle.forward(50)

def move_up(x_cord):
    #Intentionally Manipulating Global Variables
    global y_cord, vertical_spacing_btwn_colorss
    y_cord += vertical_spacing_btwn_colors
    turtle.goto(x_cord, y_cord)

draw_dots()

screen.exitonclick()
screen.mainloop()
