from turtle import Turtle
import random

COLOR = ["red", 'blue', 'green', 'yellow', 'orange', 'violet']
MOVING_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManagement:

    def __init__(self):
        self.all_cars = []
        self.move_speed = MOVING_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLOR))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.move_speed)

    def level_up(self):
        self.move_speed += MOVE_INCREMENT









