from turtle import Screen
from paddle import Paddle
from net import draw_net
from scoreboard import Scoreboard
import time

game_is_on = True

def setup_screen():
    screen = Screen()
    screen.setup(600,600)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)
    screen.listen()
    return screen
screen = setup_screen()

draw_net()

left_paddle = Paddle(-200)
left_player_score = Scoreboard((-100,250))
right_paddle = Paddle(200)
right_player_score = Scoreboard((100,250))

screen.onkey(left_paddle.up,"w")
screen.onkey(left_paddle.down,"s")

screen.onkey(right_paddle.up,"Up")
screen.onkey(right_paddle.down,"Down")

while game_is_on:
    screen.update()
    time.sleep(0.1)


screen.exitonclick()
