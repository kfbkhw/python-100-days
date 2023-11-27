from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):

    def __init__(self, level):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(280, random.randint(-260, 260))
        self.move_speed = STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * (level - 1))

    def move(self, level):
        self.move_speed = STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * (level - 1))
        self.goto(self.xcor() - self.move_speed, self.ycor())
