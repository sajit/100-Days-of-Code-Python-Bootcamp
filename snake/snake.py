from turtle import Turtle
class Snake:

    def __init__(self):
        self.head = (20,0)
        self.tail = (-20,0)
        self.size = 3
        

    def getHead(self):
        pass

    def draw(self):
        for i in range(0,self.size):
            snake_body = Turtle(shape="square")
            snake_body.color("white")
            snake_body.setpos(20-i*20,0)
        
