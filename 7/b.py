from tkinter import *

class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

def draw_circle(canvas, c):
    canvas.create_oval(
        c.x - c.r, c.y - c.r,
        c.x + c.r, c.y + c.r
    )

root = Tk()

canvas = Canvas(root, width=300, height=200)
canvas.pack()

draw_circle(canvas, Circle(80, 80, 40))
draw_circle(canvas, Circle(180, 80, 30))

root.mainloop()