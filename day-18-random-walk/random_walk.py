from turtle import Turtle,Screen
import random
colors = ["red","green","blue","yellow","pink","purple"]

def get_random_color():
    return random.choice(colors)

def get_distance():
    return random.randint(1,25)

def random_walk():
    turtle = Turtle()
    turtle.pensize(10)
    for i in range(0,50):
        distance = get_distance()
        turtle.pencolor(get_random_color())
        turtle.forward(distance=distance)
        flip_for_direction = random.choice([0,1])
        if flip_for_direction == 0: #turn left
            turtle.lt(90)
        else:
            turtle.rt(90)


screen = Screen()
screen.screensize(200,200)

random_walk()

screen.exitonclick()
