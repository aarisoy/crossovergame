import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Crossover Game by Alpay")
screen.tracer(0)

# Create needed objects
p1 = Player()
cars = CarManager()
score = Scoreboard()

# Setup key configuration
screen.listen()
screen.onkey(p1.moveUp, "w")    
screen.onkey(p1.moveLeft, "a")    
screen.onkey(p1.moveRight, "d") 

# Global variables to be used
createCounter = 0
game_is_on = True
isSpeedUpdateNeeded = False

while game_is_on:
    time.sleep(0.2)
    screen.update()
    
    # To not spam new car creation counter is used
    createCounter += 1
    if createCounter%12 == 0:
        cars.createRandomCar()

    # Check the car hit the turtle or not
    for car_index in cars.car_list:
        if car_index.distance(p1) < 20:
            game_is_on = False

    # Check player position to finish line
    if p1.ycor() >= 290:
        score.addScore()
        isSpeedUpdateNeeded = True # Whenever player hits the score update the speed
        p1.refresh()
    
    if isSpeedUpdateNeeded == True:
        isSpeedUpdateNeeded = cars.updateSpeed(isSpeedUpdateNeeded)

    cars.moveCars()

screen.exitonclick()