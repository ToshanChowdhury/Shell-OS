import os
import sys
import time
from datetime import datetime

date_time = datetime.now()
date_type = date_time.strftime("%d-%m-%Y")
time_type = date_time.strftime("%H:%M")

time.sleep(1)
print("Welcome Guest!!")
time.sleep(1)
print("The Date Is: "+date_type)
print("The Time Is: "+time_type)
print("Here Are A Few Options In Shell OS: ")
print("")
print("""
--Tools--
[1] Clock
[2] Text Editor
[3] OpenWord
[4] Calculator
[5] Paint
[6] Web Browser
[7] Terminal

--Power Options--
[8] Shut Down
[9] Restart
""")
print("")
option = input("[?]: ")

if option == "1":
    os.startfile("ClockApp.py")
    os.startfile("ShellOSGuest.py")

if option == "2":
    os.startfile("WritingDocs.py")
    os.startfile("ShellOSGuest.py")

if option == "3":
    os.startfile("OpenWord.exe")
    os.startfile("ShellOSGuest.py")

if option == "4":
    os.startfile("CalculatorApp.py")
    os.startfile("ShellOSGuest.py")

if option == "5":
    os.startfile("PaintApp.py")
    os.startfile("ShellOSGuest.py")

if option == "6":
    os.startfile("MainBrowser.py")
    os.startfile("ShellOSGuest.py")

if option == "7":
    os.startfile("CMD.py")
    os.startfile("ShellOSGuest.py")

if option == "8":
    sys.exit()

if option == "9":
    OperatingSystem = "ShellOS.py"
    os.startfile(OperatingSystem)
    sys.exit()