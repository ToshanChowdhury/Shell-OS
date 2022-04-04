from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.font import Font
from tkinter.scrolledtext import *
from MenuSystem import file_menu
from MenuSystem import edit_menu
from MenuSystem import format_menu
from MenuSystem import help_menu

root = Tk()

root.title("WritingDocs Untitled File")
root.geometry("300x300+300+300")
root.minsize(width=100, height=100)

text = ScrolledText(root, state='normal', height=400, width=400, wrap='word', pady=2, padx=3, undo=True)
text.pack(fill=Y, expand=1)
text.focus_set()

menubar = Menu(root)

file_menu.main(root, text, menubar)
edit_menu.main(root, text, menubar)
format_menu.main(root, text, menubar)
help_menu.main(root, text, menubar)
root.mainloop()
