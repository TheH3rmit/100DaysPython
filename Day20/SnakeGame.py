from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")

head = Turtle("square")
head.color("white")
head_position = head.pos()

body1 = Turtle("square")
body1.color("white")
body1.penup()
body1.setpos(x=head_position[0] - 20, y=head_position[0])

body2 = Turtle("square")
body2.color("white")
body2.penup()
body2.setpos(x=head_position[0] - 40, y=head_position[0])

snake_parts = [head, body1, body2]

screen.exitonclick()
