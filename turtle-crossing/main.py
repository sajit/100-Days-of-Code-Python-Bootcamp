import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")
UPDATE_SPEED = 0.5

player = Player()
screen.onkey(player.move,"w")
screen.listen()

scoreboard = Scoreboard()
car_manager = CarManager(cor_width=600,cor_height=600)
game_is_on = True
while game_is_on:
    time.sleep(UPDATE_SPEED)
    if random.randint(1,11-scoreboard.level) < 3:
        car_manager.generate_car()
    car_manager.move_cars()
    screen.update()

    # if player reaches top
    if player.ycor() > 280:
        scoreboard.increase_level()
        player.refresh()

    for car in car_manager.get_cars():
        if car.distance(player) < 10:
            game_is_on = False

wwwwwscoreboard.game_over()
screen.update()
    

screen.exitonclick()
