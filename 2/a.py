from tkinter import *

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

def draw_rectangle(canvas, rect):
    canvas.create_rectangle(
        rect.x,
        rect.y,
        rect.x + rect.width,
        rect.y + rect.height
    )

root = Tk()

canvas = Canvas(root, width=300, height=200)
canvas.pack()

r = Rectangle(50, 50, 150, 80)
draw_rectangle(canvas, r)

root.mainloop()