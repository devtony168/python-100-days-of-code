# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)

### Requirements: 10 x 10 dots, spot is 20 in size, space is 50 paces

from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)
# screen.setup(500, 500)  # screen-size for testing purposes

color_list = [(57, 106, 148), (224, 201, 110), (133, 85, 59), (222, 142, 65), (196, 145, 171), (234, 225, 203),
              (144, 179, 203), (138, 82, 105), (210, 91, 67), (187, 79, 120), (134, 182, 136), (69, 104, 89),
              (236, 223, 231), (65, 155, 90), (133, 133, 75), (49, 155, 194), (183, 192, 201), (214, 178, 191),
              (22, 68, 112), (21, 59, 95), (175, 202, 181), (114, 124, 150), (227, 176, 167), (158, 205, 214),
              (70, 59, 48), (72, 65, 53), (124, 45, 40), (110, 48, 58)]

tim.penup()
tim.hideturtle()
tim.speed("fastest")
start_y = -230  # for screen-size: 500 x 500


def draw_spots_per_line():
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)


for _ in range(10):
    tim.goto(-230, start_y)
    draw_spots_per_line()
    start_y += 50   # jump to next line

screen.exitonclick()
