from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        car = Turtle("square")
        car.shapesize(0.75, 1.5)
        car.color(random.choice(COLORS))
        car.penup()
        car.goto(260, random.randint(-250, 250))
        self.cars.append(car)

    def move(self, game):
        for car in self.cars:
            new_x = car.xcor() - 20
            car.goto(new_x, car.ycor())

    def speed_up(self):
        self.speed *= 0.9
        return self.speed
