import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move()
    for c in car.all_cars:
        if player.distance(c) < 20:
            scoreboard.end_game()
            game_is_on = False
    if player.ycor() > 280:
        scoreboard.increase_level()
        player.reset()
        car.increase_speed()


screen.exitonclick()