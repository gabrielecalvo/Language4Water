from tkinter import *
from tkinter.messagebox import showinfo, showerror

import random

cards = {"shown": random.randint(1, 13), "secret": random.randint(1, 13)}

window = Tk()
window.title("High-Low Card Game")
window.geometry("300x100")

Label(window, text="The shown card is, ").grid(row=0, column=0)
shown_card_label = Label(window, text=cards["shown"])
shown_card_label.grid(row=0, column=1)
Label(window, text="Is the next one going to be higher or lower?").grid(
    row=1, column=0, columnspan=2
)


def clicked(chosen):
    correct_high = chosen == "higher" and cards["secret"] > cards["shown"]
    correct_low = chosen == "lower" and cards["secret"] < cards["shown"]

    if correct_high or correct_low:
        showinfo(message=f"you WON! the hidden card was {cards['secret']}")
    else:
        showerror(message=f"you LOST! the hidden card was {cards['secret']}")

    cards["shown"] = cards["secret"]
    cards["secret"] = random.randint(1, 13)
    shown_card_label.configure(text=cards["shown"])


Button(
    window, text="Lower", command=lambda: clicked("lower"), background="green3"
).grid(row=2, column=0)
Button(
    window, text="Higher", command=lambda: clicked("higher"), background="red3"
).grid(row=2, column=1)


def on_closing():
    if showinfo(message="Thank you for playing, goodbye :)"):
        window.destroy()


window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
