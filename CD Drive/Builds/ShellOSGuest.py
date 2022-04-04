# FOR MORE INFORMATION ON EDITING THIS OS, LERAN PYTHON.

# IMPORTING THE MOUDULES THAT ARE BUILT IN PYTHON ENVIRONMENT
import sys
import os

# IMPORTING THE PyQt5 MOUDLES
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# MAKING THE MAIN WINDOW FOR THE OS
class ShellOS(QMainWindow):
    def __init__(self):
        super(ShellOS, self).__init__()
        self.real_console = QWebEngineView()
        self.real_console.setUrl(QUrl("https://www.iclarified.com/images/news/76415/76415/76415-1280.jpg"))
        self.setCentralWidget(self.real_console)
        self.create_menu_bar()
        self.showMaximized()

    # DEFINING THE MENU BAR
    def create_menu_bar(self):
        menubar = QMenuBar()
        self.setMenuBar(menubar)

        # POWER MENU
        power_menu = QMenu("Power", self)
        menubar.addMenu(power_menu)

        # SHUT DOWN
        shut_down = QAction(QIcon("paste.png"), "Shut Down", self)
        shut_down.triggered.connect(sys.exit)
        power_menu.addAction(shut_down)

        # RESTART
        restart_os = QAction(QIcon("redo.png"), "Restart", self)
        restart_os.triggered.connect(self.restart_os)
        power_menu.addAction(restart_os)

        # HIBERNATE
        hibernate = QAction(QIcon("paste.png"), "Hibernate", self)
        hibernate.triggered.connect(lambda: self.showMinimized())
        power_menu.addAction(hibernate)

        # SLEEP
        sleep_mode = QAction(QIcon("paste.png"), "Sleep", self)
        sleep_mode.triggered.connect(lambda: self.showNormal())
        power_menu.addAction(sleep_mode)

        # DEFAULT APPS MENU
        default_apps = QMenu("Default Applications", self)
        menubar.addMenu(default_apps)

        # PUTING THE CLOCK APP IN THE MENUBAR
        clock_app = QAction(QIcon("ClockAppIcon.jpg"), "Clock", self)
        clock_app.triggered.connect(self.ask_time)
        default_apps.addAction(clock_app)

        # PUTING THE TEXT EDITOR APP IN THE MENUBAR
        text_editor = QAction(QIcon("NotepadAppIcon.jpg"), "Text Editor", self)
        text_editor.triggered.connect(self.open_text)
        default_apps.addAction(text_editor)

        # PUTING THE CALCULATOR APP IN THE MENUBAR
        calc_operation = QAction(QIcon("CalculatorAppIcon.jpg"), "Calculator", self)
        calc_operation.triggered.connect(self.calculate)
        default_apps.addAction(calc_operation)

        # PUTING THE PAINT APP IN THE MENUBAR
        paint_app = QAction(QIcon("PaintAppIcon.jpg"), "Paint App", self)
        paint_app.triggered.connect(self.draw_image)
        default_apps.addAction(paint_app)

        # PUTING THE BROWSER APP IN THE MENUBAR
        browser_app = QAction(QIcon("WebBrowserIcon.jpg"), "Web Browser", self)
        browser_app.triggered.connect(self.browse_internet)
        default_apps.addAction(browser_app)

        # MAKING A TOOLBAR
        ToolBar = QToolBar("TASKBAR")
        self.addToolBar(ToolBar)

        # PUTING THE CLOCK APP IN THE TOOLBAR
        clock_app = QAction(QIcon("ClockAppIcon.jpg"), "Clock", self)
        clock_app.triggered.connect(self.ask_time)
        ToolBar.addAction(clock_app)

        # PUTING THE TEXT EDITOR APP IN THE TOOLBAR
        text_editor = QAction(QIcon("NotepadAppIcon.jpg"), "Text Editor", self)
        text_editor.triggered.connect(self.open_text)
        ToolBar.addAction(text_editor)

        # PUTING THE CALCULATOR APP IN THE TOOLBAR
        calc_operation = QAction(QIcon("CalculatorAppIcon.jpg"), "Calculator", self)
        calc_operation.triggered.connect(self.calculate)
        ToolBar.addAction(calc_operation)

        # PUTING THE PAINT APP IN THE TOOLBAR
        paint_app = QAction(QIcon("PaintAppIcon.jpg"), "Paint App", self)
        paint_app.triggered.connect(self.draw_image)
        ToolBar.addAction(paint_app)

        # PUTING THE BROWSER APP IN THE TOOLBAR
        browser_app = QAction(QIcon("WebBrowserIcon.jpg"), "Web Browser", self)
        browser_app.triggered.connect(self.browse_internet)
        ToolBar.addAction(browser_app)

        ToolBar.addSeparator()

        # MAKING BACK FUNCTION
        back_btn = QAction(QIcon("cil-arrow-circle-left.png"), "Back", self)
        back_btn.triggered.connect(self.real_console.back)
        ToolBar.addAction(back_btn)
        
        # MAKING FORWARD BUTTON
        forward_btn = QAction(QIcon("cil-arrow-circle-right.png"), "Forward", self)
        forward_btn.triggered.connect(self.real_console.forward)
        ToolBar.addAction(forward_btn)

        # MAKING A SEARCH BAR
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.real_console.urlChanged.connect(self.update_url)
        ToolBar.addWidget(self.url_bar)

        # MAKING RELOAD BUTTON
        reload_btn = QAction(QIcon("cil-reload.png"), "Reload", self)
        reload_btn.triggered.connect(self.real_console.reload)
        ToolBar.addAction(reload_btn)

        # MAKING HOME BUTTON
        home_btn = QAction(QIcon("cil-home.png"), "Home", self)
        home_btn.triggered.connect(self.navigate_home)
        ToolBar.addAction(home_btn)

        self.addToolBar(ToolBar)


    # DEFINING THE FUNCTIONS
    def ask_time(self):
        os.startfile("ClockApp.py")

    def open_text(self):
        os.startfile("WritingDocs.py")

    def calculate(self):
        os.startfile("CalculatorApp.py")

    def draw_image(self):
        os.startfile("PaintApp.py")

    def browse_internet(self):
        os.startfile("MainBrowser.py")

    def microsoft_word(self):
        os.startfile("Word.lnk")

    def microsoft_excel(self):
        os.startfile("Excel.lnk")

    def microsoft_powerpoint(self):
        os.startfile("PowerPoint.lnk")

    def microsoft_outlook(self):
        os.startfile("Outlook.lnk")
    
    def microsoft_onenote(self):
        os.startfile("OneNote.lnk")

    def check_waether(self):
        os.startfile("weather.py")

    def cmd(self):
        os.startfile("Command Prompt.lnk")

    def cmd_successor(self):
        os.startfile("Windows Powershell.lnk")

    def antivurus(self):
        os.startfile("ShellAntivirus.bat")

    def file_manager(self):
        os.startfile("File Manager.py")
    
    def ms_teams(self):
        os.startfile("Microsoft Teams.lnk")

    def folder_settings(self):
        os.startfile("Settings")

    def microsoft_onedrive(self):
        os.startfile("https://www.onedrive.live.com/")

    def google_drive(self):
        os.startfile("https://www.drive.google.com/")

    def note_editor(self):
        os.startfile("Note Edit.py")

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.real_console.setUrl(QUrl(url))

    def navigate_home(self):
        self.real_console.setUrl(QUrl("https://www.iclarified.com/images/news/76415/76415/76415-1280.jpg"))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

    def code_language(self):
        os.startfile("Python 3.10 (64-bit).lnk")

    def sys_file_scanner(self):
        os.startfile("FileScanner.bat")

    # POWER CONTROL FUNCTIONS
    def restart_os(self):
        os.startfile("ShellOSGuest.py")
        os.abort("ShellOSGuest.py")


# MAKING THE CONFIGURATION TO LET THE OS KNOW TO SHOW THE WINDOW
app = QApplication(sys.argv)
QApplication.setApplicationName("Shell OS Guest")
QApplication.setWindowIcon(QIcon("ShellOS Logo.jpg"))
window = ShellOS()
app.exec_()