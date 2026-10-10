from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,280)
        self.refresh()

    def increment(self,amount):
        self.score += amount
        print(f"Score={self.score}")

    def refresh(self):
        self.clear()
        self.write(self.score,align="center",font=("Arial",12,"normal"))