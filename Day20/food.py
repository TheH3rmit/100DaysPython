import random
import turtle
from turtle import Turtle
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.food_eaten()

    def food_eaten(self):
        x_random = random.randint(-270,270)
        y_random = random.randint(-270, 270)
        self.goto(x_random,y_random)