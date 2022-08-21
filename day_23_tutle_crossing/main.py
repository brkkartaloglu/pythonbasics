import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player1 = Player()
scoreboard1 = Scoreboard()
screen.listen()
screen.onkey(player1.run, "Up")
car = CarManager()


game_is_on = True
loop_counter = 0
loop_count = 4
game_speed = 5
while game_is_on:
    time.sleep(0.04*game_speed)
    if loop_counter % loop_count == 0:
        car.create_cars()
    car.move(game_is_on)
    screen.update()
    if player1.ycor() > 260:
        scoreboard1.level_up()
        player1.goto(0, -280)
        game_speed = car.speed_up()
        print(game_speed)
    for c in car.cars:
        if c.distance(player1) < 20:
            scoreboard1.game_over()
            game_is_on = False
screen.exitonclick()
