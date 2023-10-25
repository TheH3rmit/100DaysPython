from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
head = snake.snake_parts[0]


def up():
    head.setheading(90)


def down():
    head.setheading(270)


def right():
    head.setheading(0)


def left():
    head.setheading(180)


while True:
    screen.onkey(up, "w")
    screen.onkey(down, "s")
    screen.onkey(right, "d")
    screen.onkey(left, "a")
    screen.listen()
    screen.update()
    time.sleep(0.1)
    snake.move()

# screen.exitonclick()
