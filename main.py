from turtle import Screen
from player import Player
from car_management import CarManagement
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.title("Turtle Car Race")

player = Player()
car_management = CarManagement()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()
    car_management.create_car()
    car_management.move()

    for car in car_management.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        car_management.level_up()
        scoreboard.update_score()


screen.exitonclick()
