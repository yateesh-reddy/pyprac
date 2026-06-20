from tkinter import *

class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

def draw_rectangle(canvas, rect):
    canvas.create_rectangle(
        rect.x,
        rect.y,
        rect.x + rect.width,
        rect.y + rect.height,
        fill=rect.color 
    )

root = Tk()

canvas = Canvas(root, width=300, height=200)
canvas.pack()

r = Rectangle(50, 50, 150, 80, "blue")
draw_rectangle(canvas, r)

root.mainloop()