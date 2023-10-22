from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setpos(0, 0)
        self.x = 8
        self.y = 8
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.x, self.ycor() + self.y)

    def bounce(self):
        self.y *= -1

    def paddle_bounce(self):
        self.x *= -1
        self.move_speed *= 0.7

    def collision(self):
        if self.xcor() > 380:
            return "l_score"
        if self.xcor() < -380:
            return "r_score"

    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce()
