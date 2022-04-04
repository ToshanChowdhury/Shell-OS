from tkinter import *
import os

def OpenWord():
    os.startfile("https://1drv.ms/u/s!Ag6ZJEd83-sghKR8_xJYhZi6aUHhJA?e=f3L1Td")

def Vira():
    os.startfile("https://1drv.ms/u/s!Ag6ZJEd83-sghJ9bEwYtB4fWhWQpEA?e=4iIVxE")

def Python_Cloud_OS():
    os.startfile("https://1drv.ms/u/s!Ag6ZJEd83-sghJ56HNGjeqASMwMujQ?e=3BVrBK")

def GMT_Repair_OS():
    os.startfile("https://1drv.ms/u/s!Ag6ZJEd83-sghJ55_BdKq6frmhSyig?e=ybfWDy")

def TkFileMan():
    os.startfile("https://1drv.ms/u/s!Ag6ZJEd83-sghKYq2AbgOd7NxUGA4A?e=lOkKj8")

def LibreOffice():
    os.startfile("https://github.com/LibreOffice")

def OpenOffice():
    os.startfile("https://github.com/apache/openoffice")

def ONLYOFFICE():
    os.startfile("https://github.com/ONLYOFFICE")

def andriod():
    os.startfile("https://github.com/android")

def HarmoyOS():
    os.startfile("https://github.com/Awesome-HarmonyOS/HarmonyOS")

def PyQt5():
    os.startfile("https://github.com/PyQt5")

def PyQt4():
    os.startfile("https://github.com/Werkov/PyQt4")

def PyQtWebEngine():
    os.startfile("https://github.com/qt/qtwebengine?msclkid=e0d3e57cadbf11eca971816f2eb709c0")

def OpenCV():
    os.startfile("https://www.github.com/opencv/opencv")

def easygui():
    os.startfile("https://github.com/robertlugg/easygui")

def requests():
    os.startfile("https://www.github.com/requests")

def psutil():
    os.startfile("https://github.com/giampaolo/psutil")

def TkinterApp():
    os.startfile("https://github.com/python/cpython/tree/main/Lib/tkinter")

def more_command():
    os.startfile("storescreen2.py")

window = Tk()
window.title("Projects Store")
window.state("zoomed")

head_title = Label(window, text="Shell Project Store", font=("Segoe UI", 20))
head_title.pack()

btn_1 = Button(window, text="OpenWord", font=("Segoe UI", 11), command=OpenWord)
btn_1.pack()

btn_2 = Button(window, text="Vira", font=("Segoe UI", 11), command=Vira)
btn_2.pack()

btn_3 = Button(window, text="Python Cloud OS", font=("Segoe UI", 11), command=Python_Cloud_OS)
btn_3.pack()

btn_4 = Button(window, text="GMT Repair OS", font=("Segoe UI", 11), command=GMT_Repair_OS)
btn_4.pack()

btn_5 = Button(window, text="TkFileMan", font=("Segoe UI", 11), command=TkFileMan)
btn_5.pack()

btn_6 = Button(window, text="LibreOffice", font=("Segoe UI", 11), command=LibreOffice)
btn_6.pack()

btn_7 = Button(window, text="OpenOffice", font=("Segoe UI", 11), command=OpenOffice)
btn_7.pack()

btn_8 = Button(window, text="ONLYOFFICE", font=("Segoe UI", 11), command=ONLYOFFICE)
btn_8.pack()

btn_9 = Button(window, text="Google Android", font=("Segoe UI", 11), command=andriod)
btn_9.pack()

btn_10 = Button(window, text="Huawei Harmony OS", font=("Segoe UI", 11), command=HarmoyOS)
btn_10.pack()

btn_11 = Button(window, text="PyQt5", font=("Segoe UI", 11), command=PyQt5)
btn_11.pack()

btn_12 = Button(text="PyQt4", font=("Segoe UI", 11), command=PyQt4)
btn_12.pack()

btn_13 = Button(text="PyQtWebEngine", font=("Segoe UI", 11), command=PyQtWebEngine)
btn_13.pack()

btn_14 = Button(text="Open-CV", font=("Segoe UI", 11), command=OpenCV)
btn_14.pack()

btn_15 = Button(text="EasyGui", font=("Segoe UI", 11), command=easygui)
btn_15.pack()

btn_16 = Button(text="Requests", font=("Segoe UI", 11), command=requests)
btn_16.pack()

btn_17 = Button(text="Psutil", font=("Segoe UI", 11), command=psutil)
btn_17.pack()

btn_18 = Button(text="Tkinter", font=("Segoe UI", 11), command=TkinterApp)
btn_18.pack()

more_btn = Button(text="More >>", font=("Segoe UI", 11), command=more_command)
more_btn.pack(side=RIGHT)

window.mainloop()