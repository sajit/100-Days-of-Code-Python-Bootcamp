###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
from turtle import Turtle,Screen
import random
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append((color.rgb.r,color.rgb.g,color.rgb.b))

#print(rgb_colors)

timmy = Turtle()
timmy.pensize(20)
screen = Screen()
screen.colormode(255)
def paint():
    
    for i in range(0,10):
        for j in range(0,10):
            color = random.choice(rgb_colors)
            timmy.dot(20, color)
            timmy.penup()
            timmy.forward(50)

        timmy.backward(500)
        timmy.left(90)
        timmy.forward(50)
        timmy.right(90)  

timmy.penup()        
timmy.goto(-300,-300)
paint()
screen.exitonclick()
