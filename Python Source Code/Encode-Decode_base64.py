# image_viewer.py
import io
import os
import PySimpleGUI as sg
import base64
import sys
import subprocess

sg.theme("DarkTeal2")

#from PIL import Image
#file_types = [("All files (*.*)", "*.*")]
def main():

    hashtypes = ("MD5: ", "SHA1: ", "SHA224: ", "SHA256: ", "SHA384: ", "SHA512: ", "SHA3_224: ", "SHA3_256: ", "SHA3_384: ", "SHA3_512: ", "SHAKE_128: ", "SHAKE_256: ", "BLAKE2B: ", "BLAKE2S: ")


    layout = [
        #[sg.Image(key="-IMAGE-")],
        [
            [sg.Text("Text Input:"), sg.Input(size=(100, 30), key="-EncText-")],
            #[sg.HSeparator()],
            #[sg.Text('Enter text to hash: ', size=(15, 1)), sg.InputText(key="-TEXT-")],
            #[sg.HSeparator()],
            #[sg.Text('Enter hash to verify: ', size=(15, 1)), sg.InputText(key="-HASH-")],
            #[sg.HSeparator()],
            [sg.Button("Encode"), sg.Button("Decode"), sg.Button("Exit")],
            [sg.HSeparator()],
            [sg.Text('Your Hashes: ')],
            sg.Output(size=(100, 30)),
        ],
    ]
    window = sg.Window("Base64", layout)
    while True:
        event, values = window.read()



        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Encode":
            textstring = values["-EncText-"]

            try:
                if textstring != None:
                    s = textstring
                    b = s.encode("UTF-8")
                    e = base64.b64encode(b) # bytes
                    textencode = e.decode("UTF-8")
                    print("Base64 Encoded: ", textencode)
                    print('Original input text: ', textstring)
                    
                    
                #for type, hash in zip(hashtypes, hashes):
                #    print(type, hash)
                print("")
                #print("")
            except:
                #print("No text has been entered for encoding or decoding. ")
                print("")
                #print("")
            #   output = "Hashes for '" + filename + "'"
        
        if event == "Decode":
            textstring = values["-EncText-"]

            try:
                if textstring != None:
                    s = textstring
                    b = s.encode("UTF-8")
                    e = base64.b64decode(b) # bytes
                    textencode = e.decode("UTF-8")
                    print("Base64 Decoded: ", textencode)
                    print('Original input text: ', textstring)
                    
                    
                #for type, hash in zip(hashtypes, hashes):
                #    print(type, hash)
                print("")
                #print("")
            except:
                #print("No text has been entered for encoding or decoding. ")
                print("")
                #print("")
            #   output = "Hashes for '" + filename + "'"


    window.close()
if __name__ == "__main__":
    main()
