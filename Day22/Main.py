from tkinter import *
from tkinter import ttk

root = Tk()
root.title("PONG GAME")
root.geometry("1200x800+100+100")

#TODO rewrite into OOP way
#Window parameters
window_width = 1200
window_height = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

root.resizable(False, False)

root.mainloop()
