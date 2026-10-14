from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto((0,0))
        self.orientation = random.randint(0,360)
        self.setheading(self.orientation)
        self.MOVE_DISTANCE = 20


    def refresh(self):
        self.penup()
        self.goto((0,0))
        self.orientation = random.randint(0,360)
        print(f"Ball orientation {self.orientation}")

    def move(self):
        self.forward(self.MOVE_DISTANCE)

    def hit_paddle(self, paddle, moving_right):
        paddle_center_y = paddle.segments[len(paddle.segments) // 2].ycor()
        paddle_half_height = 50
        hit_offset = (self.ycor() - paddle_center_y) / paddle_half_height
        hit_offset = max(-1, min(1, hit_offset))

        angle = hit_offset * 60
        if moving_right:
            heading = angle if angle >= 0 else 360 + angle
        else:
            heading = 180 - angle

        self.setheading(heading)


    def hit_wall(self):
        self.setheading((360 - self.heading()) % 360)



# if __name__ == "__main__":
#     ball = Ball()
