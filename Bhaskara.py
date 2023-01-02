import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Number 1'), sg.InputText()],
            [sg.Text('Number 2'), sg.InputText()],
            [sg.Text('Number 3'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

#Bhaskara 

a = int(values[0])
b = int(values[1])
c = int(values[2])

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()