from turtle import Turtle
class Snake:

    def __init__(self):
        self.head = (20,0)
        self.tail = (-20,0)
        self.positions  = [self.head,(0,0),self.tail] 
        self.segments = []
        for i in range(0,len(self.positions)):
            snake_body = Turtle(shape="square")
            snake_body.color("white")
            position = self.positions[i]
            snake_body.penup()
            snake_body.goto(position)
            self.segments.append(snake_body)
        #self.current_direction = "right"
        
        


    def move(self,direction):
        if direction == "right":
            for i in range(len(self.segments)-1,0,-1):
                new_x = self.segments[i-1].xcor()
                new_y = self.segments[i-1].ycor()
                self.segments[i].goto(new_x,new_y)
            self.segments[0].forward(20)
        else:
            pass
   

        
