from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snake_parts = []
        self.create_body()

    def create_body(self):
        for position in STARTING_POSITIONS:
            self.add_body(position)

    def add_body(self, position):
        part = Turtle("square")
        part.color("white")
        part.penup()
        part.setpos(position)
        self.snake_parts.append(part)

    def extend_body(self):
        position_last_part = self.snake_parts[-1].pos()
        self.add_body(position_last_part)

    def move(self):
        for i in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[i - 1].xcor()
            new_y = self.snake_parts[i - 1].ycor()
            self.snake_parts[i].goto(new_x, new_y)
        self.snake_parts[0].fd(MOVE_DISTANCE)

    def up(self):
        if self.snake_parts[0].heading() != DOWN:
            self.snake_parts[0].setheading(UP)

    def down(self):
        if self.snake_parts[0].heading() != UP:
            self.snake_parts[0].setheading(DOWN)

    def right(self):
        if self.snake_parts[0].heading() != LEFT:
            self.snake_parts[0].setheading(RIGHT)

    def left(self):
        if self.snake_parts[0].heading() != RIGHT:
            self.snake_parts[0].setheading(LEFT)
