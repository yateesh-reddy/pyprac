from tkinter import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def draw_point(canvas, point):
    canvas.create_oval(
        point.x - 2, point.y - 2,
        point.x + 2, point.y + 2,
        fill="black"
    )

root = Tk()

canvas = Canvas(root, width=300, height=200)
canvas.pack()

p = Point(100, 80)
draw_point(canvas, p)

root.mainloop()