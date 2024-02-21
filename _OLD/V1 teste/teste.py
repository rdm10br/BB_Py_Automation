from tkinter import *
from tkinter import Tk

Window = Tk()
Window.configure(width=500, height=300)
Window.title("executor de macro")
Window.minsize(200, 200)  # width, height
Window.maxsize(500, 500)

# Example labels that serve as placeholders for other widgets
t1 = Button(Window, text="macro mouse")
t1.pack()
t2 = Button(Window, text="Filters")
t2.pack()
#exec(open('mouse.ahk').read())
Window.mainloop()