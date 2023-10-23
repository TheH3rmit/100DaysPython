from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")


starting_positions = [(0, 0), (-20, 0), (-40, 0)]
snake_parts = []

for x in starting_positions:
    part = Turtle("square")
    part.color("white")
    part.penup()
    part.setpos(x)

while True:
    for i in snake_parts:
        i.fd(20)

screen.exitonclick()
