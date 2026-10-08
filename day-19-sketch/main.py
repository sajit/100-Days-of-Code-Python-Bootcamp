from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()

screen.listen()
def clear():
    tim.clear()
    tim.penup()
    tim.home()
screen.onkey(lambda: tim.forward(10),"w")
screen.onkey(lambda: tim.backward(10),"s")
screen.onkey(lambda: tim.rt(90),"d")
screen.onkey(lambda: tim.lt(90),"a")
screen.onkey(clear,"c")
screen.exitonclick()