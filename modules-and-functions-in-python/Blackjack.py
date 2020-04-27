# Blackjack card game

import random

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


mainWindow = tkinter.Tk()

# Set up the screen and frames for the dealer and player

mainWindow.title("Black Jack")
mainWindow.geometry("640x480")
