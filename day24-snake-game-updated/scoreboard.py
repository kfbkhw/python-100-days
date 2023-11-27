from turtle import Turtle
ALIGNMENT = "center"
POS = 0, 270
CENTER = 0, 0
FONT = ("Courier", 24, "normal")
COLOR = "white"
with open("score_history.txt") as file:
    high_score = int(file.read())


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = high_score
        self.hideturtle()
        self.penup()
        self.color(COLOR)
        self.goto(POS)
        self.update()

    def new_score(self):
        self.score += 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        with open("score_history.txt", mode='w') as f:
            f.write(str(self.high_score))

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update()
