from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        super().__init__()
        self.cars = []
        self.createRandomCar()

    def createRandomCar(self):
        new = Turtle()
        new.color(random.choice(COLORS))        
        new.penup()
        new.shape("square")
        new.shapesize(stretch_wid=1, stretch_len=2)
        new.goto(x=280, y=random.randint(-230, +250))
        self.cars.append(new)        

    def moveCars(self):
        for car_index in range(0, len(self.cars)):
            self.cars[car_index].goto(self.cars[car_index].xcor() - MOVE_INCREMENT, self.cars[car_index].ycor())