from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.goto(-230, 250)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level:{self.level}", align="center", font=FONT)

    def end_game(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update()