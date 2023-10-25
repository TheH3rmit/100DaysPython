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



while True:
    screen.onkey(snake.up, "w")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.right, "d")
    screen.onkey(snake.left, "a")
    screen.listen()
    screen.update()
    time.sleep(0.1)
    snake.move()

# screen.exitonclick()
