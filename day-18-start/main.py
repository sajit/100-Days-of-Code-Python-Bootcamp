from turtle import Turtle
from turtle import Screen

screen = Screen()
image_name = "/Users/sajit/PycharmProjects/100-Days-of-Code-Python-Bootcamp/day-18-start/leonardo.png"
screen.register_shape(image_name)
screen.screensize(200,200)
leonardo = Turtle()
leonardo.shape(image_name)


warden_image_name = "/Users/sajit/PycharmProjects/100-Days-of-Code-Python-Bootcamp/day-18-start/warden.png"
screen.register_shape(warden_image_name)

warden = Turtle()
warden.shape(warden_image_name)
warden.goto(100,100)

def draw_square(size,turtle):
    turtle.forward(size)
    turtle.rt(90)
    turtle.forward(size)
    turtle.rt(90)
    turtle.forward(size)
    turtle.rt(90)
    turtle.forward(size)

#draw_square(100,leonardo)
def dashed_line(turtle):
    for i in range(1,10):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()

#dashed_line(leonardo)

def draw_shapes():
    turtle = Turtle()
    for i in range(4,7):
        angle = 360/i
        print(f"i={i} , angle={angle}")
        for s in range(0,i):
            print(f"s={s},i={i}")
            turtle.forward(100)
            turtle.rt(angle)


#draw_shapes()

screen.exitonclick()

