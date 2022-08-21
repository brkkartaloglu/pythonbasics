import turtle as t
import random


timmy_the_turtle = t.Turtle()
screen = t.Screen()

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.setheading(0)
timmy_the_turtle.left(90)

for i in range(10):
    timmy_the_turtle.pendown()
    timmy_the_turtle.color("red")
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)

timmy_the_turtle.setheading(0)
timmy_the_turtle.clear()
timmy_the_turtle.pendown()
i = 4
while i <= 10:
    r = random.random()
    g = random.random()
    b = random.random()
    for _ in range(i):
        timmy_the_turtle.pencolor(r, g, b)
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(360/i)
    i += 1
timmy_the_turtle.setheading(0)
timmy_the_turtle.clear()
timmy_the_turtle.pensize(10)


def get_random_move():
    r = random.randint(0, 3)
    if r == 0:
        return timmy_the_turtle.forward(50)
    elif r == 1:
        return timmy_the_turtle.bk(50)
    elif r == 2:
        return timmy_the_turtle.right(90)
    elif r == 3:
        return timmy_the_turtle.left(90)


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
timmy_the_turtle.home()
for _ in range(100):
    timmy_the_turtle.color(random.choice(colours))
    get_random_move()

timmy_the_turtle.home()
heading = 0
timmy_the_turtle.speed(0)
timmy_the_turtle.pensize(0)
while heading <= 360:
    r = random.random()
    g = random.random()
    b = random.random()
    timmy_the_turtle.pencolor(r, g, b)
    timmy_the_turtle.setheading(heading)
    timmy_the_turtle.circle(150)
    heading += 5

screen.exitonclick()
