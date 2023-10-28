import random
from turtle import Turtle
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        x_random = random.randint(-290,290)
        y_random = random.randint(-290, 290)
        self.goto(x_random,y_random)
