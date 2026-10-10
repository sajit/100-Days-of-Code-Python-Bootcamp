from turtle import Screen
from snake import Snake
import time

def setup_screen():
    screen = Screen()
    screen.setup(600,600)
    screen.bgcolor("black")
    screen.title("Snake")
    screen.tracer(0)
    screen.listen()
    return screen

game_is_on = True
screen = setup_screen()
snake = Snake()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
while game_is_on:
    snake.move()
    screen.update()
    time.sleep(0.1)
screen.exitonclick()
