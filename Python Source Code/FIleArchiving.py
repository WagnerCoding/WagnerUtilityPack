import os
import PySimpleGUI as sg
import sys
import bz2
import lzma
import gzip
import shutils
import zipfile

def main():


    layout = [
        #[sg.Image(key="-IMAGE-")],
        [

            [sg.HSeparator()],
            [sg.Text('Your Hashes: ')],
            sg.Output(size=(150, 30)),
        ],
    ]
    window = sg.Window("File Archiving", layout)
    while True:
        event, values = window.read()

        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()


if __name__ == "__main__":
    main()