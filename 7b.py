from tkinter import *

class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

def draw_circle(canvas, c):
    canvas.create_oval(c.x-c.r, c.y-c.r,
                       c.x+c.r, c.y+c.r)

root = Tk()
cv = Canvas(root, width=300, height=300)
cv.pack()

c1 = Circle(100, 100, 50)
draw_circle(cv, c1)

root.mainloop()