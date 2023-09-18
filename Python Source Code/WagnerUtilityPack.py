import PySimpleGUI as sg
import PyHashGen
import FIleArchiving

def createList():
    myList = ["PyHashGen", 'ok', 'friend']
    return myList

myList = ["PyHashGen", 'FileArchiving', 'friend']

layout = [

   # [sg.Button("Create dropdown list")],
   # [sg.Output(key="console_output")],
    [sg.OptionMenu(myList, key="-TEST-")],
    [sg.Button("Click")]

]

window = sg.Window("Winner profiles", layout)

while True:
    event, values = window.read()

    choice = values

    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    #if event == "Create dropdown list":
     #   print("Creating, please wait...")
      #  doneList = createList()
       # print("Completed!")
        #window['tester'].update(values=doneList)

    if event == "Click" and values["-TEST-"] == "PyHashGen":
        PyHashGen.main()

    if event == "Click" and values["-TEST-"] == "FileArchiving":
        FIleArchiving.main()