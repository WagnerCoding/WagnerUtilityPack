import io
import os
import PySimpleGUI as sg
import sys
import subprocess

sg.theme("DarkTeal2")

#from PIL import Image
file_types = [("All files (*.*)", "*.*")]
def main():


    layout = [
        #[sg.Image(key="-IMAGE-")],
        [
            [sg.Button("Install Reaper"), sg.Button("Install Audacity"), sg.Button("Install VLC"), sg.Button("Install Pycharm"), sg.Button("Install Eclipse"), sg.Button("Install OpenJDK"), sg.Button("Install WinRar"), sg.Button("Install Python"),  sg.Button("Install All"), sg.Button("Exit")],
            [sg.HSeparator()],
            [sg.Text('Output: ')],
            sg.Output(size=(150, 30)),
        ],
    ]
    window = sg.Window("PyHashGen", layout)
    while True:
        event, values = window.read()



        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        if event == "Install WinRar":
            try:
                subprocess.run("powershell.exe mkdir C:\\temp", shell=True, capture_output=True, text=True),
                subprocess.run("powershell.exe Start-BitsTransfer -Source https://www.rarlab.com/rar/winrar-x64-624.exe -Destination C:\\temp\\winrar.exe", shell=True, capture_output=True, text=True),
                subprocess.run("powershell.exe c:\\temp\\winrar.exe /S", shell=True, capture_output=True, text=True),
                subprocess.run("powershell.exe Remove-Item -LiteralPath 'c:\\temp' -Force -Recurse", shell=True, capture_output=True, text=True),
                print("Success")
            except:
                print("Failed")


        if event == "Install Python":
            try:
                subprocess.run("powershell.exe mkdir C:\\temp", shell=True, capture_output=True, text=True),
                subprocess.run("powershell.exe Start-BitsTransfer -Source https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe -Destination C:\\temp\\python.exe", shell=True, capture_output=True, text=True),
                subprocess.run("powershell.exe c:\\temp\\python.exe /S", shell=True, capture_output=True, text=True),
                subprocess.run("powershell.exe Remove-Item -LiteralPath 'c:\\temp' -Force -Recurse", shell=True, capture_output=True, text=True),
                print("Success")
            except:
                print("Failed")


        if event == "Install OpenJDK":
            try:
                subprocess.run("powershell.exe mkdir C:\\temp", shell=True, capture_output=True, text=True),
                subprocess.run("powershell.exe Start-BitsTransfer -Source https://github.com/adoptium/temurin8-binaries/releases/download/jdk8u382-b05/OpenJDK8U-jdk_x64_windows_hotspot_8u382b05.msi -Destination C:\\temp\\openjdk.msi", shell=True, capture_output=True, text=True),
                subprocess.run("powershell.exe Start-Process C:\\temp\\openjdk.msi -ArgumentList '/qn' -Wait", shell=True, capture_output=True, text=True),
                subprocess.run("powershell.exe Remove-Item -LiteralPath 'c:\\temp' -Force -Recurse", shell=True, capture_output=True, text=True),
                print("Success")
            except:
                print("Failed")


        if event == "Install Eclipse":
            try:
                subprocess.run("powershell.exe mkdir C:\\temp", shell=True, capture_output=True, text=True),
                subprocess.run("powershell.exe Start-BitsTransfer -Source https://tinyurl.com/5hct5rkr -Destination c:\\temp\\eclipse.zip", shell=True, capture_output=True, text=True),
                subprocess.run("powershell.exe Expand-Archive C:\\temp\\eclipse.zip -DestinationPath C:\\Users\\Public\\Desktop", shell=True, capture_output=True, text=True),
                subprocess.run("powershell.exe Remove-Item -LiteralPath 'c:\\temp' -Force -Recurse", shell=True, capture_output=True, text=True),
                print("Success")
            except:
                print("Failed")

        if event == "Install Reaper":
            try:
                subprocess.run("powershell.exe mkdir C:\\temp", shell=True, capture_output=True, text=True),
                subprocess.run("powershell.exe Start-BitsTransfer -Source https://www.reaper.fm/files/6.x/reaper682_x64-install.exe -Destination C:\\temp\\reaper.exe", shell=True, capture_output=True, text=True),
                subprocess.run("powershell.exe C:\\temp\\reaper.exe /S", shell=True, capture_output=True, text=True),
                subprocess.run("powershell.exe Remove-Item -LiteralPath 'c:\\temp' -Force -Recurse", shell=True, capture_output=True, text=True),
                print("Success")
            except:
                print("Failed")

            #   output = "Hashes for '" + filename + "'"
        if event == "Install VLC":

            try:
                subprocess.run("powershell.exe mkdir C:\\temp", shell=True, capture_output=True, text=True),
                subprocess.run("powershell.exe Start-BitsTransfer -Source https://get.videolan.org/vlc/3.0.19/win64/vlc-3.0.19-win64.msi -Destination C:\\temp\\vlc.msi", shell=True, capture_output=True, text=True),
                subprocess.run("powershell.exe Start-Process C:\\temp\\vlc.msi -ArgumentList '/qn' -Wait", shell=True, capture_output=True, text=True),
                subprocess.run("powershell.exe Remove-Item -LiteralPath 'c:\\temp' -Force -Recurse", shell=True, capture_output=True, text=True),
                print("Success")
            except:
                print("failed")
            #   output = "Hashes for '" + filename + "'"
        if event == "Install Audacity":
            try:
                subprocess.run("powershell.exe mkdir C:\\temp", shell=True, capture_output=True, text=True),
                subprocess.run("powershell.exe Start-BitsTransfer -Source https://github.com/audacity/audacity/releases/download/Audacity-3.3.3/audacity-win-3.3.3-x64.exe -Destination C:\\temp\\audacity.exe", shell=True, capture_output=True, text=True),
                subprocess.run("powershell.exe C:\\temp\\audacity.exe /VERYSILENT", shell=True, capture_output=True, text=True),
                subprocess.run("powershell.exe Remove-Item -LiteralPath 'c:\\temp' -Force -Recurse", shell=True, capture_output=True, text=True),
                print("Success")
            except:
                print("failed")

        if event == "Install Pycharm":
            try:
                subprocess.run("powershell.exe mkdir C:\\temp", shell=True, capture_output=True, text=True),
                subprocess.run("powershell.exe Start-BitsTransfer -Source https://download.jetbrains.com/python/pycharm-community-2023.2.2.exe -Destination C:\\temp\\pycharm.exe", shell=True, capture_output=True, text=True),
                subprocess.run("powershell.exe C:\\temp\\pycharm.exe /S", shell=True, capture_output=True, text=True),
                subprocess.run("powershell.exe Remove-Item -LiteralPath 'c:\\temp' -Force -Recurse", shell=True, capture_output=True, text=True),
                print("Success")
            except:
                print("failed")

        if event == "Install All":
                try:
                    subprocess.run("powershell.exe mkdir C:\\temp", shell=True, capture_output=True, text=True),
                    subprocess.run("powershell.exe Start-BitsTransfer -Source https://download.jetbrains.com/python/pycharm-community-2023.2.2.exe -Destination C:\\temp\\pycharm.exe", shell=True, capture_output=True, text=True),
                    subprocess.run("powershell.exe C:\\temp\\pycharm.exe /S", shell=True, capture_output=True, text=True),
                    print("Pycharm Installer Finished"),
                    subprocess.run("powershell.exe Start-BitsTransfer -Source https://github.com/audacity/audacity/releases/download/Audacity-3.3.3/audacity-win-3.3.3-x64.exe -Destination C:\\temp\\audacity.exe", shell=True, capture_output=True, text=True),
                    subprocess.run("powershell.exe C:\\temp\\audacity.exe /VERYSILENT", shell=True, capture_output=True, text=True),
                    print("Audacity Installer Finished"),
                    subprocess.run("powershell.exe Start-BitsTransfer -Source https://get.videolan.org/vlc/3.0.19/win64/vlc-3.0.19-win64.msi -Destination C:\\temp\\vlc.msi", shell=True, capture_output=True, text=True),
                    subprocess.run("powershell.exe Start-Process C:\\temp\\vlc.msi -ArgumentList '/qn' -Wait", shell=True, capture_output=True, text=True),
                    print("VLC Installer Finished"),
                    subprocess.run("powershell.exe Start-BitsTransfer -Source https://www.reaper.fm/files/6.x/reaper682_x64-install.exe -Destination C:\\temp\\reaper.exe",shell=True, capture_output=True, text=True),
                    subprocess.run("powershell.exe C:\\temp\\reaper.exe /S", shell=True, capture_output=True, text=True),
                    print("Reaper Installer Finished"),
                    subprocess.run("powershell.exe Start-BitsTransfer -Source https://tinyurl.com/5hct5rkr -Destination c:\\temp\\eclipse.zip", shell=True, capture_output=True, text=True),
                    subprocess.run("powershell.exe Expand-Archive C:\\temp\\eclipse.zip -DestinationPath C:\\Users\\Public\\Desktop", shell=True, capture_output=True, text=True),
                    print("Eclipse Installer Finished"),
                    subprocess.run("powershell.exe Start-BitsTransfer -Source https://github.com/adoptium/temurin8-binaries/releases/download/jdk8u382-b05/OpenJDK8U-jdk_x64_windows_hotspot_8u382b05.msi -Destination C:\\temp\\openjdk.msi", shell=True, capture_output=True, text=True),
                    subprocess.run("powershell.exe Start-Process C:\\temp\\openjdk.msi -ArgumentList '/qn' -Wait", shell=True, capture_output=True, text=True),
                    print("OpenJDK Installer Finished"),
                    subprocess.run("powershell.exe Start-BitsTransfer -Source https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe -Destination C:\\temp\\python.exe", shell=True, capture_output=True, text=True),
                    subprocess.run("powershell.exe c:\\temp\\python.exe /S", shell=True, capture_output=True, text=True),
                    print("Python Installer Finished"),
                    subprocess.run("powershell.exe Start-BitsTransfer -Source https://www.rarlab.com/rar/winrar-x64-624.exe -Destination C:\\temp\\winrar.exe", shell=True, capture_output=True, text=True),
                    subprocess.run("powershell.exe c:\\temp\\winrar.exe /S", shell=True, capture_output=True, text=True),
                    print("WinRar Installer Finished"),
                    subprocess.run("powershell.exe Remove-Item -LiteralPath 'c:\\temp' -Force -Recurse", shell=True, capture_output=True, text=True),
                    print("Success")
                except:
                    print("failed")

    window.close()
if __name__ == "__main__":
    main()