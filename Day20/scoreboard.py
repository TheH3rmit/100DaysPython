from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.score_number = 0
        self.game_over_text = "GAME OVER"
        self.score_text = "Score: " + str(self.score_number)
        self.write(self.score_text, False, align="center", font=('Arial', 16, 'normal'))

    def add_point(self):
        self.score_number += 1
        self.show_score()

    def show_score(self):
        self.clear()
        self.score_text = "Score: " + str(self.score_number)
        self.write(self.score_text, False, align="center", font=('Arial', 16, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(self.game_over_text, False, align="center", font=('Arial', 16, 'normal'))
