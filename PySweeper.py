import tkinter
from tkinter import *

# https://www.tutorialspoint.com/python3/python_gui_programming.htm
# https://www.tutorialspoint.com/python3/tk_button.htm
# https://www.tutorialspoint.com/python3/tk_canvas.htm
# https://www.jython.org/

top = tkinter.Tk()
b = Button(top, text = "Button")
b.place(x=10,y=10)
top.mainloop()