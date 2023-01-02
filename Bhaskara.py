import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Insira a'), sg.InputText()],
            [sg.Text('Insira b'), sg.InputText()],
            [sg.Text('Insira c'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]



# Create the Window
window = sg.Window('Bhaskara', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    
    #Bhaskara
    
    if values[0] == "":
        a = 0
    else:
        a = float(values[0])
        
    if values[1] == "":
        b = 0
    else:
        b = float(values[1])
    
    if values[2] == "":
        c = 0
    else:
        c = float(values[2])
    
    delta = b**2 - 4*a*c
    
    if delta > 0:
        X1 = (-1*b + delta**0.5) / (2 * a)
        X2 = (-1*b - delta**0.5) / (2 * a)
        
        print("Os valores de X são ", X1, X2)
        print(delta)
    
    if delta < 0:
        X = "Ø"
        
        print("Não é possível calcular X, pois deltta é negativo")
        
    if delta == 0:
        X = (-1*b + delta**0.5) / (2 * a)
        
        print("X é ", X)
      
    print('You entered ', a, b, c,)

window.close()