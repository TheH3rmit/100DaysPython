from tkinter import *
from tkinter import ttk
from field import Field

root = Tk()
root.title('Minesweeper')
root.geometry('750x700')
# root.resizable(False, False)

# Style for
s = ttk.Style()
s.configure('score_frame.TFrame', background='green')
s.configure('play_frame.TFrame', background='red')
s.configure('debug_frame.TFrame', background='blue')
# Frames
score_frame = ttk.Frame(root, width=750, height=140, borderwidth=1, style='score_frame.TFrame')
score_frame.place(x=0, y=0)

play_frame = ttk.Frame(root, width=500, height=560, borderwidth=1, style='play_frame.TFrame')
play_frame.place(x=0, y=140)

debug_frame = ttk.Frame(root, width=250, height=560, borderwidth=1, style='debug_frame.TFrame')
debug_frame.place(x=500, y=140)

for x in range(6):
    for y in range(6):
        square = Field()
        square.create_btn(play_frame)
        square.field_btn.grid(column=x, row=y)

root.mainloop()
