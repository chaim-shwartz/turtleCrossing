import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import *
import random


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(315, random.randint(-250, 250))
        self.addCar()

    def addCar(self):
        # time.sleep(0.1)
        self.setheading(180)
        self.shape("square")
        self.shapesize(1, 3)
        self.color(random.choice(COLORS))
        self.goto(315, random.randint(-250, 250))

    def move(self,cars):
        for car in cars:
            car.forward(10)
            if car.xcor() < -310:
                cars.remove(car)
                car.hideturtle()

        #     car.goto(310,random.randint(-300,300))
