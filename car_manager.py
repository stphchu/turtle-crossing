from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.moving_speed = STARTING_MOVE_DISTANCE
        self.cars = []

    def make_car(self):
        car = Turtle("square")
        car.pu()
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(choice(COLORS))
        car.setpos(-280, randint(-250, 250))
        self.cars.append(car)

    def increase_speed(self):
        self.moving_speed += MOVE_INCREMENT

    def move_cars(self):
        for car in self.cars:
            car.fd(self.moving_speed)
