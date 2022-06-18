from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        super().__init__()
        self.car_list = []
        self.movedist = MOVE_INCREMENT
        self.createRandomCar()

    def createRandomCar(self):
        new = Turtle()
        new.color(random.choice(COLORS))        
        new.penup()
        new.shape("square")
        new.shapesize(stretch_wid=1, stretch_len=2)
        new.goto(x=280, y=random.randint(-230, +250))
        self.car_list.append(new)        

    def moveCars(self):
        for car_index in range(0, len(self.car_list)):
            self.car_list[car_index].goto(self.car_list[car_index].xcor() - self.movedist, self.car_list[car_index].ycor())

    def updateSpeed(self, flag):
        self.movedist += MOVE_INCREMENT
        flag = False
        return flag