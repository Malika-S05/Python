from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, posn):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(posn)

    def up(self):
        y = self.ycor()
        self.goto(self.xcor(), y + 20)

    def down(self):
        y = self.ycor()
        self.goto(self.xcor(), y - 20)