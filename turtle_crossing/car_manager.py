from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []

    def create_cars(self):
        i = randint(1, 6)
        if i == 1:
            new = Turtle("square")
            new.color(choice(COLORS))
            new.penup()
            new.shapesize(1, 2)
            y = randint(-250, 250)
            new.goto(300, y)
            self.all_cars.append(new)

    def move(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT


