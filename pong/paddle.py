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

    def up(self):
        if self.segments[0].ycor() > 280:
            return
        for segment in self.segments:
            segment.sety(segment.ycor() + MOVE_DISTANCE)

    def down(self):
        if self.segments[len(self.segments)-1].ycor() < -280:
            return
        for segment in self.segments:
            segment.sety(segment.ycor() - MOVE_DISTANCE)

