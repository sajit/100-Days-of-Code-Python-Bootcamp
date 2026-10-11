from turtle import Turtle
class Snake:

    def __init__(self):
        self.head = (20,0)
        self.tail = (-20,0)
        self.positions  = [self.head,(0,0),self.tail] 
        self.segments = []
        self.MOVE_DISTANCE = 20
        for i in range(0,len(self.positions)):
            self.add_segment(self.positions[i])

    def add_segment(self, position):
        snake_body = Turtle(shape="square")
        snake_body.color("white")
        snake_body.penup()
        snake_body.goto(position)
        self.segments.append(snake_body)
        
        

    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            new_x = self.segments[i-1].xcor()
            new_y = self.segments[i-1].ycor()
            self.segments[i].goto(new_x,new_y)
        self.segments[0].forward(self.MOVE_DISTANCE)

    def get_head(self):
        return self.segments[0]

    def up(self):
        self.segments[0].setheading(90)

    def down(self):
        self.segments[0].setheading(270)

    def right(self):
        self.segments[0].setheading(0)

    def left(self):
        self.segments[0].setheading(180)

    def extend(self):
        self.add_segment(self.segments[-1].position())
        
