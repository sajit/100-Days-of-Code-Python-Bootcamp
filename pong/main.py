from turtle import Screen, Turtle
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
    if ball.xcor() < -320:
        if left_paddle.catches_ball(ball):
            ball.hit_paddle(left_paddle, moving_right=True)
        else:
            ball.refresh()
            right_player_score.increment()
            right_player_score.refresh()

    # detect collision with right paddle
    if ball.xcor() > 320:
        if right_paddle.catches_ball(ball):
            ball.hit_paddle(right_paddle, moving_right=False)
        else:
            ball.refresh()
            left_player_score.increment()
            left_player_score.refresh()


winner = "Left" if left_player_score.score > right_player_score.score else "Right"
game_over_message = Turtle()
game_over_message.hideturtle()
game_over_message.penup()
game_over_message.color("white")
game_over_message.goto(0, 0)
game_over_message.write(
    f"Game Over\n{winner} player wins!",
    align="center",
    font=("Arial", 24, "bold"),
)
screen.update()


screen.exitonclick()
