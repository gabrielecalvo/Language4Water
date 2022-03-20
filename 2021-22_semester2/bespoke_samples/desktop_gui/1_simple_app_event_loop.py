import PySimpleGUI as sg

sg.theme("DarkAmber")  # Keep things interesting for your users

first_row = [sg.Text("My one-shot window.")]
second_row = [sg.InputText(key="-IN-")]
third_row = [sg.Submit(), sg.Cancel()]

window = sg.Window("Window Title", layout=[first_row, second_row, third_row])

while True:  # The Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        print("closed window")
        break

window.close()
