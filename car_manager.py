from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car = []
        self.create()

    def create(self):
        col = random.choice(COLORS)
        y = random.uniform(-200, 200)
        for i in range(3):
            new = Turtle(shape='square')
            new.color(col)
            new.penup()
            new.goto(310 + i*20, y)
            new.setheading(180)
            self.car.append(new)

    def move(self):
        for i in range(3):
            self.car[i].fd(STARTING_MOVE_DISTANCE)

    def inc_speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT

    def clear_car(self):
        for i in range(3):
            self.car[i].hideturtle()

    def car_pos(self):
        return self.car[1].pos()
