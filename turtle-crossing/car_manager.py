import random
from turtle import Turtle
from car import Car
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self,cor_width,cor_height):
        self.level = 1
        self.height = cor_height
        self.width = cor_width
        self.cars = []

    def generate_car(self):
        car_x_cor = (int)(self.width/2)-10
        y_cor_limit = (int)(self.height/2)
                
        car_y_cor = random.randint(-y_cor_limit+50,y_cor_limit)
        car_color = random.choice(COLORS)
        print(f"Starting {car_x_cor},{car_y_cor} with color {car_color}")     
        car = Car(color=car_color,position=(car_x_cor,car_y_cor),move_distance=MOVE_INCREMENT)
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.move()

    def get_cars(self):
        return self.cars

    def remove_car(self, car):
        if car in self.cars:
            car.hideturtle()
            self.cars.remove(car)
