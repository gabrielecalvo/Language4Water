"""
To improve this example I highly recommend to have a look at:
https://pysimplegui.readthedocs.io/en/latest/screenshots_demos/
"""

import PySimpleGUI as sg
import random

shown_card = random.randint(1, 13)
secret_card = random.randint(1, 13)

window = sg.Window(
    "High-Low Card Game",
    layout=[
        [
            sg.Text(text="The shown card is, "),
            sg.Text(text=shown_card, key="-SHOWN-"),
        ],
        [sg.Text("is the next one going to be higher or lower?")],
        [
            sg.Button("Lower", button_color=("black", "green3"), key="-Lower-"),
            sg.Button("Higher", button_color=("black", "red3"), key="-Higher-"),
        ],
    ],
)

while True:  # The Event Loop
    event, values = window.read()

    print(event, values)
    if event == sg.WIN_CLOSED:
        print("closed window")
        sg.popup("Thank you for playing, goodbye :)")
        break

    correct_high = event == "-Higher-" and secret_card > shown_card
    correct_low = event == "-Lower-" and secret_card < shown_card
    if correct_high or correct_low:
        sg.popup(f"you WON! the hidden card was {secret_card}")
    else:
        sg.popup(f"you LOST! the hidden card was {secret_card}")

    shown_card = secret_card
    secret_card = random.randint(1, 13)
    window["-SHOWN-"].update(shown_card)

window.close()
