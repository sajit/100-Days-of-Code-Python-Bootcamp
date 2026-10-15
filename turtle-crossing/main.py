import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")

player = Player()
car_manager = CarManager(cor_width=600,cor_height=600)
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.generate_car()
    car_manager.move_cars()
    screen.update()

screen.exitonclick()
