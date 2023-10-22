from turtle import Turtle

STARTING_NUMBER = 3
STARTING_POINT = 0
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.snake = []
        self.number = STARTING_NUMBER
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for i in range(self.number):
            segment = Turtle(shape="square")
            segment.penup()
            segment.color("white")
            segment.setpos((STARTING_POINT - 20 * i), 0)
            self.snake.append(segment)

    def reset_snake(self):
        for segment in self.snake:
            segment.goto(1000, 1000)
        self.snake.clear()
        self.snake = []
        self.number = STARTING_NUMBER
        self.create_snake()
        self.head = self.snake[0]

    def move(self):
        for i in range(len(self.snake)-1, 0, -1):
            new_x = self.snake[i-1].xcor()
            new_y = self.snake[i-1].ycor()
            self.snake[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def extend(self):
        self.number += 1
        segment = Turtle(shape="square")
        segment.penup()
        segment.color("white")
        self.snake.append(segment)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
