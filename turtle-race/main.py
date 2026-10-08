from turtle import Turtle, Screen
import random
screen = Screen()

# Define the TMNT team colors and their starting Y-coordinates
turtles = [("blue", 0), ("red", 50), ("orange", 100), ("yellow", 150)]
tmnt = []
for color, y_pos in turtles:
    t = Turtle(shape="turtle")
    t.color(color)
    t.penup()
    t.setpos(0, y_pos)
    tmnt.append(t)

def draw_finish():
    t = Turtle()
    # 1. Lift the pen so it doesn't draw while moving to the start position
    t.penup()
    t.goto(250, -250)  # Start at the bottom (X=0, Y=-150)

    # 2. Put the pen down and move straight up along the Y-axis
    t.pendown()
    t.goto(250, 250) 


def race(user_guess):
    is_finish = False
   
    winner_color = None
    while not is_finish:
        t = random.choice(tmnt)
        print(f"Turtle chosen {t.color()[0]}")
        t.forward(10)
        if t.pos()[0] >= 250:
            is_finish = True
            winner_color = t.color()[0]
    print(f"Winner is {winner_color}. You chose {user_guess}")
    if user_guess == winner_color:
        print("You won")
    else:
        print("You lose")
# 1. Display the text input box
guess = screen.textinput("Welcome", "Pick a color")

draw_finish()
race(user_guess=guess)
screen.exitonclick()