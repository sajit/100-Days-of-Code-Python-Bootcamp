from turtle import Turtle

class Car(Turtle):

    def __init__(self,color,position,move_distance):
        super().__init__(shape="square")
        self.color = color
        self.setheading(180)
        self.penup()
        self.goto(position)
        self.move_distance = move_distance

    def move(self):
        self.forward(self.move_distance)