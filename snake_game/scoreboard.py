from turtle import Turtle


FONT = ('courier', 30, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as file:
            self.HighScore = int(file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore {self.HighScore}", align="center", font=FONT)

    def increase(self):
        self.score += 1
        self.update()
    # def end_game(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER")

    def reset(self):
        if self.score > self.HighScore:
            self.HighScore = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.HighScore))
        self.score = 0
        self.update()
