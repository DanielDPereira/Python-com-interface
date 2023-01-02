import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Number 1'), sg.InputText()],
            [sg.Text('Number 2'), sg.InputText()],
            [sg.Text('Number 3'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]



# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    
    #Bhaskara
    
    a = float(values[0])
    b = float(values[1])
    c = float(values[2])
    
    delta = b**2 - 4*a*c
    
    if delta > 0:
        X1 = -1*b + delta**0.5 / 2 * a
        
    
    #-b+-(delta)**0.5/2*a
  
    print('You entered ', a, b, c,)

window.close()