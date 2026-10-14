from turtle import Screen
from paddle import Paddle
from net import draw_net
from scoreboard import Scoreboard
from ball import Ball
import time

game_is_on = True

def setup_screen():
    screen = Screen()
    screen.setup(width=800,height=600)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)
    screen.listen()
    return screen
screen = setup_screen()

draw_net()

left_paddle = Paddle(-350)
left_player_score = Scoreboard((-100,250))
right_paddle = Paddle(350)
right_player_score = Scoreboard((100,250))

ball = Ball()

screen.onkey(left_paddle.up,"w")
screen.onkey(left_paddle.down,"s")

screen.onkey(right_paddle.up,"Up")
screen.onkey(right_paddle.down,"Down")

while game_is_on and left_player_score.score < 5 and right_player_score.score < 5:
    screen.update()
    time.sleep(0.1)
    ball.move()

    #detect collision with top or bottom wall
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.hit_wall()


    #detect collision with left paddle
    if ball.xcor() < -320 and left_paddle.catches_ball(ball):
        ball.hit_paddle()

    # detect collision with right paddle
    if ball.xcor() > 320 and right_paddle.catches_ball(ball):
        ball.hit_paddle()

    # detect miss


screen.exitonclick()
