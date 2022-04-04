from tkinter import *
import os

window = Tk()
window.title("Screen 2")
window.state("zoomed")

def PyAudio():
    os.startfile("https://github.com/jleb/pyaudio")

btn_19 = Button(text="PyAudio", font=("Segoe UI", 11), command=PyAudio)
btn_19.pack()

window.mainloop()