import time
from random import randint
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")

turtle = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(turtle.move_up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()
    if turtle.ycor() >= 280:
        scoreboard.level_up()
        turtle.reset_pos()
        car_manager.increase_speed()
    for car in car_manager.cars:
        if turtle.distance(car.pos()) < 25:
            scoreboard.game_over()
            game_is_on = False
    random_num = randint(1, 6)
    if random_num == 6:
        car_manager.make_car()

screen.exitonclick()
