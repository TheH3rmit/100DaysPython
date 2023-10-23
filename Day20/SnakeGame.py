from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)


starting_positions = [(0, 0), (-20, 0), (-40, 0)]
snake_parts = []

for x in starting_positions:
    part = Turtle("square")
    part.color("white")
    part.penup()
    part.setpos(x)
    snake_parts.append(part)

screen.update()

while True:
    screen.update()
    time.sleep(0.1)
    for i in range(len(snake_parts)-1,0,-1):
        new_x = snake_parts[i-1].xcor()
        new_y = snake_parts[i-1].ycor()
        snake_parts[i].goto(new_x,new_y)
    snake_parts[0].fd(20)

screen.exitonclick()
