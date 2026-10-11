from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,position):
        super().__init__(shape="square")
        self.color("white")
        self.segments = []
        self.goto(position)

