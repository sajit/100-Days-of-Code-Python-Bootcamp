FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"
STARTING_POSITION = (-280, 250)


class Scoreboard:
    def __init__(self):
        from turtle import Turtle

        self.level = 1
        self.pen = Turtle()
        self.pen.hideturtle()
        self.pen.penup()
        self.pen.goto(STARTING_POSITION)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.pen.clear()
        self.pen.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.pen.goto(0, 0)
        self.pen.write("GAME OVER", align="center", font=FONT)
