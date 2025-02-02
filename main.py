import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.move_cars()

    if player.player_in_the_edge():
        player.reset_position()
        car_manager.speed_up()
        scoreboard.increase_level()

    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
