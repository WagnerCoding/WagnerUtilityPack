import os
import PySimpleGUI as sg
import sys
import bz2
import lzma
import gzip
import shutils
import zipfile
import io
import tarfile
import time
import binascii


def main():


    layout = [
        #[sg.Image(key="-IMAGE-")],
        [
            [sg.Text("Target File: "), sg.Input(size=(25, 1), key="-FILE-"),sg.FileBrowse()],
             [sg.HSeparator()],
             [sg.Text("--OR--")],
             [sg.HSeparator()],
             [sg.Text("Target Folder: "), sg.Input(size=(25, 1), key="-FOLDER-"), sg.FolderBrowse()],
            [sg.HSeparator()],
            [sg.Text("Compression types: ")],
            [sg.Button("GZIP"), sg.Button("BZIP2"), sg.Button("LMZA"), sg.Button("Exit")],
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

        if event == "GZIP":
            filename = values["-FILE-"]
            foldername = values["-FOLDER-"]
            archivename = filename + ".gz"


            if os.path.exists(filename):
                with open(filename, 'rb') as src, gzip.open(archivename, 'wb') as dst:
                    dst.writelines(src)
                    print("File archiving finished: \n" + archivename)
                    window["-FILE-"].Update('')

            if os.path.exists(foldername):
                with tarfile.open(foldername + ".tgz", "w:gz") as tar:
                    tar.add(foldername, arcname = foldername)
                    tar.close()
                    print("Folder archiving finished: \n" + foldername + ".tgz")
                    window["-FOLDER-"].Update('')

        if event == "BZIP2":
            filename = values["-FILE-"]
            foldername = values["-FOLDER-"]
            archivename = filename + ".bz2"
            compressionLevel = 9

            if os.path.exists(filename):
                tarbz2contents = bz2.compress(open(filename, 'rb').read(), compressionLevel)
                fh = open(archivename, "wb")
                fh.write(tarbz2contents)
                fh.close()
                print("File archiving finished: \n" + filename + ".tbz2")
                window["-FILE-"].Update('')

            if os.path.exists(foldername):
                with tarfile.open(foldername + ".tbz2", "w:bz2") as tar:
                    tar.add(foldername, arcname=foldername)
                    tar.close()
                    print("Folder archiving finished: \n" + foldername + ".tbz2")
                    window["-FOLDER-"].Update('')

        if event == "LMZA":
            filename = values["-FILE-"]
            foldername = values["-FOLDER-"]
            archivename = filename + ".xz"

            if os.path.exists(filename):
                with open(filename, 'rb') as f:
                    data = f.read()
                with lzma.open(archivename, 'w') as f:
                    f.write(data)
                print("File archiving finished: \n" + filename + ".xz")
                window["-FILE-"].Update('')

            if os.path.exists(foldername):
                with tarfile.open(foldername + ".xz", "w:xz") as tar:
                    tar.add(foldername, arcname=foldername)
                    tar.close()
                    print("Folder archiving finished: \n" + foldername + ".xz")
                    window["-FOLDER-"].Update('')



    #time.sleep(30)
    window.close()


if __name__ == "__main__":
    main()