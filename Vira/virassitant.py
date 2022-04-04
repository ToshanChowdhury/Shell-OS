# IMPORTS
from datetime import date
import time
import os
from time import sleep

# THIS ASSISTANT HAS A FOLLOWING SET OF COMMANDS, IF YOU DO NOT ENTER THE COMMAND IN THIS LIST, IT WILL EXIT.
time.sleep(3)
print("Hello. I am Vira, your Personal Assistant, so tell me, how can I help you today?")
print("")
commands = input("Enter Your Text: ")

# VARIABLES SECTION

# TIME AND DATE
time = time.strftime("%I:%M:%S")
today = date.today()

# WORDS IN LIST
list = ["Tell me the time", 
"Tell me the date",
"How Are You?",
"I am fine thank you",
"I am not fine",
"Open a file",
"Delete a file",
"Start WordPad",
"Start TextMaker",
"Start Antivirus",
"Start Weather",
"Start WritingDocs",
"Repair my operating system",
"Start PlanMaker",
"Start Presentations",
"Start MS Word",
"Start MS Excel",
"Start MS PowerPoint",
"Start MS Outlook",
"Start MS OneNote",
"Start web browser",
"Open a program",
"Open a website",
"Tell me a joke",
"I want to ask internet queries",
"1",
"2",
"3",
"",
"""
""",
]

# LIST
if commands == "Tell me the time":
    print("The Current Time is: "+time)
    input()
    os.startfile("virassitant.py")

if commands == "Tell me the date":
    print("The Current Date is: "+str(today))
    input()
    os.startfile("virassitant.py")

if commands == "How Are You?":
    print("I am Fine Thank You. How About you?")
    answer = input("")

    if answer == "I am fine thank you":
        print("Good To Hear That!")
        input()
        os.startfile("virassitant.py")

    if answer == "I am not Fine":
        print("I Am So Sorry To Hear That :(")
        input()
        os.startfile("virassitant.py")

if commands == "Open a file":
    print("Which File Would You Like Me To Open?")
    var_data = input("File: ")
    print("Opening File...")
    sleep(3)
    os.startfile(var_data)
    input()
    os.startfile("virassitant.py")

if commands == "Delete a file":
    print("Which File Would You Like Me To Delete?")
    var_data = input("File: ")
    print("Deleting File...")
    sleep(3)
    os.remove(var_data)
    input()
    os.startfile("virassitant.py")

if commands == "Start WordPad":
    print("Opening WordPad...")
    sleep(3)
    os.startfile("Wordpad.lnk")
    input()
    os.startfile("virassitant.py")

if commands == "Start TextMaker":
    print("Opening TextMaker...")
    sleep(3)
    os.startfile("TextMaker.lnk")
    input()
    os.startfile("virassitant.py")

if commands == "Start Antivirus":
    print("Opening ShellAntivirus...")
    sleep(3)
    os.startfile("ShellAntivirus.bat")
    input()
    os.startfile("virassitant.py")

if commands == "Start Weather":
    print("Opening Weather...")
    sleep(3)
    os.startfile("Weather.py")
    input()
    os.startfile("virassitant.py")

if commands == "Start WritingDocs":
    print("Opening WritingDocs...")
    sleep(3)
    os.startfile("WritingDocs.py")
    input()
    os.startfile("virassitant.py")

if commands == "Repair my operating system":
    print("Opening RepairTool...")
    sleep(3)
    os.startfile("RepairTool.bat - Admin.lnk")
    input()
    os.startfile("virassitant.py")

if commands == "Start PlanMaker":
    print("Opening PlanMaker...")
    sleep(3)
    os.startfile("PlanMaker.lnk")
    input()
    os.startfile("virassitant.py")

if commands == "Start Presentations":
    print("Opening Presentations...")
    sleep(3)
    os.startfile("Presentations.lnk")
    input()
    os.startfile("virassitant.py")

if commands == "Start MS Word":
    version = input("Enter Your Microsoft Office Version: ")
    sleep(3)
    print("Opening Microsoft Word Version "+version+"...")
    sleep(3)
    os.startfile("Word.lnk")
    input()
    os.startfile("virassitant.py")

if commands == "Start MS Excel":
    version = input("Enter Your Microsoft Office Version: ")
    sleep(3)
    print("Opening Microsoft Excel Version "+version+"...")
    sleep(3)
    os.startfile("Excel.lnk")
    input()
    os.startfile("virassitant.py")

if commands == "Start MS PowerPoint":
    version = input("Enter Your Microsoft Office Version: ")
    sleep(3)
    print("Opening Microsoft PowerPoint Version "+version+"...")
    sleep(3)
    os.startfile("PowerPoint.lnk")
    input()
    os.startfile("virassitant.py")

if commands == "Start MS Outlook":
    version = input("Enter Your Microsoft Office Version: ")
    sleep(3)
    print("Opening Microsoft Outlook Version "+version+"...")
    sleep(3)
    os.startfile("Outlook.lnk")
    input()
    os.startfile("virassitant.py")

if commands == "Start MS OneNote":
    version = input("Enter Your Microsoft Office Version: ")
    sleep(3)
    print("Opening Microsoft OneNote Version "+version+"...")
    sleep(3)
    os.startfile("OneNote.lnk")
    input()
    os.startfile("virassitant.py")

if commands == "Start web browser":
    print("Opening Spinn Browser...")
    sleep(3)
    os.startfile("MainBrowser.py")
    input()
    os.startfile("virassitant.py")

if commands == "Open a program":
    print("")
    print("""Select A Program Extension:
    [1] .lnk
    [2] .py
    [3] .bat
    """)
    print("")
    fileextension = input("[?]: ")

    if fileextension == "1":
        print("Type The Program Name of the .lnk program")
        link = input("Program Name: ")
        os.startfile(link+".lnk")

    if fileextension == "2":
        print("Type The Program Name of the .py program")
        python = input("Program Name: ")
        os.startfile(python+".py")
        input()
        os.startfile("virassitant.py")

    if fileextension == "3":
        print("Type The Program Name of the .bat program")
        batch = input("Program Name: ")
        os.startfile(batch+".bat")

if commands == "Tell me a joke":
    print("Once, my father came home and found me in front of a roaring fire. That made my father very mad, as he didin't have a fireplace.")
    input()
    os.startfile("virassitant.py")

if commands == "I want to ask internet queries":
    print("Just wait for a moment and I will transfer you right over to Internet Browser.")
    sleep(3)
    os.startfile("MainBrowser.py")
    input()
    os.startfile("virassitant.py")

if commands == "Open a website":
    print("Type The Website Name in the field below: ")
    websitename = input()
    os.startfile(websitename)

if not commands == list:
    print("I coludn't get that word, could you try again in the next window?")
    aski = input()

    if aski == "YES":
        os.startfile("virassitant.py")

    if aski == "NO":
        exit()