from turtle import Turtle
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
posn = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for p in posn:
            t = Turtle(shape="square")
            t.penup()
            t.color("yellow")
            t.goto(p)
            t.speed("fastest")
            self.segment.append(t)

    def move(self):
        for seg in range(len(self.segment) - 1, 0, -1):
            x = self.segment[seg - 1].xcor()
            y = self.segment[seg - 1].ycor()
            self.segment[seg].goto(x, y)
        self.segment[0].forward(MOVING_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def increase_size(self):
        t = Turtle(shape="square")
        t.penup()
        t.color("yellow")
        self.segment.append(t)

    def check_boundary(self):
        if self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 280 or self.head.ycor() < -280:
            return False
        else:
            return True

    def reset(self):
        for seg in self.segment:
            seg.goto(1800, 1800)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]
