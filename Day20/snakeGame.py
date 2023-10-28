import turtle
from turtle import Screen
from snake import Snake
import time
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
head = snake.snake_parts[0]

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")


def food_collision():
    if head.distance(food) < 15:
        print("eaten")
        food.food_eaten()


while True:
    food_collision()
    screen.update()
    time.sleep(0.1)
    snake.move()

# screen.exitonclick()
