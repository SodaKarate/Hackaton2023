import PySimpleGUI as sg

sg.theme('LightBrown4')
layout=[[sg.Text('Mit szeretnél rendelni?')],
        [sg.InputText('')],
        [sg.Button('Oké mehet!'),sg.Button('Mégsem.')]]
window=sg.Window('Pizza rendelés',layout)


while True:                             # The Event Loop
    event, values = window.read() 
    print(event, values)       
    if event == sg.WIN_CLOSED or event == 'Mégsem.':
        break      

window.close()