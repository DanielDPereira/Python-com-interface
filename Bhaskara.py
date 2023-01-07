import PySimpleGUI as sg

def programa():
    
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('Insira a'), sg.InputText()],
                [sg.Text('Insira b'), sg.InputText()],
                [sg.Text('Insira c'), sg.InputText()],
                [sg.Button('Ok'), sg.Button('Cancel')],
                [sg.Text('Created by DanielDPereira')]]



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
        
        #Calculo de delta
        delta = b**2 - 4*a*c
        
        # Se delta...
        
        if delta > 0:
            X1 = (-1*b + delta**0.5) / (2 * a)
            X2 = (-1*b - delta**0.5) / (2 * a)
            
            print(delta)
            
            window.close()
            
            layout1 = [[sg.Text('Os valores de X são:')],
                [sg.Text(X1)],
                [sg.Text(X2)],
                [sg.Text('Created by DanielDPereira')]]

            window = sg.Window('Bhaskara', layout1)
            
            print("Os valores de X são ", X1, X2)

        elif delta < 0:
            X = "Ø"
            
            window.close()
            
            layout1 = [[sg.Text('A equação não possui solução dentre os números reais.')],
                [sg.Text('Created by DanielDPereira')]]

            window = sg.Window('Bhaskara', layout1)
            
            print("Não é possível calcular X, pois delta é negativo")
            
        elif delta == 0:
            X = (-1*b + delta**0.5) / (2 * a)
            
            window.close()
            
            layout1 = [[sg.Text('X possui apenas um valor, que é:')],
                [sg.Text(X)],
                [sg.Text('Created by DanielDPereira')]]

            window = sg.Window('Bhaskara', layout1)
            
            print("X é ", X)
        
programa()    
