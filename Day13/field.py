from tkinter import Button, Label


class Field:
    all = []
    bomb_count = 10
    field_count = 25

    def __int__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.x = x
        self.y = y
        self.field_btn = None
        self.flag_field = None

        Field.all.append(self)

    def create_btn(self, location):
        btn = Button(location, text="filed", width=10, height=5)
        self.field_btn = btn
