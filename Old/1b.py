from tkinter import *

root = Tk()
root.title("Wizard")

Label(root, text="Name").grid(row=0, column=0)
Label(root, text="Age").grid(row=1, column=0)

e1 = Entry(root)
e2 = Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

def submit():
    print(e1.get(), e2.get())

def reset():
    e1.delete(0, END)
    e2.delete(0, END)

Button(root, text="Submit", command=submit).grid(row=2, column=0)
Button(root, text="Reset", command=reset).grid(row=2, column=1)

root.mainloop()