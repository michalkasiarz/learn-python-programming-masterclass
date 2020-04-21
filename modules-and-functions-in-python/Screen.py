try:
    import tkinter
except ImportError:  # Python 2
    import Tkinter as tkinter

import os

mainWindow = tkinter.Tk()

mainWindow.title("Grid Demo")
mainWindow.geometry("640x480-8-200")

label = tkinter.Label(mainWindow, text="Tkinter Grid Demo")
label.grid(row=0, column=0, columnspan=3)

# column conf added
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=3)
mainWindow.columnconfigure(3, weight=3)
mainWindow.columnconfigure(4, weight=3)

# row conf added
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

# listbox added
fileList = tkinter.Listbox(mainWindow)
fileList.grid(row=1, column=0, sticky="nsew", rowspan=2)
fileList.config(border=2, relief="sunken")

for zone in os.listdir("/Windows/System32"):
    fileList.insert(tkinter.END, zone)

mainWindow.mainloop()
