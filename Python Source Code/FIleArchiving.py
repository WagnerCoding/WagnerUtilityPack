import os
import PySimpleGUI as sg
import sys
import bz2
import lzma
import gzip
import shutils
import zipfile
import io



file_types = [("All files (*.*)", "*.*")]

def main():


    layout = [
        #[sg.Image(key="-IMAGE-")],
        [
            [sg.Text("File to hash: "), sg.Input(size=(25, 1), key="-FILE-"), sg.FileBrowse(file_types=file_types)],
            [sg.HSeparator()],
            [sg.Button("Hash that File!"), sg.Button("Hash that text!"), sg.Button("Verify that Hash!"), sg.Button("Exit")],
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

        if event == "Hash that File!":
            filename = values["-FILE-"]
            archivename = filename + ".gz"

            if os.path.exists(filename):
                with open(filename, 'rb') as src, gzip.open(archivename, 'wb') as dst:
                    dst.writelines(src)

    window.close()


if __name__ == "__main__":
    main()