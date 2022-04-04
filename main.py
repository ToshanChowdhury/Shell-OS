# LIBRARIES
$ pip install PyQt5
$ pip install PyQtWebEngine
$ pip install easygui
$ pip install sip
$ pip install requests
$ pip install psutil

# FOR MORE INFORMATION ON EDITING THIS OS, LERAN PYTHON.
# THE .vscode FOLDER IS IMPORTANT, THE FILES IN THE FOLDER IS USED TO TEST THIS OPERATING SYSTEM.

# FOR MORE INFORMATION ON EDITING THIS OS, LERAN PYTHON.
# THE .vscode FOLDER IS IMPORTANT, THE FILES IN THE FOLDER IS USED TO TEST THIS OPERATING SYSTEM.

# IMPORTING THE MOUDULES THAT ARE BUILT IN PYTHON ENVIRONMENT
import sys
import os

# IMPORTING THE PyQt5 AND OTHER MOUDLES
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from datetime import *
import psutil

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = str(battery.percent)
plugged_str = "Plugged In" if plugged else "Not Plugged In"
login_username = open("CD Drive/UsersData/username.user")
l_username = login_username.read()
today = datetime.now()
d4 = today.strftime("%d/%m/%Y  %H:%M %p")
d3 = today.strftime("%H:%M %p")
d2 = today.strftime("%d/%m/%Y")

