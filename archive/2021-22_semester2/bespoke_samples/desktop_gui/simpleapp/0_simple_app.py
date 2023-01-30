import PySimpleGUI as sg

first_row = [sg.Text("My one-shot window.")]
second_row = [sg.InputText(key="-IN-")]
third_row = [sg.Submit(), sg.Cancel()]

window = sg.Window("Window Title", layout=[first_row, second_row, third_row])

event, values = window.read()

window.close()

text_input = values["-IN-"]
sg.popup("You entered", text_input)
