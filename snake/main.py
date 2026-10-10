from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
SLEEP_TIME=1

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
food = Food()
scoreboard = Scoreboard()
while game_is_on:
    screen.update()
    time.sleep(SLEEP_TIME)
    snake.move()
    #Detect collision with food
    if snake.get_head().distance(food) < 15:
        
        food.refresh()
        scoreboard.increment(int(10/SLEEP_TIME))
        scoreboard.refresh()
        SLEEP_TIME = max((SLEEP_TIME-0.2),0.1)
        print(f"Collision. New speed {SLEEP_TIME}")
        # TODO increase size

screen.exitonclick()
