"""
Simple Tkinter only GUI
reference: https://likegeeks.com/python-gui-examples-tkinter-tutorial/
"""

from tkinter import *

window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry("350x200")

lbl = Label(window, text="Hello")
lbl.pack()


def clicked():
    lbl.configure(text="Button was clicked !!")


btn = Button(window, text="Click Me", command=clicked)
btn.pack()

window.mainloop()
