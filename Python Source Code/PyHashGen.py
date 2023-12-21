# image_viewer.py
import io
import os
import PySimpleGUI as sg
import hashlib
import sys
import subprocess

sg.theme("DarkTeal2")

#from PIL import Image
file_types = [("All files (*.*)", "*.*")]
def main():

    hashtypes = ("MD5: ", "SHA1: ", "SHA224: ", "SHA256: ", "SHA384: ", "SHA512: ", "SHA3_224: ", "SHA3_256: ", "SHA3_384: ", "SHA3_512: ", "SHAKE_128: ", "SHAKE_256: ", "BLAKE2B: ", "BLAKE2S: ")


    layout = [
        #[sg.Image(key="-IMAGE-")],
        [
            [sg.Text("File to hash: "), sg.Input(size=(25, 1), key="-FILE-"), sg.FileBrowse(file_types=file_types)],
            [sg.HSeparator()],
            [sg.Text('Enter text to hash: ', size=(15, 1)), sg.InputText(key="-TEXT-")],
            [sg.HSeparator()],
            [sg.Text('Enter hash to verify: ', size=(15, 1)), sg.InputText(key="-HASH-")],
            [sg.HSeparator()],
            [sg.Button("Hash that File!"), sg.Button("Hash that text!"), sg.Button("Verify that Hash!"), sg.Button("Install Pycharm"), sg.Button("Exit")],
            [sg.HSeparator()],
            [sg.Text('Your Hashes: ')],
            sg.Output(size=(150, 30)),
        ],
    ]
    window = sg.Window("PyHashGen", layout)
    while True:
        event, values = window.read()



        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Hash that File!":
            filename = values["-FILE-"]
            if os.path.exists(filename):
                # BUF_SIZE is totally arbitrary, change for your app!
                BUF_SIZE = 51200000  # lets read stuff in 64kb chunks!

                md5 = hashlib.md5()
                sha1 = hashlib.sha1()
                sha224 = hashlib.sha224()
                sha256 = hashlib.sha256()
                sha384 = hashlib.sha384()
                sha512 = hashlib.sha512()
                sha3_224 = hashlib.sha3_224()
                sha3_256 = hashlib.sha3_256()
                sha3_384 = hashlib.sha3_384()
                sha3_512 = hashlib.sha3_512()
                shake_128 = hashlib.shake_128()
                shake_256 = hashlib.shake_256()
                blake2b = hashlib.blake2b(digest_size=30)
                blake2s = hashlib.blake2s(digest_size=30)

                with open(filename, 'rb') as f:
                    while True:
                        data = f.read(BUF_SIZE)
                        if not data:
                            break
                        md5.update(data)
                        sha1.update(data)
                        sha224.update(data)
                        sha256.update(data)
                        sha384.update(data)
                        sha512.update(data)
                        sha3_224.update(data)
                        sha3_256.update(data)
                        sha3_384.update(data)
                        sha3_512.update(data)
                        shake_128.update(data)
                        shake_256.update(data)
                        blake2b.update(data)
                        blake2s.update(data)

                    hashes = (md5.hexdigest(), sha1.hexdigest(), sha224.hexdigest(), sha256.hexdigest(), sha384.hexdigest(), sha512.hexdigest(), sha3_224.hexdigest(), sha3_256.hexdigest(), sha3_384.hexdigest(), sha3_512.hexdigest(), shake_128.hexdigest(30), shake_256.hexdigest(30), blake2b.hexdigest(), blake2s.hexdigest())


                for type, hash in zip(hashtypes, hashes):
                    print(type, hash)
                print("")
                print("")

            else:
                print("No file has been selected for hash computation.")
                print("")
                print("")

            #   output = "Hashes for '" + filename + "'"
        if event == "Hash that text!":
            textstring = values["-TEXT-"]

            try:
                if textstring:
                    texthash = textstring

                    md5 = hashlib.md5(texthash.encode())
                    sha1 = hashlib.sha1(texthash.encode())
                    sha224 = hashlib.sha224(texthash.encode())
                    sha256 = hashlib.sha256(texthash.encode())
                    sha384 = hashlib.sha384(texthash.encode())
                    sha512 = hashlib.sha512(texthash.encode())
                    sha3_224 = hashlib.sha3_224(texthash.encode())
                    sha3_256 = hashlib.sha3_256(texthash.encode())
                    sha3_384 = hashlib.sha3_384(texthash.encode())
                    sha3_512 = hashlib.sha3_512(texthash.encode())
                    shake_128 = hashlib.shake_128(texthash.encode())
                    shake_256 = hashlib.shake_256(texthash.encode())
                    blake2b = hashlib.blake2b(texthash.encode())
                    blake2s = hashlib.blake2s(texthash.encode())

                    hashes = (md5.hexdigest(), sha1.hexdigest(), sha224.hexdigest(), sha256.hexdigest(), sha384.hexdigest(), sha512.hexdigest(), sha3_224.hexdigest(), sha3_256.hexdigest(), sha3_384.hexdigest(), sha3_512.hexdigest(), shake_128.hexdigest(30), shake_256.hexdigest(30), blake2b.hexdigest(), blake2s.hexdigest())


                for type, hash in zip(hashtypes, hashes):
                    print(type, hash)
                print("")
                print("")
            except:
                print("No text has been entered for hash computation. ")
                print("")
                print("")
            #   output = "Hashes for '" + filename + "'"
        if event == "Verify that Hash!":
            checkhash = window['-HASH-'].get().strip()
            try:
                if checkhash in hashes:
                    print("Hash is a match! Source integrity verified!")
                    print("")
                    print("")
                if checkhash not in hashes:
                    print("Hash does not match, source integrity compromised!!!")
                    print("")
                    print("")
            except:
                print("No computed hash to verify.")
                print("")
                print("")

        if event == "Install Pycharm":
            try:
                Processes = subprocess.call('powershell.exe "Start-BitsTransfer -Source https://download.jetbrains.com/python/pycharm-community-2023.2.2.exe -Destination pycharm.exe"', shell=True, capture_output=True, text=True)
                print(Processes)
            except:
                print("failed")

    window.close()
if __name__ == "__main__":
    main()
