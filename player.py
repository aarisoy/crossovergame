from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

UP = 90

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("green")
        self.shape("turtle")
        self.goto(0,-280)
        self.setheading(UP)
    
    def moveUp(self):
        self.setheading(UP)
        self.forward(MOVE_DISTANCE)
    
    def moveLeft(self):
        self.goto(self.xcor() - MOVE_DISTANCE, self.ycor())
        
    def moveRight(self):
        self.goto(self.xcor() + MOVE_DISTANCE, self.ycor())
        
    