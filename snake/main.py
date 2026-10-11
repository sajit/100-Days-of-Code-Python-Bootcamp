from turtle import Screen, Turtle
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

def game_over():
    game_is_on = False
    game_over = Turtle()
    game_over.color("white")
    game_over.write("Game Over!",align="center",font=("Arial",12,"normal"))
    return game_is_on

while game_is_on:
    screen.update()
    time.sleep(SLEEP_TIME)
    snake.move()
    #Detect collision with food
    snake_head = snake.get_head()
    if snake_head.distance(food) < 15:
        
        food.refresh()
        scoreboard.increment(int(10/SLEEP_TIME)+10*len(snake.segments))
        scoreboard.refresh()
        SLEEP_TIME = max((SLEEP_TIME-0.2),0.1)
        snake.extend()
        print(f"Collision. New speed {SLEEP_TIME}. {len(snake.segments)}")

    #Detect collision with wall
    if snake_head.xcor() > 280 or snake_head.xcor() < -280 or snake_head.ycor() > 280 or snake_head.ycor() < -280:
        game_is_on = game_over()

    #Detect collision with tail
    for i in range(1,len(snake.segments)):
        segment = snake.segments[i]
        if snake_head.distance(segment) < 10:
            print("Collision with tail")
            game_is_on = game_over()
        
screen.exitonclick()
