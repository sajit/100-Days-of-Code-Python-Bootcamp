from turtle import Turtle,Screen

turtle = Turtle()
screen = Screen()

screen.screensize(100,100)
def draw_circle():
    turtle.circle(50.0)

def draw_spirograph():
    count = 0
    while count < 360:
        draw_circle()
        turtle.rt(10.0)
        count += 10

#draw_circle()
draw_spirograph()

screen.exitonclick()
