try:
    import tkinter
except ImportError:     # Python 2
    import Tkinter as tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Grid Demo")
mainWindow.geometry("640x480-8-200")

label = tkinter.Label(mainWindow, text="Tkinter Grid Demo")
label.grid(row=0, column=0, columnspan=3)

mainWindow.mainloop()
