# Tkiner demo

try:
    import tkinter
except ImportError:     # Python 2
    import Tkinter as tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Hello world!")
mainWindow.geometry("640x480-8-200")

label = tkinter.Label(mainWindow, text="Hello world!")
label.grid(row=0, column=0)

# left frame
leftFrame = tkinter.Frame(mainWindow)
leftFrame.grid(row=1, column=1)

# canvas
canvas = tkinter.Canvas(leftFrame, relief="raised", borderwidth=1)
canvas.grid(row=1, column=0)

# right frame
rightFrame = tkinter.Frame(mainWindow)
rightFrame.grid(row=1, column=2, sticky="n")

button1 = tkinter.Button(rightFrame, text="button1")
button2 = tkinter.Button(rightFrame, text="button2")
button3 = tkinter.Button(rightFrame, text="button3")

button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)

# configure the columns
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.grid_columnconfigure(2, weight=1)

leftFrame.config(relief="sunken", borderwidth=1)
rightFrame.config(relief="sunken", borderwidth=1)
leftFrame.grid(sticky="ns")
rightFrame.grid(sticky="new")

rightFrame.columnconfigure(0, weight=1)
button2.grid(sticky="ew")
mainWindow.mainloop()
