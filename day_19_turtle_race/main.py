import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(
    "make your bet", "select your turtle color: \nred, green, pink, blue, orange, purple").lower()
colors = ["red", "green", "pink", "blue", "orange", "purple"]
v = -100
turtles = []
line = Turtle()
line.penup()
line.setposition(210, -210)
line.pendown()
line.setposition(210, 210)
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=v)
    turtles.append(new_turtle)
    v += 50
race_on = False
winner = ""
if user_bet:
    race_on = True
while race_on:
    for turtle in turtles:
        distance = random.randint(0, 10)
        turtle.fd(distance)
        pos_x = list(turtle.pos())[0]
        if pos_x > 220:
            race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                screen.textinput("You win", f"{user_bet} took first place.")
            else:
                screen.textinput("You lose", f"{winner} took first place.")

screen.exitonclick()
