import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Number 1'), sg.InputText("Insira o valor de a")],
            [sg.Text('Number 2'), sg.InputText("Insira o valor de b")],
            [sg.Text('Number 3'), sg.InputText("Insira o valor de c")],
            [sg.Button('Ok'), sg.Button('Cancel')] ]



# Create the Window
window = sg.Window('Bhaskara', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    
    #Bhaskara
    
    if a == "":
        a = 0
        
    if b == "":
        b = 0
    
    if c == "":
        c = 0
    
    a = float(values[0])
    b = float(values[1])
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