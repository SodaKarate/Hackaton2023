import PySimpleGUI as sg

def showCurrentList(adatok):
    indexek = ['sajtos pizza', 'sonkás pizza', 'gombás pizza', 'hawaii pizza', 'pepsi', 'coca cola', 'viz']
    layout = []

    for i in range(len(adatok)):
        if adatok[i]!=0:
            szoveg=indexek[i],adatok[i]
            layout.append([sg.Text(szoveg)])
    layout.append([sg.Button('Vissza')])
    sg.theme('LightBrown4')
    window = sg.Window('Pizza rendelés részletek', layout)
    
    while True:
        event, values = window.read()
        print(event, values)
        
        if event == sg.WINDOW_CLOSED or event == 'Vissza':
            break
    
    window.close() 

sg.theme('LightBrown4')
layout=[[sg.Text('Mit szeretnél rendelni?')],
        [sg.InputText('')],
        [sg.Button('Oké mehet!'),sg.Button('Részletek'),sg.Button('Mégsem.')]]
window=sg.Window('Pizza rendelés',layout)


while True:                             # The Event Loop
    event, values = window.read() 
    print(event, values)       
    if event == sg.WIN_CLOSED or event == 'Mégsem.':
        break
    if event == 'Részletek':
        showCurrentList([0,1,2,1,0,0,1])

window.close()