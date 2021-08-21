import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
cars = []
player = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move_up, 'Up')

game_is_on = True
count = 0
n = 5
while game_is_on:

    time.sleep(0.1)

    car = CarManager()
    if count % n == 0:
        cars.append(car)
    for i in range(len(cars)):
        cars[i].move()
    screen.update()

    if player.finish():
        player.reset_pos()
        screen.update()
        cars[-1].inc_speed()
        scoreboard.inc_score()
        screen.update()
        time.sleep(1)
        player.reset_pos()

    for i in range(len(cars)):
        posi = cars[i].car_pos()
        if player.distance(posi) < 30 and posi[1] - 15 < player.ycor() < posi[1] + 15:
            game_is_on = False
            scoreboard.game_over()

    count += 1

screen.exitonclick()
