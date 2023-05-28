import PySimpleGUI as sg

def checkInput(adat,lista):
    if 'sajtos pizza' in adat:
        lista[0]+=1
    if 'sonkás pizza' in adat:
        lista[1]+=1
    if 'gombás pizza' in adat:
        lista[2]+=1
    if 'hawaii pizza' in adat:
        lista[3]+=1
    if 'pepsi' in adat:
        lista[4]+=1
    if 'coca' in adat:
        lista[5]+=1
    if 'víz' in adat:
        lista[6]+=1
    
    return lista


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


orderDone=False
lista=[0,0,0,0,0,0,0]

while True:
    event, values = window.read() 
    print(event, values)       
    if event == sg.WIN_CLOSED or event == 'Mégsem.':
        break
    if event == 'Részletek':
        showCurrentList(lista)
    if event == 'Oké mehet!':
        lista=checkInput(values[0],lista)
        print(lista)

window.close()