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
canvas.pack(side="top")

button1 = tkinter.Button(mainWindow, text="button1")
button2 = tkinter.Button(mainWindow, text="button2")
button3 = tkinter.Button(mainWindow, text="button3")

button1.pack(side="top", anchor="n")
button2.pack(side="top", anchor="s")
button3.pack(side="top", anchor="e")

mainWindow.mainloop()
