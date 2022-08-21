import colorgram
import turtle as t
import random

# rgb_colors = []
# colors = colorgram.extract('day_18\image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)
color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]
turtle = t.Turtle()
screen = t.Screen()
turtle.penup()
turtle.speed("fastest")
turtle.hideturtle()
s = -100
turtle.setposition(s, s)
space = 50
size = 20
grid = 10
screen.colormode(255)
for _ in range(grid):
    for _ in range(grid):
        turtle.dot(20, random.choice(color_list))
        turtle.penup()
        turtle.fd(50)
    s += 50
    turtle.setposition(-100, s)

screen.exitonclick()
