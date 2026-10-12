from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__(shape="classic", undobuffersize=100, visible=True)
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.refresh()

    def increment(self):
        self.score += 1
        

    def refresh(self):
        self.clear()
        self.write(self.score,align="center",font=("Arial",20,"normal"))