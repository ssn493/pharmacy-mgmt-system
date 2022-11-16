from loadfont import loadfont_win, loadfont_lin, removefont_lin
import ui
import tkinter as tk
from tkinter import ttk
import os

fbasepath = os.getcwd() + os.path.sep + "assets" + os.path.sep

if os.name == "nt":
    loadfont_win(fbasepath + "Inter-Light.ttf")
    loadfont_win(fbasepath + "Inter-Regular.ttf")
elif os.name == 'posix':
    loadfont_lin(fbasepath+'Inter-Light.ttf')
    loadfont_lin(fbasepath+'Inter-Regular.ttf')
    
#main code
ui.main()

if os.name == 'posix':
    removefont_lin(fbasepath+'Inter-Light.ttf')
    removefont_lin(fbasepath+'Inter-Regular.ttf')