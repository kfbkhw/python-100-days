from turtle import Turtle
ALIGNMENT = "center"
POS = 0, 270
CENTER = 0, 0
FONT = ("Courier", 24, "normal")
COLOR = "white"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color(COLOR)
        self.goto(POS)
        self.update()

    def new_score(self):
        self.score += 1
        self.clear()
        self.update()

    def update(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(CENTER)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
