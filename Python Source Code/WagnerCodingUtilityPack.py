import PySimpleGUI as sg
import PyHashGen
import FileArchiving
import ApplicationDeployer
import PowershellTools
import EncodeDecodeBase64

sg.theme("DarkTeal2")

def createList():
    myList = ["PyHashGen", 'ok', 'friend']
    return myList

myList = ["PyHashGen", 'FileArchiving', 'ApplicationDeployer', "PowershellTools", 'Base64']

layout = [

   # [sg.Button("Create dropdown list")],
   # [sg.Output(key="console_output")],
    [sg.OptionMenu(myList, key="-TEST-")],
    [sg.Button("Open")]

]

window = sg.Window("Wagner Coding Utility Pack", layout)

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

    if event == "Open" and values["-TEST-"] == "PyHashGen":
        PyHashGen.main()

    if event == "Open" and values["-TEST-"] == "FileArchiving":
        FileArchiving.main()

    if event == "Open" and values["-TEST-"] == "ApplicationDeployer":
        ApplicationDeployer.main()

    if event == "Open" and values["-TEST-"] == "PowershellTools":
        PowershellTools.main()
        
    if event == "Open" and values["-TEST-"] == "Base64":
        EncodeDecodeBase64.main()