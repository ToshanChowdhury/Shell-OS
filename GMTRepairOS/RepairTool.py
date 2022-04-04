from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import os
import winsound
import sys



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.PS = QWebEngineView()
        self.setCentralWidget(self.PS)
        self.showMaximized()

        # NAVIGATION BAR
        navbar = QToolBar("Navigation Bar")
        self.addToolBar(navbar)

        code_editor = QAction(QIcon("VSCODE.png"), "Code Editor", self)
        code_editor.triggered.connect(self.vscode)
        navbar.addAction(code_editor)

        reinstall = QAction(QIcon("REINSTALL.png"), "Reinstall OS", self)
        reinstall.triggered.connect(self.linktoshellos)
        navbar.addAction(reinstall)

        exit = QAction(QIcon("SHUTDOWN.png"), "Shut Down", self)
        exit.triggered.connect(sys.exit)
        navbar.addAction(exit)

        restart = QAction(QIcon("redo.png"), "Restart", self)
        restart.triggered.connect(self.restart)
        navbar.addAction(restart)

        beeping = QAction(QIcon("left-align.png"), "Beep", self)
        beeping.triggered.connect(self.beep)
        navbar.addAction(beeping)

        test = QAction(QIcon("left-align.png"), "Load", self)
        test.triggered.connect(self.icons)
        navbar.addAction(test)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.url_to_go_to)
        navbar.addWidget(self.url_bar)

    def vscode(self):
        os.startfile("Visual Studio Code.lnk")

    def linktoshellos(self):
        os.startfile("https://1drv.ms/u/s!Ag6ZJEd83-sgg-FPD56w745nB7xjwA?e=Qb6uJb")

    def url_to_go_to(self):
        url = self.url_bar.text()
        self.PS.setUrl(QUrl(url))

    def restart(self):
        file = "RepairTool.py"
        os.startfile(file)
        os.abort(file)

    def beep(self):
        winsound.Beep(3000, 1000)
        winsound.Beep(3000, 1000)
        winsound.Beep(3000, 1000)
        winsound.Beep(3000, 1000)
        winsound.Beep(3000, 1000)
        winsound.Beep(3000, 1000)
        winsound.Beep(3000, 1000)
        winsound.Beep(3000, 1000)
        winsound.Beep(3000, 1000)
        winsound.Beep(3000, 1000)

    def icons(self):
        os.startfile("GCalendar.png")
        os.startfile("GChats.png")
        os.startfile("GClassroom.png")
        os.startfile("GDocs.png")
        os.startfile("GForms.png")
        os.startfile("GLE Chrome.jpg")
        os.startfile("GMail.png")
        os.startfile("GMaps.png")
        os.startfile("GMeet.png")
        os.startfile("Google books.png")

app = QApplication(sys.argv)
QApplication.setApplicationName("Shell RepOS")
window = MainWindow()
app.exec_()