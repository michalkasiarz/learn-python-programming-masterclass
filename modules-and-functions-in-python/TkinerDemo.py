# Tkiner demo

try:
    import tkinter
except ImportError:     # Python 2
    import Tkinter as tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Hello world!")
mainWindow.geometry("640x480+800+400")

label = tkinter.Label(mainWindow, text="Hello world!")
label.pack(side="top")

canvas = tkinter.Canvas(mainWindow, relief="raised", borderwidth=1)
canvas.pack(side="left")

mainWindow.mainloop()
