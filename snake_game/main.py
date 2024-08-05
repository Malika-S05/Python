from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time

s = Screen()
s.setup(600, 600)
s.bgcolor("black")
s.title("My Snake Game")
s.tracer(0)
s.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")

is_on = True
while is_on:
    s.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase()
        snake.increase_size()
    if not snake.check_boundary():
        scoreboard.reset()
        snake.reset()
    for segments in snake.segment[1:]:
        if snake.head.distance(segments) < 10:
            scoreboard.reset()
            snake.reset()


s.exitonclick()

