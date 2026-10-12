from turtle import Turtle

def draw_net():
    net = Turtle()
    net.hideturtle()
    net.color("white")
    net.penup()
    net.goto(0, 280)
    net.setheading(270)  # face down

    for _ in range(30):
        net.pendown()
        net.forward(10)
        net.penup()
        net.forward(10)