# MAKING THE MAIN WINDOW FOR THE OS
class ShellOS(QMainWindow):
    def __init__(self):
        super(ShellOS, self).__init__()
        self.real_console = QWebEngineView()
        self.real_console.setUrl(QUrl("https://www.iclarified.com/images/news/76415/76415/76415-1280.jpg"))
        self.setCentralWidget(self.real_console)
        self.showMaximized()

    # DEFINING THE MENU BAR
        menubar = QMenuBar()
        self.setMenuBar(menubar)

        # START MENU
        l_username_menu = QMenu("👤"+l_username, self)
        menubar.addMenu(l_username_menu)

        logout = QAction(QIcon("paste.png"), "Log Out", self)
        logout.triggered.connect(self.exit)
        l_username_menu.addAction(logout)

        start_menu = QMenu("Start", self)
        menubar.addMenu(start_menu)

        # POWER MENU
        power_menu = QMenu("Power", self)
        start_menu.addMenu(power_menu)

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
        start_menu.addMenu(user_account_menu)

        user_account = QAction(QIcon("UserAccount.png"), "UserAccount", self)
        user_account.triggered.connect(self.user_account)
        user_account_menu.addAction(user_account)

        # DEFAULT APPS MENU
        default_apps = QMenu("Default Apps", self)
        start_menu.addMenu(default_apps)

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

        # PUTING THE OPENWORD PROGRAM IN THE MENU BAR
        open_word = QAction(QIcon("MainIcon.ico"), "OpenWord", self)
        open_word.triggered.connect(self.open_word)
        default_apps.addAction(open_word)

        # ADITIONAL APPS
        apps = QMenu("Apps", self)
        start_menu.addMenu(apps)

        # MICROSOFT OFFICE MENU
        ms_office_menu = QMenu("Microsoft Office", self)
        apps.addMenu(ms_office_menu)

        # MICROSOFT WORD
        word_app = QAction(QIcon("Microsoft Word Logo.png"), "Microsoft Word", self)
        word_app.triggered.connect(self.microsoft_word)
        ms_office_menu.addAction(word_app)

        # MICROSOFT EXCEL
        excel_app = QAction(QIcon("Microsoft Excel Logo.png"), "Microsoft Excel", self)
        excel_app.triggered.connect(self.microsoft_excel)
        ms_office_menu.addAction(excel_app)

        # MICROSOFT POWERPOINT
        powerpoint_app = QAction(QIcon("Microsoft PowerPoint Logo.png"), "Microsoft PowerPoint", self)
        powerpoint_app.triggered.connect(self.microsoft_powerpoint)
        ms_office_menu.addAction(powerpoint_app)

        # MICROSOFT OUTLOOK
        outlook_app = QAction(QIcon("Micosoft Outlook Logo.jpg"), "Microsoft Outlook", self)
        outlook_app.triggered.connect(self.microsoft_outlook)
        ms_office_menu.addAction(outlook_app)

        # MICROSOFT ONENOTE
        onenote_app = QAction(QIcon("Microsoft OneNote Logo.png"), "Microsoft OneNote", self)
        onenote_app.triggered.connect(self.microsoft_onenote)
        ms_office_menu.addAction(onenote_app)

        # WEATHER
        weather_app = QAction(QIcon("Weather Logo.png"), "Weather", self)
        weather_app.triggered.connect(self.check_waether)
        apps.addAction(weather_app)

        # MAIN TOOLS SUBMENU
        main_tools = QMenu("Main Tools", self)
        apps.addMenu(main_tools)

        # COMMAND PROMPT
        command_reciver = QAction(QIcon("Windows Terminal Logo.png"), "Command Prompt", self)
        command_reciver.triggered.connect(self.cmd)
        main_tools.addAction(command_reciver)

        # POWERSHELL
        powershell = QAction(QIcon("Windows Powershell Logo.jpg"), "Windows Powershell", self)
        powershell.triggered.connect(self.cmd_successor)
        main_tools.addAction(powershell)

        # FILE MANAGER
        file_manager = QAction(QIcon("open-file.png"), "Shell File Manager", self)
        file_manager.triggered.connect(self.file_manager)
        main_tools.addAction(file_manager)

        # PYTHON LANGUAGE
        python_code = QAction(QIcon("Python Logo.png"), "Python 3.10", self)
        python_code.triggered.connect(self.code_language)
        main_tools.addAction(python_code)

        # FILE SEARCH
        file_search = QAction(QIcon("open-file.png"), "File Search", self)
        file_search.triggered.connect(self.file_search)
        main_tools.addAction(file_search)

        # NOTES APP
        notes_app = QAction(QIcon("doc_icon.png"), "Notes", self)
        notes_app.triggered.connect(self.note_editor)
        main_tools.addAction(notes_app)

        # SHELL CMD
        shell_cmd = QAction(QIcon("Windows Terminal Logo.png"), "Shell Command Prompt", self)
        shell_cmd.triggered.connect(self.ShellCMD)
        main_tools.addAction(shell_cmd)

        # SHELL STORE
        shell_store = QAction(QIcon("Shell Store.png"), "Shell OS Store", self)
        shell_store.triggered.connect(self.shell_store)
        main_tools.addAction(shell_store)

        # MICROSOFT TEAMS
        microsoft_teams = QAction(QIcon("Microsoft Teams Logo.png"), "Microsoft Teams", self)
        microsoft_teams.triggered.connect(self.ms_teams)
        apps.addAction(microsoft_teams)

        # ONLINE STORAGE
        oneline_storage_menu = QMenu("Online Cloud Storage", self)
        apps.addMenu(oneline_storage_menu)

        # ONEDRIVE WEB
        onedrive_web = QAction(QIcon("OneDrive Logo.jpeg"), "Microsoft OneDrive", self)
        onedrive_web.triggered.connect(self.microsoft_onedrive)
        oneline_storage_menu.addAction(onedrive_web)

        # GOOGLE DRIVE
        google_drive_web = QAction(QIcon("Google Drive Logo.png"), "Google Drive", self)
        google_drive_web.triggered.connect(self.google_drive)
        oneline_storage_menu.addAction(google_drive_web)

        # ANTIVIRUS MENU
        antivirus_menu = QMenu("Antivirus Menu", self)
        apps.addMenu(antivirus_menu)

        # ANTIVIRUS
        antivirus = QAction(QIcon("cil-lock-locked.png"), "Antivirus", self)
        antivirus.triggered.connect(self.antivurus)
        antivirus_menu.addAction(antivirus)

        # AVAST FREE ANTIVIRUS
        avast_free = QAction(QIcon("cil-lock-locked.png"), "Avast Free Antivirus", self)
        avast_free.triggered.connect(self.advanced_antivirus)
        antivirus_menu.addAction(avast_free)

        # FILE SCANNER
        file_scanner = QAction(QIcon("left-align.png"), "File Scanner", self)
        file_scanner.triggered.connect(self.sys_file_scanner)
        antivirus_menu.addAction(file_scanner)

        # FREE OFFICE MENU
        freeoffice_menu = QMenu("FreeOffice", self)
        apps.addMenu(freeoffice_menu)

        # FREEOFFICE TEXTMAKER
        textmaker_free = QAction(QIcon("TextMaker.png"), "FreeOffice TextMaker", self)
        textmaker_free.triggered.connect(self.freeoffice_textmaker)
        freeoffice_menu.addAction(textmaker_free)

        # FREEOFFICE PLANMAKER
        planmaker_free = QAction(QIcon("PlanMaker.png"), "FreeOffice PlanMaker", self)
        planmaker_free.triggered.connect(self.freeoffice_planmaker)
        freeoffice_menu.addAction(planmaker_free)

        # FREEOFFICE PRESENTATIONS
        presentations_free = QAction(QIcon("Presentations.png"), "FreeOffice Presentations", self)
        presentations_free.triggered.connect(self.freeoffice_presentations)
        freeoffice_menu.addAction(presentations_free)

        # ONLYOFFICE
        onlyoffice_menu = QMenu("ONLYOFFICE", self)
        apps.addMenu(onlyoffice_menu)

        # ONLYOFFICE DESKTOP EDITORS
        onlyoffice = QAction(QIcon("ONLYOFFICE.jfif"), "ONLYOFFICE Desktop Editors", self)
        onlyoffice.triggered.connect(self.onlyoffice_desktop_editors)
        onlyoffice_menu.addAction(onlyoffice)

        # GOOGLE CHROME
        chrome_app = QAction(QIcon("GLE Chrome.jpg"), "Google Chrome", self)
        chrome_app.triggered.connect(self.chrome_broswer)
        apps.addAction(chrome_app)

        # PYTHON CLOUD
        python_cloud = QAction(QIcon("ShellOS Logo.jpg"), "Python Cloud", self)
        python_cloud.triggered.connect(self.pythoncloud)
        apps.addAction(python_cloud) 

        # REPAIR OS
        repair_os = QAction(QIcon("RepairIcon.png"), "GMT Repair OS", self)
        repair_os.triggered.connect(self.repair)
        apps.addAction(repair_os)

        # WINDOWS TOOLS
        windows_tools = QMenu("Windows Tools", self)
        apps.addMenu(windows_tools)

        # WORDPAD
        wordpad = QAction(QIcon("Worpad Icon.png"), "WordPad", self)
        wordpad.triggered.connect(self.WordPad)
        windows_tools.addAction(wordpad)

        # NOTEPAD
        notepad = QAction(QIcon("NotepadIcon.png"), "Notepad", self)
        notepad.triggered.connect(self.notepad)
        windows_tools.addAction(notepad)

        # CALCULATOR
        windows_calculator = QAction(QIcon("CalculatorAppIcon.jpg"), "Calculator", self)
        windows_calculator.triggered.connect(self.win_calc)
        windows_tools.addAction(windows_calculator)

        # PAINT
        windows_paint = QAction(QIcon("PaintAppIcon.jpg"), "Paint", self)
        windows_paint.triggered.connect(self.mspaint)
        windows_tools.addAction(windows_paint)

        # SNIPPING TOOL
        snipping_tool = QAction(QIcon("cut.png"), "Snipping Tool", self)
        snipping_tool.triggered.connect(self.snip_tool)
        windows_tools.addAction(snipping_tool)

        # UTLITIES MENU
        utilities = QMenu("Utilities", self)
        start_menu.addMenu(utilities)

        # SETTINGS APP
        settings_utility = QAction(QIcon("cil-settings.png"), "Settings", self)
        settings_utility.triggered.connect(self.folder_settings)
        utilities.addAction(settings_utility)

        # UPDATE OS
        update_os = QAction(QIcon("redo.png"), "Update OS", self)
        update_os.triggered.connect(self.update_os)
        utilities.addAction(update_os)

        # SFC
        sfc_file_checker = QAction("Repair Tool", self)
        sfc_file_checker.triggered.connect(self.sfc_tool)
        utilities.addAction(sfc_file_checker)

        # WEB Apps MENU
        web_apps = QMenu("Web Apps", self)
        start_menu.addMenu(web_apps)

        microsoft_apps = QMenu("Microsoft Web Apps", self)
        web_apps.addMenu(microsoft_apps)

        # WORD WEB
        word = QAction(QIcon("Microsoft Word Logo.png"), "Microsoft Word Web", self)
        word.triggered.connect(self.word_web)
        microsoft_apps.addAction(word)

        # EXCEL WEB
        excel = QAction(QIcon("Microsoft Excel Logo.png"), "Microsoft Excel Web", self)
        excel.triggered.connect(self.excel_web)
        microsoft_apps.addAction(excel)

        # POWERPOINT WEB
        powerpoint = QAction(QIcon("Microsoft PowerPoint Logo.png"), "Microsoft PowerPoint Web", self)
        powerpoint.triggered.connect(self.powerpoint_web)
        microsoft_apps.addAction(powerpoint)

        # Google Web Apps MENU
        google_apps = QMenu("Google Apps", self)
        web_apps.addMenu(google_apps)

        # GOOGLE BOOKS
        google_books = QAction(QIcon("Google books.png"), "Google Books", self)
        google_books.triggered.connect(self.google_books)
        google_apps.addAction(google_books)

        # GOOGLE
        google = QAction(QIcon("Google Icon.png"), "Google", self)
        google.triggered.connect(self.google_search)
        google_apps.addAction(google)

        # YOUTUBE
        youtube = QAction(QIcon("YouTube Logo.jpg"), "YouTube", self)
        youtube.triggered.connect(self.you_tube)
        google_apps.addAction(youtube)

        # GOOGLE DOCS
        google_docs = QAction(QIcon("GDocs.png"), "Google Docs", self)
        google_docs.triggered.connect(self.docs)
        google_apps.addAction(google_docs)

        # GOOGLE SHEETS
        google_sheets = QAction(QIcon("GSheets.png"), "Google Sheets", self)
        google_sheets.triggered.connect(self.sheets)
        google_apps.addAction(google_sheets)

        # GOOGLE SLIDES
        google_slides = QAction(QIcon("GSlides.png"), "Google Slides", self)
        google_slides.triggered.connect(self.slides)
        google_apps.addAction(google_slides)

        # GOOGLE FORMS
        google_forms = QAction(QIcon("GForms.png"), "Google Forms", self)
        google_forms.triggered.connect(self.forms)
        google_apps.addAction(google_forms)

        # GOOGLE MAPS
        google_maps = QAction(QIcon("GMaps.png"), "Google Maps", self)
        google_maps.triggered.connect(self.maps)
        google_apps.addAction(google_maps)

        # GOOGLE CLASSROOM
        google_classroom = QAction(QIcon("GClassroom.png"), "Google Classroom", self)
        google_classroom.triggered.connect(self.classroom)
        google_apps.addAction(google_classroom)

        # GOOGLE CHAT
        google_chat = QAction(QIcon("GChats.png"), "Google Chat", self)
        google_chat.triggered.connect(self.chat)
        google_apps.addAction(google_chat)

        # GOOGLE MEET
        google_meet = QAction(QIcon("GMeet.png"), "Google Meet", self)
        google_meet.triggered.connect(self.meet)
        google_apps.addAction(google_meet)

        # GOOGLE MAIL
        google_mail = QAction(QIcon("GMail.png"), "Google Mail", self)
        google_mail.triggered.connect(self.mail)
        google_apps.addAction(google_mail)

        # GOOGLE CALENDAR
        google_calendar = QAction(QIcon("GCalendar.png"), "Google Calendar", self)
        google_calendar.triggered.connect(self.calendar)
        google_apps.addAction(google_calendar)

        # GOOGLE PHOTOS
        google_photos = QAction(QIcon("GPhotos.png"), "Google Photos", self)
        google_photos.triggered.connect(self.photos)
        google_apps.addAction(google_photos)

        # GOOGLE TRANSLATE
        google_translate = QAction(QIcon("GTranslate.png"), "Google Translate", self)
        google_translate.triggered.connect(self.translate)
        google_apps.addAction(google_translate)

        # BING
        bing = QAction(QIcon("Bing Logo.png"), "Bing", self)
        bing.triggered.connect(self.bing_search)
        web_apps.addAction(bing)

        # ONLYOFFICE WEB
        onlyoffice_web = QAction(QIcon("onlyoffice.jfif"), "OnlyOffice", self)
        onlyoffice_web.triggered.connect(self.onlyofficeweb)
        web_apps.addAction(onlyoffice_web)

        # OUTLOOK.COM
        outlook_com = QAction(QIcon("Micosoft Outlook Logo.jpg"), "Outlook", self)
        outlook_com.triggered.connect(self.outlookweb)
        web_apps.addAction(outlook_com)

        # BOOKMARKS MENU
        bookmarks = QMenu("Bookmarks", self)
        start_menu.addMenu(bookmarks)

        empty = QAction("(Empty)", self)
        bookmarks.addAction(empty)

        # SHORTCUTS MENU
        shortcuts = QMenu("Shortcuts", self)
        start_menu.addMenu(shortcuts)

        clock_app = QAction(QIcon("ClockAppIcon.jpg"), "Clock", self)
        clock_app.triggered.connect(self.ask_time)
        shortcuts.addAction(clock_app)

        # MAKING A TOOLBAR
        ToolBar = QToolBar("TASKBAR")
        self.addToolBar(Qt.LeftToolBarArea, ToolBar)

        # VIRA ASSISTANT
        vira = QAction(QIcon("Vira.png"), "Vira", self)
        vira.triggered.connect(self.vira_assistant)
        ToolBar.addAction(vira)

        ToolBar.addSeparator()

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

        # PUTHING THE FILE MANAGER IN THE TOOLBAR
        file_manager = QAction(QIcon("open-file.png"), "Shell File Manager", self)
        file_manager.triggered.connect(self.file_manager)
        ToolBar.addAction(file_manager)

        # PUTING THE COMMAND PROMPT IN THE TOOLBAR
        command_reciver = QAction(QIcon("Windows Terminal Logo.png"), "Command Prompt", self)
        command_reciver.triggered.connect(self.ShellCMD)
        ToolBar.addAction(command_reciver)

        # PUTING THE POWERSHELL APP IN THE TOOLBAR
        powershell = QAction(QIcon("Windows Powershell Logo.jpg"), "Windows Powershell", self)
        powershell.triggered.connect(self.cmd_successor)
        ToolBar.addAction(powershell)

        # PUTING THE SHELL STORE IN THE TOOLBAR
        shell_store = QAction(QIcon("Shell Store.png"), "Shell OS Store", self)
        shell_store.triggered.connect(self.shell_store)
        ToolBar.addAction(shell_store)

        # SEARCH TOOLBAR
        search_bar = QToolBar("Search Toolbar", self)
        self.addToolBar(search_bar)

        # MAKING BACK FUNCTION
        back_btn = QAction(QIcon("cil-arrow-circle-left.png"), "Back", self)
        back_btn.triggered.connect(self.real_console.back)
        search_bar.addAction(back_btn)
        
        # MAKING FORWARD BUTTON
        forward_btn = QAction(QIcon("cil-arrow-circle-right.png"), "Forward", self)
        forward_btn.triggered.connect(self.real_console.forward)
        search_bar.addAction(forward_btn)

        # MAKING A SEARCH BAR
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.real_console.urlChanged.connect(self.update_url)
        search_bar.addWidget(self.url_bar)

        # MAKING RELOAD BUTTON
        reload_btn = QAction(QIcon("cil-reload.png"), "Reload", self)
        reload_btn.triggered.connect(self.real_console.reload)
        search_bar.addAction(reload_btn)

        # MAKING HOME BUTTON
        home_btn = QAction(QIcon("cil-home.png"), "Home", self)
        home_btn.triggered.connect(self.navigate_home)
        search_bar.addAction(home_btn)

        # WEB APPLICATIONS TOOLBAR
        web_apps = QToolBar("Web Applications", self)
        self.addToolBar(Qt.BottomToolBarArea, web_apps)

        # WORD WEB
        word = QAction(QIcon("Microsoft Word Logo.png"), "Microsoft Word Web", self)
        word.triggered.connect(self.word_web)
        web_apps.addAction(word)

        # EXCEL WEB
        excel = QAction(QIcon("Microsoft Excel Logo.png"), "Microsoft Excel Web", self)
        excel.triggered.connect(self.excel_web)
        web_apps.addAction(excel)

        # POWERPOINT WEB
        powerpoint = QAction(QIcon("Microsoft PowerPoint Logo.png"), "Microsoft PowerPoint Web", self)
        powerpoint.triggered.connect(self.powerpoint_web)
        web_apps.addAction(powerpoint)

        # GOOGLE BOOKS
        google_books = QAction(QIcon("Google books.png"), "Google Books", self)
        google_books.triggered.connect(self.google_books)
        web_apps.addAction(google_books)

        # GOOGLE
        google = QAction(QIcon("Google Icon.png"), "Google", self)
        google.triggered.connect(self.google_search)
        web_apps.addAction(google)

        # YOUTUBE
        youtube = QAction(QIcon("YouTube Logo.jpg"), "YouTube", self)
        youtube.triggered.connect(self.you_tube)
        web_apps.addAction(youtube)

        # GOOGLE DOCS
        google_docs = QAction(QIcon("GDocs.png"), "Google Docs", self)
        google_docs.triggered.connect(self.docs)
        web_apps.addAction(google_docs)

        # GOOGLE SHEETS
        google_sheets = QAction(QIcon("GSheets.png"), "Google Sheets", self)
        google_sheets.triggered.connect(self.sheets)
        web_apps.addAction(google_sheets)

        # GOOGLE SLIDES
        google_slides = QAction(QIcon("GSlides.png"), "Google Slides", self)
        google_slides.triggered.connect(self.slides)
        web_apps.addAction(google_slides)

        # GOOGLE FORMS
        google_forms = QAction(QIcon("GForms.png"), "Google Forms", self)
        google_forms.triggered.connect(self.forms)
        web_apps.addAction(google_forms)

        # GOOGLE MAPS
        google_maps = QAction(QIcon("GMaps.png"), "Google Maps", self)
        google_maps.triggered.connect(self.maps)
        web_apps.addAction(google_maps)

        # GOOGLE CLASSROOM
        google_classroom = QAction(QIcon("GClassroom.png"), "Google Classroom", self)
        google_classroom.triggered.connect(self.classroom)
        web_apps.addAction(google_classroom)

        # GOOGLE CHAT
        google_chat = QAction(QIcon("GChats.png"), "Google Chat", self)
        google_chat.triggered.connect(self.chat)
        web_apps.addAction(google_chat)

        # GOOGLE MEET
        google_meet = QAction(QIcon("GMeet.png"), "Google Meet", self)
        google_meet.triggered.connect(self.meet)
        web_apps.addAction(google_meet)

        # GOOGLE MAIL
        google_mail = QAction(QIcon("GMail.png"), "Google Mail", self)
        google_mail.triggered.connect(self.mail)
        web_apps.addAction(google_mail)

        # GOOGLE CALENDAR
        google_calendar = QAction(QIcon("GCalendar.png"), "Google Calendar", self)
        google_calendar.triggered.connect(self.calendar)
        web_apps.addAction(google_calendar)

        # GOOGLE PHOTOS
        google_photos = QAction(QIcon("GPhotos.png"), "Google Photos", self)
        google_photos.triggered.connect(self.photos)
        web_apps.addAction(google_photos)

        # GOOGLE TRANSLATE
        google_translate = QAction(QIcon("GTranslate.png"), "Google Translate", self)
        google_translate.triggered.connect(self.translate)
        web_apps.addAction(google_translate)

        # BING
        bing = QAction(QIcon("Bing Logo.png"), "Bing", self)
        bing.triggered.connect(self.bing_search)
        web_apps.addAction(bing)

        # ONLYOFFICE WEB
        onlyoffice_web = QAction(QIcon("onlyoffice.jfif"), "OnlyOffice", self)
        onlyoffice_web.triggered.connect(self.onlyofficeweb)
        web_apps.addAction(onlyoffice_web)

        # OUTLOOK.COM
        outlook_com = QAction(QIcon("Micosoft Outlook Logo.jpg"), "Outlook", self)
        outlook_com.triggered.connect(self.outlookweb)
        web_apps.addAction(outlook_com)

        # TIME TOOLBAR
        time_toolbar = QToolBar("Time", self)
        self.addToolBar(Qt.BottomToolBarArea, time_toolbar)

        date = QAction(d2, self)
        date.setFont(QFont("Segoe UI Variable Display", 11))
        time_toolbar.addAction(date)

        time = QAction(d3, self)
        time.setFont(QFont("Segoe UI Variable Display", 11))
        time_toolbar.addAction(time)

        time_toolbar.addSeparator()

        wifi = QAction("Wi-Fi: ShellOS-Server", self)
        wifi.setFont(QFont("Segoe UI Variable Display", 11))
        time_toolbar.addAction(wifi)

        volume = QAction("Volume: 100%", self)
        volume.setFont(QFont("Segoe UI Variable Display", 11))
        time_toolbar.addAction(volume)

        battery = QAction("Battery: "+plugged_str+" "+percent+"%", self)
        battery.setFont(QFont("Segoe UI Variable Display", 11))
        time_toolbar.addAction(battery)

        # APPS TOOLBAR
        apps = QToolBar("Apps", self)
        self.addToolBar(Qt.RightToolBarArea, apps)

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

        # FILE SEARCH
        file_search = QAction(QIcon("open-file.png"), "File Search", self)
        file_search.triggered.connect(self.file_search)
        apps.addAction(file_search)

        # NOTES APP
        notes_app = QAction(QIcon("doc_icon.png"), "Notes", self)
        notes_app.triggered.connect(self.note_editor)
        apps.addAction(notes_app)

        # SHELL CMD
        shell_cmd = QAction(QIcon("Windows Terminal Logo.png"), "Shell Command Prompt", self)
        shell_cmd.triggered.connect(self.ShellCMD)
        apps.addAction(shell_cmd)

        # SHELL STORE
        shell_store = QAction(QIcon("Shell Store.png"), "Shell OS Store", self)
        shell_store.triggered.connect(self.shell_store)
        apps.addAction(shell_store)

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
        google_drive_web.triggered.connect(self.google_drive)
        apps.addAction(google_drive_web)

        # ANTIVIRUS
        antivirus = QAction(QIcon("cil-lock-locked.png"), "Antivirus", self)
        antivirus.triggered.connect(self.antivurus)
        apps.addAction(antivirus)

        # AVAST FREE ANTIVIRUS
        avast_free = QAction(QIcon("cil-lock-locked.png"), "Avast Free Antivirus", self)
        avast_free.triggered.connect(self.advanced_antivirus)
        apps.addAction(avast_free)

        # FILE SCANNER
        file_scanner = QAction(QIcon("left-align.png"), "File Scanner", self)
        file_scanner.triggered.connect(self.sys_file_scanner)
        apps.addAction(file_scanner)

        # FREEOFFICE TEXTMAKER
        textmaker_free = QAction(QIcon("TextMaker.png"), "FreeOffice TextMaker", self)
        textmaker_free.triggered.connect(self.freeoffice_textmaker)
        apps.addAction(textmaker_free)

        # FREEOFFICE PLANMAKER
        planmaker_free = QAction(QIcon("PlanMaker.png"), "FreeOffice PlanMaker", self)
        planmaker_free.triggered.connect(self.freeoffice_planmaker)
        apps.addAction(planmaker_free)

        # FREEOFFICE PRESENTATIONS
        presentations_free = QAction(QIcon("Presentations.png"), "FreeOffice Presentations", self)
        presentations_free.triggered.connect(self.freeoffice_presentations)
        apps.addAction(presentations_free)

        # ONLYOFFICE DESKTOP EDITORS
        onlyoffice = QAction(QIcon("ONLYOFFICE.jfif"), "ONLYOFFICE Desktop Editors", self)
        onlyoffice.triggered.connect(self.onlyoffice_desktop_editors)
        apps.addAction(onlyoffice)

        # GOOGLE CHROME
        chrome_app = QAction(QIcon("GLE Chrome.jpg"), "Google Chrome", self)
        chrome_app.triggered.connect(self.chrome_broswer)
        apps.addAction(chrome_app)

        # PYTHON CLOUD
        python_cloud = QAction(QIcon("ShellOS Logo.jpg"), "Python Cloud", self)
        python_cloud.triggered.connect(self.pythoncloud)
        apps.addAction(python_cloud) 

        # REPAIR OS
        repair_os = QAction(QIcon("RepairIcon.png"), "GMT Repair OS", self)
        repair_os.triggered.connect(self.repair)
        apps.addAction(repair_os)

        # WORDPAD
        wordpad = QAction(QIcon("Worpad Icon.png"), "WordPad", self)
        wordpad.triggered.connect(self.WordPad)
        apps.addAction(wordpad)

        # NOTEPAD
        notepad = QAction(QIcon("NotepadIcon.png"), "Notepad", self)
        notepad.triggered.connect(self.notepad)
        apps.addAction(notepad)

        # CALCULATOR
        windows_calculator = QAction(QIcon("CalculatorAppIcon.jpg"), "Calculator", self)
        windows_calculator.triggered.connect(self.win_calc)
        apps.addAction(windows_calculator)

        # PAINT
        windows_paint = QAction(QIcon("PaintAppIcon.jpg"), "Paint", self)
        windows_paint.triggered.connect(self.mspaint)
        apps.addAction(windows_paint)

        # SNIPPING TOOL
        snipping_tool = QAction(QIcon("cut.png"), "Snipping Tool", self)
        snipping_tool.triggered.connect(self.snip_tool)
        apps.addAction(snipping_tool)

        # LIBRARIES MENU
        libraries_menu = QMenu("Libraries", self)
        menubar.addMenu(libraries_menu)

        # DOCUMENTS
        documents = QAction(QIcon("FolderIcon.png"), "Documents", self)
        documents.triggered.connect(self.documents)
        libraries_menu.addAction(documents)

        # PICTURES
        pictures = QAction(QIcon("FolderIcon.png"), "Pictures", self)
        pictures.triggered.connect(self.pictures)
        libraries_menu.addAction(pictures)

        # VIDEOS
        videos = QAction(QIcon("FolderIcon.png"), "Videos", self)
        videos.triggered.connect(self.videos)
        libraries_menu.addAction(videos)

        # DOWNLOADS
        downloads = QAction(QIcon("FolderIcon.png"), "Downloads", self)
        downloads.triggered.connect(self.downloads)
        libraries_menu.addAction(downloads)

        # DATE AND TIME
        date_time_menu = QMenu(d4, self)
        menubar.addMenu(date_time_menu)

        settings = QAction(QIcon("ClockAppIcon.jpg"), "Settings", self)
        settings.triggered.connect(self.ask_time)
        date_time_menu.addAction(settings)


    # DEFINING THE FUNCTIONS
    def close_current_tab(self, i):
 
        # if there is only one tab
        if self.tabs.count() < 2:
            # do nothing
            return
 
        # else remove the tab
        self.tabs.removeTab(i)

    def add_new_tab(self, qurl = None, label ="Blank"):
 
        # if url is blank
        if qurl is None:
            # creating a google url
            qurl = QUrl('http://www.google.com')
 
        # creating a QWebEngineView object
        browser = QWebEngineView()
 
        # setting url to browser
        browser.setUrl(qurl)
 
        # setting tab index
        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)
 
        # adding action to the browser when url is changed
        # update the url
        browser.urlChanged.connect(lambda qurl, browser = browser:
                                   self.update_urlbar(qurl, browser))
 
        # adding action to the browser when loading is finished
        # set the tab title
        browser.loadFinished.connect(lambda _, i = i, browser = browser:
                                     self.tabs.setTabText(i, browser.page().title()))

    def tab_open_doubleclick(self, i):
 
        # checking index i.e
        # No tab under the click
        if i == -1:
            # creating a new tab
            self.add_new_tab()

    def current_tab_changed(self, i):
 
        # get the curl
        qurl = self.tabs.currentWidget().url()
 
        # update the url
        self.update_url(qurl, self.tabs.currentWidget())
 
        # update the title
        self.update_url(self.tabs.currentWidget())

    def repair(self):
        os.startfile("RepairTool.py")

    def snip_tool(self):
        os.startfile("SnippingTool.exe")

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

    def notepad(self):
        os.startfile("notepad.exe.lnk")

    def win_calc(self):
        os.startfile("calc.exe.lnk")

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

    def mspaint(self):
        os.startfile("mspaint.exe.lnk")

    def microsoft_onedrive(self):
        self.real_console.setUrl(QUrl("https://www.onedrive.live.com/"))

    def google_drive(self):
        self.real_console.setUrl(QUrl("https://accounts.google.com/signin/v2/identifier?service=wise&passive=true&continue=http%3A%2F%2Fdrive.google.com%2F%3Futm_source%3Den&utm_medium=button&utm_campaign=web&utm_content=gotodrive&usp=gtd&ltmpl=drive&flowName=GlifWebSignIn&flowEntry=ServiceLogin"))

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

    def advanced_antivirus(self):
        os.startfile("Avast Free Antivirus.lnk")

    def freeoffice_textmaker(self):
        os.startfile("TextMaker.lnk")
    
    def freeoffice_planmaker(self):
        os.startfile("PlanMaker.lnk")

    def freeoffice_presentations(self):
        os.startfile("Presentations.lnk")

    def onlyoffice_desktop_editors(self):
        os.startfile("ONLYOFFICE Editors.lnk")

    def chrome_broswer(self):
        os.startfile("Google Chrome.lnk")

    def WordPad(self):
        os.startfile("Wordpad.lnk")

    def file_search(self):
        os.startfile("File Search.bat")

    def ShellCMD(self):
        os.startfile("CMD.py")

    def documents(self):
        os.startfile("C:/Users/Family/OneDrive/Desktop/Toshan/Shell OS/CD Drive/UsersData/Documents")

    def pictures(self):
        os.startfile("C:/Users/Family/OneDrive/Desktop/Toshan/Shell OS/CD Drive/UsersData/Pictures")

    def downloads(self):
        os.startfile("C:/Users/Family/OneDrive/Desktop/Toshan/Shell OS/CD Drive/UsersData/Downloads")

    def videos(self):
        os.startfile("C:/Users/Family/OneDrive/Desktop/Toshan/Shell OS/CD Drive/UsersData/Videos")

    def shell_store(self):
        os.startfile("store.py")

    # POWER CONTROL FUNCTIONS
    def restart_os(self):
        var = "ShellOS.py"
        os.startfile(var)
        os.abort(var)
    
    def exit(self):
        sys.exit()

    # WEB APPS
    def bing_search(self):
        self.real_console.setUrl(QUrl("https://www.bing.com"))

    def google_search(self):
        self.real_console.setUrl(QUrl("https://www.google.com"))

    def you_tube(self):
        self.real_console.setUrl(QUrl("https://www.youtube.com/"))

    def word_web(self):
        self.real_console.setUrl(QUrl("https://www.office.com/launch/word"))

    def excel_web(self):
        self.real_console.setUrl(QUrl("https://www.office.com/launch/excel"))

    def powerpoint_web(self):
        self.real_console.setUrl(QUrl("https://www.office.com/launch/powerpoint"))

    def google_books(self):
        self.real_console.setUrl(QUrl("https://books.google.com/?hl=en&tab=rp"))

    def docs(self):
        self.real_console.setUrl(QUrl("https://www.google.com/docs"))

    def sheets(self):
        self.real_console.setUrl(QUrl("https://www.google.com/sheets"))

    def slides(self):
        self.real_console.setUrl(QUrl("https://www.google.com/slides"))

    def forms(self):
        self.real_console.setUrl(QUrl("https://www.google.com/forms"))

    def maps(self):
        self.real_console.setUrl(QUrl("https://www.google.com/maps"))

    def classroom(self):
        self.real_console.setUrl(QUrl("https://www.google.com/classroom"))

    def chat(self):
        self.real_console.setUrl(QUrl("https://mail.google.com/chat/u/0/"))

    def meet(self):
        self.real_console.setUrl(QUrl("https://www.google.com/meet"))

    def mail(self):
        self.real_console.setUrl(QUrl("https://www.gmail.com/"))

    def calendar(self):
        self.real_console.setUrl(QUrl("https://www.google.com/calendar"))

    def photos(self):
        self.real_console.setUrl(QUrl("https://www.google.com/photos"))
        
    def translate(self):
        self.real_console.setUrl(QUrl("https://www.google.com/translate"))

    def outlookweb(self):
        self.real_console.setUrl(QUrl("https://www.outlook.com"))

    def pythoncloud(self):
        os.startfile("PythonCloudOS.py")

    def onlyofficeweb(self):
        self.real_console.setUrl(QUrl("https://www.onlyoffice.com"))

    def open_word(self):
        os.startfile("C:/Users/Family/OneDrive/Desktop/Toshan/Shell OS/OpenWord 2/OpenWord 2.exe")

    # VIRA
    def vira_assistant(self):
        os.startfile("virassitant.py")

    # REAPIR OS
    def sfc_tool(self):
        os.startfile("RepairTool.bat - Admin")

    def dism_tool(self):
        os.startfile("DISM.bat")


# MAKING THE CONFIGURATION TO LET THE OS KNOW TO SHOW THE WINDOW
app = QApplication(sys.argv)
 
# setting name to the application
app.setApplicationName("Shell OS 2204")

# setting icon to the application
app.setWindowIcon(QIcon("ShellOS Logo.ico"))
 
# creating Window object
window = ShellOS()
 
# loop
app.exec_()
