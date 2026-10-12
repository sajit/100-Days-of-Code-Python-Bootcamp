from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto((0,0))
        self.orientation = 1
        self.MOVE_DISTANCE = 20
        self.direction = None


    def refresh(self):
        self.penup()
        self.goto((0,0))
        self.orientation = -1 if random.randint(0,1) == 0 else 1
        angle = random.randint(-90,90)
        if self.orientation == -1:
            self.direction = 180 - angle
        else:
            self.direction = 0 + angle
        self.setheading(self.direction)

    def move(self):
        new_x = self.xcor() + self.MOVE_DISTANCE*self.orientation
        new_y = self.ycor()

