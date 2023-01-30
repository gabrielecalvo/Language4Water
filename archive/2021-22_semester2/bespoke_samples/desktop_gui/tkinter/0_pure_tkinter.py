"""
Simple Tkinter only GUI
reference: https://likegeeks.com/python-gui-examples-tkinter-tutorial/
"""

import tkinter as tk

window = tk.Tk()
window.title("Welcome to LikeGeeks app")
window.geometry("350x200")

lbl = tk.Label(window, text="Hello")
lbl.pack()


def clicked():
    lbl.configure(text="Button was clicked !!")


btn = tk.Button(window, text="Click Me", command=clicked)
btn.pack()

window.mainloop()
