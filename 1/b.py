from tkinter import *

root = Tk()
root.title("Window Wizard")
root.geometry("300x150")

Label(root, text="Name").grid(row=0, column=0)
Entry(root).grid(row=0, column=1)

Label(root, text="Email").grid(row=1, column=0)
Entry(root).grid(row=1, column=1)

Button(root, text="Submit").grid(row=2, column=0)
Button(root, text="Reset").grid(row=2, column=1)

root.mainloop()
