from tkinter import *

class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

def draw_rectangle(canvas, rect):
    canvas.create_rectangle(rect.x, rect.y,
                            rect.x+rect.w,
                            rect.y+rect.h)

root = Tk()
c = Canvas(root, width=300, height=300)
c.pack()

r = Rectangle(50, 50, 100, 80)
draw_rectangle(c, r)

root.mainloop()