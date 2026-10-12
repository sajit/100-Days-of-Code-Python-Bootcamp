from turtle import Turtle

MOVE_DISTANCE = 20
class Paddle:

    def __init__(self,xcor):
        self.segments = []
        for position in [(xcor,20),(xcor,0),(xcor,-20)]:
            self.segments.append(self.add_segment(position=position))


    def add_segment(self,position):
        paddle_segment = Turtle(shape="square")
        paddle_segment.color("white")
        paddle_segment.penup()
        paddle_segment.goto(position)
        return paddle_segment

        
    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            new_x = self.segments[i-1].xcor()
            new_y = self.segments[i-1].ycor()
            self.segments[i].goto(new_x,new_y)
        self.segments[0].forward(self.MOVE_DISTANCE)


    def up(self):
        self.segments[0].setheading(90)

    def down(self):
        self.segments[0].setheading(270)
