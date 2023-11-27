
# import colorgram

# colors = colorgram.extract('image.jpg', 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_list.append((r, g, b))

import turtle
import random

color_list = [(249, 249, 249), (249, 247, 248), (202, 172, 108), (224, 230, 236), (238, 245, 243), (153, 180, 196), (152, 186, 174), (193, 161, 176), (214, 204, 113), (208, 179, 197), (175, 188, 212), (161, 213, 187), (164, 202, 212), (114, 122, 185), (214, 181, 180), (182, 161, 67), (98, 98, 98), (44, 44, 44), (103, 101, 102), (197, 207, 44), (42, 40, 41), (90, 92, 91), (106, 111, 145), (20, 22, 21)]
color_turtle = turtle.Turtle()
color_turtle.screen.colormode(255)
color_turtle.hideturtle()
color_turtle.penup()
color_turtle.speed(10)
color_turtle.backward(200)
color_turtle.right(90)
color_turtle.forward(200)
color_turtle.left(90)
starting_point = color_turtle.pos()

def one_row(number_of_dots):
    for i in range(number_of_dots):
        color_turtle.dot(20, random.choice(color_list))
        color_turtle.forward(50)


def square_dot_drawing(column, row):
    color_turtle.goto(starting_point)
    for i in range(column):
        one_row(row)
        color_turtle.goto(starting_point)
        color_turtle.left(90)
        color_turtle.forward(50+50*i)
        color_turtle.right(90)


square_dot_drawing(10, 10)

turtle.exitonclick()
