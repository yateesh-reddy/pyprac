class Rectangle:
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color

def draw_rectangle(canvas, rect):
    canvas.create_rectangle(rect.x, rect.y,
                            rect.x+rect.w,
                            rect.y+rect.h,
                            fill=rect.color)