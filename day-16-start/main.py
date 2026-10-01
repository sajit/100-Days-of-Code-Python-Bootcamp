print("Jesus is Lord")
import turtle

screen = turtle.Screen()
screen.register_shape("michelangelo", "/Users/sajit/PycharmProjects/100-Days-of-Code-Python-Bootcamp/day-16-start/michelangelo.png")
screen.register_shape("leonardo", "/Users/sajit/PycharmProjects/100-Days-of-Code-Python-Bootcamp/day-16-start/leonardo.png")
leonardo = turtle.Turtle()
leonardo.shape("leonardo")

michelangelo = turtle.Turtle()
michelangelo.shape("michelangelo")

screen.screensize(150, 150)
leonardo.goto(50, 50)
michelangelo.forward(20)
screen.exitonclick()
