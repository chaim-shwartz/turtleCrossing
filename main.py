import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

score = 0
sum_cars = 20
cars = []
speed = 0.1
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
game_is_on = True
turtle = Player()
screen.onkeypress(turtle.move, "Up")
scoreb = Scoreboard()
while game_is_on:

    if len(cars) < sum_cars and len(cars) == 0 or cars[-1].xcor() < 250:
        car = CarManager()
        cars.append(car)
    if turtle.ycor() > 280:
        turtle.finish()
        score += 1
        if score>1:
            sum_cars=30
        speed *=0.9
        scoreb.score_update(score)
    for c in cars:
        if turtle.distance(c) < 55:
            if turtle.ycor() < c.ycor():
                if (turtle.ycor() * -1) - (c.ycor() * -1) < 22:
                    scoreb.game_over()
                    game_is_on = False
            elif (c.ycor() * -1) - (turtle.ycor() * -1) < 22:
                scoreb.game_over()
                game_is_on = False
    car.move(cars)
    time.sleep(speed)
    screen.update()

screen.exitonclick()
