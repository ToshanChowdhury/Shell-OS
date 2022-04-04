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

        # SLEEP
        sleep = QAction(QIcon("paste.png"), "Sleep", self)
        sleep.triggered.connect(lambda: self.showNormal())
        power_menu.addAction(sleep)

        # HIBERNATE
        hibernate = QAction(QIcon("paste.png"), "Hibernate", self)
        hibernate.triggered.connect(lambda: self.showMinimized())
        power_menu.addAction(hibernate)

        # USER ACCOUNT MENU
        user_account_menu = QMenu("User Account", self)
        menubar.addMenu(user_account_menu)

        user_account = QAction(QIcon("UserAccount.png"), "UserAccount", self)
        user_account.triggered.connect(self.user_account)
        user_account_menu.addAction(user_account)

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

        # ADITIONAL APPS
        apps = QMenu("Applications", self)
        menubar.addMenu(apps)

        # MICROSOFT WORD
        word_app = QAction(QIcon("Microsoft Word Logo.png"), "Microsoft Word", self)
        word_app.triggered.connect(self.microsoft_word)
        apps.addAction(word_app)

        # MICROSOFT EXCEL
        excel_app = QAction(QIcon("Microsoft Excel Logo.png"), "Microsoft Excel", self)
        excel_app.triggered.connect(self.microsoft_excel)
        apps.addAction(excel_app)

        # MICROSOFT POWERPOINT
        powerpoint_app = QAction(QIcon("Microsoft PowerPoint Logo.png"), "Microsoft PowerPoint", self)
        powerpoint_app.triggered.connect(self.microsoft_powerpoint)
        apps.addAction(powerpoint_app)

        # MICROSOFT OUTLOOK
        outlook_app = QAction(QIcon("Micosoft Outlook Logo.jpg"), "Microsoft Outlook", self)
        outlook_app.triggered.connect(self.microsoft_outlook)
        apps.addAction(outlook_app)

        # MICROSOFT ONENOTE
        onenote_app = QAction(QIcon("Microsoft OneNote Logo.png"), "Microsoft OneNote", self)
        onenote_app.triggered.connect(self.microsoft_onenote)
        apps.addAction(onenote_app)

        # WEATHER
        weather_app = QAction(QIcon("Weather Logo.png"), "Weather", self)
        weather_app.triggered.connect(self.check_waether)
        apps.addAction(weather_app)

        # COMMAND PROMPT
        command_reciver = QAction(QIcon("Windows Terminal Logo.png"), "Command Prompt", self)
        command_reciver.triggered.connect(self.cmd)
        apps.addAction(command_reciver)

        # POWERSHELL
        powershell = QAction(QIcon("Windows Powershell Logo.jpg"), "Windows Powershell", self)
        powershell.triggered.connect(self.cmd_successor)
        apps.addAction(powershell)

        # FILE MANAGER
        file_manager = QAction(QIcon("open-file.png"), "Shell File Manager", self)
        file_manager.triggered.connect(self.file_manager)
        apps.addAction(file_manager)

        # PYTHON LANGUAGE
        python_code = QAction(QIcon("Python Logo.png"), "Python 3.10", self)
        python_code.triggered.connect(self.code_language)
        apps.addAction(python_code)

        # FILE SCANNER
        file_scanner = QAction(QIcon("left-align.png"), "File Scanner", self)
        file_scanner.triggered.connect(self.sys_file_scanner)
        apps.addAction(file_scanner)

        # NOTES APP
        notes_app = QAction(QIcon("doc_icon.png"), "Notes", self)
        notes_app.triggered.connect(self.note_editor)
        apps.addAction(notes_app)

        # MICROSOFT TEAMS
        microsoft_teams = QAction(QIcon("Microsoft Teams Logo.png"), "Microsoft Teams", self)
        microsoft_teams.triggered.connect(self.ms_teams)
        apps.addAction(microsoft_teams)

        # ONEDRIVE WEB
        onedrive_web = QAction(QIcon("OneDrive Logo.jpeg"), "Microsoft OneDrive", self)
        onedrive_web.triggered.connect(self.microsoft_onedrive)
        apps.addAction(onedrive_web)

        # GOOGLE DRIVE
        google_drive_web = QAction(QIcon("Google Drive Logo.png"), "Google Drive", self)
        apps.addAction(google_drive_web)

        # ANTIVIRUS
        antivirus = QAction(QIcon("cil-lock-locked.png"), "Antivirus", self)
        antivirus.triggered.connect(self.antivurus)
        apps.addAction(antivirus)

        # UTLITIES MENU
        utilities = QMenu("Utilities", self)
        menubar.addMenu(utilities)

        # SETTINGS APP
        settings_utility = QAction(QIcon("cil-settings.png"), "Settings", self)
        settings_utility.triggered.connect(self.folder_settings)
        utilities.addAction(settings_utility)

        # UPDATE OS
        update_os = QAction(QIcon("redo.png"), "Update OS", self)
        update_os.triggered.connect(self.update_os)
        utilities.addAction(update_os)

        # WEB APPLICATIONS MENU
        web_apps = QMenu("Web Applications", self)
        menubar.addMenu(web_apps)

        # WORD WEB
        word = QAction(QIcon("Microsoft Word Logo.png"), "Microsoft Word Web", self)
        word.triggered.connect(self.word_web)
        web_apps.addAction(word)

        # EXCEL WEB
        excel = QAction(QIcon("Microsoft Excel Logo.png"), "Microsoft Excel Web", self)
        excel.triggered.connect(self.excel_web)
        web_apps.addAction(excel)

        # POWERPOINT
        powerpoint = QAction(QIcon("Microsoft PowerPoint Logo.png"), "Microsoft PowerPoint Web", self)
        powerpoint.triggered.connect(self.powerpoint_web)
        web_apps.addAction(powerpoint)

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

    def user_account(self):
        os.startfile("UserProfiles.py")

    def update_os(self):
        os.startfile("UpdateFile.py")

    # POWER CONTROL FUNCTIONS
    def restart_os(self):
        os.startfile("ShellOS.py")
        os.abort("ShellOS.py")

    # WEB APPS
    def word_web(self):
        os.startfile("https://www.office.com/launch/word")

    def excel_web(self):
        os.startfile("https://www.office.com/launch/excel")

    def powerpoint_web(self):
        os.startfile("https://www.office.com/launch/powerpoint")


# MAKING THE CONFIGURATION TO LET THE OS KNOW TO SHOW THE WINDOW
app = QApplication(sys.argv)
QApplication.setApplicationName("Shell OS")
QApplication.setWindowIcon(QIcon("ShellOS Logo.jpg"))
window = ShellOS()
app.exec_()
