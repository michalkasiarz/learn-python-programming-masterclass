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

# left frame
leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side="left", anchor="n", fill=tkinter.Y, expand=False)

# canvas
canvas = tkinter.Canvas(leftFrame, relief="raised", borderwidth=1)
canvas.pack(side="left", anchor="n")

# right frame
rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side="right", anchor="n", expand=True)

button1 = tkinter.Button(rightFrame, text="button1")
button2 = tkinter.Button(rightFrame, text="button2")
button3 = tkinter.Button(rightFrame, text="button3")

button1.pack(side="top", anchor="n")
button2.pack(side="top", anchor="s")
button3.pack(side="top", anchor="e")

mainWindow.mainloop()
