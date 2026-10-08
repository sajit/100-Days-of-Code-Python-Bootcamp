from turtle import Screen
from snake import Snake

def setup_screen():
    screen = Screen()
    screen.setup(600,600)
    screen.bgcolor("black")
    screen.title("Snake")
    return screen


screen = setup_screen()
snake = Snake()
snake.draw()
screen.exitonclick()
