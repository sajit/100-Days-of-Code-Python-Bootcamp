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
        self.current_high_score = self.get_current_high_score()

    def increment(self,amount):
        self.score += amount
        print(f"Score={self.score}")

    def refresh(self):
        self.clear()
        self.write(self.score,align="center",font=("Arial",12,"normal"))


    def get_current_high_score(self):
        high_score = None
        try:
            # Use 'with' so the file closes automatically even if an error occurs
            with open("scores/highscore.txt", "r", encoding="utf-8") as file:
                high_score = file.read()

        except FileNotFoundError:
            print("Error: The file does not exist.")
            high_score = 0
        return (int)(high_score)

    def get_current_score(self):
        return self.score
    
    def write_high_score(self,high_score):
        with open("scores/highscore.txt", "w", encoding="utf-8") as file:
            file.write(str(high_score))