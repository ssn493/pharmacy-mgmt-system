from loadfont import loadfont_win, loadfont_lin, removefont_lin
import ui
import tkinter as tk
from tkinter import ttk
import os

fbasepath = os.getcwd() + os.path.sep + "assets" + os.path.sep

if os.name == "nt":
    loadfont_win(f'{fbasepath}Inter-Light.ttf')
    loadfont_win(f"{fbasepath}Inter-Medium.ttf")
    loadfont_win(f"{fbasepath}Inter-Regular.ttf")
elif os.name == 'posix':
    loadfont_lin(f'{fbasepath}Inter-Medium.ttf')
    loadfont_lin(f'{fbasepath}Inter-Regular.ttf')
    loadfont_lin(f'{fbasepath}Inter-Medium.ttf')

#main code
ui.devel_run_pages()

if os.name == 'posix':
    removefont_lin(f'{fbasepath}Inter-Medium.ttf')
    removefont_lin(f'{fbasepath}Inter-Light.ttf')
    removefont_lin(f'{fbasepath}Inter-Regular.ttf')