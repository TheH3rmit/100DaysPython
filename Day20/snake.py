from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
snake_parts = []
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snake_parts = []
        self.create_body()

    def create_body(self):
        for x in STARTING_POSITIONS:
            part = Turtle("square")
            part.color("white")
            part.penup()
            part.setpos(x)
            self.snake_parts.append(part)

    def move(self):
        for i in range(len(snake_parts) - 1, 0, -1):
            new_x = snake_parts[i - 1].xcor()
            new_y = snake_parts[i - 1].ycor()
            snake_parts[i].goto(new_x, new_y)
        snake_parts[0].fd(MOVE_DISTANCE)
