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

    def hit_paddle(self):
        self.setheading((180 - self.heading()) % 360)


    def hit_wall(self):
        self.setheading((360 - self.heading()) % 360)



# if __name__ == "__main__":
#     ball = Ball()
