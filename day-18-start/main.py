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

# warden = Turtle()
# warden.shape(warden_image_name)
# warden.goto(10,10)

def draw_square(size,turtle):
    turtle.forward(size)
    turtle.rt(90)
    turtle.forward(size)
    turtle.rt(90)
    turtle.forward(size)
    turtle.rt(90)
    turtle.forward(size)

draw_square(100,leonardo)
screen.exitonclick()

