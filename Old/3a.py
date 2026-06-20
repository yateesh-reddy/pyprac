from tkinter import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def draw_point(canvas, p):
    canvas.create_oval(p.x-2, p.y-2,
                       p.x+2, p.y+2,
                       fill="black")

root = Tk()
c = Canvas(root, width=300, height=300)
c.pack()

p = Point(100, 100)
draw_point(c, p)

root.mainloop()