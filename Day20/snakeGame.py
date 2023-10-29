from scoreboard import Scoreboard
from turtle import Screen, Turtle
from snake import Snake
import time
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

game_status = True
snake = Snake()
food = Food()
scoreboard = Scoreboard()
head = snake.snake_parts[0]

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")


def food_collision():
    if head.distance(food) < 15:
        scoreboard.add_point()
        food.food_eaten()
        snake.extend_body()


def wall_collision():
    global game_status
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        game_status = False


def body_collision():
    global game_status
    for body_parts in snake.snake_parts[1:-1]:
        if head.distance(body_parts) < 10:
            game_status = False


while game_status:
    body_collision()
    wall_collision()
    food_collision()
    screen.update()
    time.sleep(0.1)
    snake.move()
scoreboard.game_over()

screen.exitonclick()
