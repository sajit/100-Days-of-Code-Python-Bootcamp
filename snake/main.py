from turtle import Screen
from snake import Snake
import time

def setup_screen():
    screen = Screen()
    screen.setup(600,600)
    screen.bgcolor("black")
    screen.title("Snake")
    screen.tracer(0)
    return screen

game_is_on = True
screen = setup_screen()
snake = Snake()
while game_is_on:
    snake.move("right")
    screen.update()
    time.sleep(1)
screen.exitonclick()
