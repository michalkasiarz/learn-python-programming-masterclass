# Tkiner demo

try:
    import tkinter
except ImportError:     # Python 2
    import Tkinter as tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

# tkinter._test()

mainWindow = tkinter.Tk()

mainWindow.title("Hello world!")
mainWindow.geometry("640x480")
mainWindow.mainloop()
