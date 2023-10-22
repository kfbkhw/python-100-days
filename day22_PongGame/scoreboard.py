from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_point = 0
        self.r_point = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 210)
        self.write(self.l_point, align="center", font=("Ariel", 80, "normal"))
        self.goto(0, 220)
        self.write(":", align="center", font=("Ariel", 80, "normal"))
        self.goto(100, 210)
        self.write(self.r_point, align="center", font=("Ariel", 80, "normal"))

    def l_score(self):
        self.l_point += 1
        self.update_score()

    def r_score(self):
        self.r_point += 1
        self.update_score()
