from loadfont import loadfont_win, loadfont_lin, removefont_lin
from theme import style
from pharmacy_backend import (
    meds,
    customers,
    get_field_names,
    search_by_field,
    search_cust_by_name,
    get_table,
    insert_from_dict,
    close,
)
import ui_utils as utils
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
root = ui.main()

s = style(root)
# a = login_page(root)

note = utils.VerticalNavMenu(root, menu_button=True)

# order = (note.content_frame, root_window=root)
abt = ui.about_page(master=note.content_frame, root_window=root)

# note.add(order.as_tab(), text="New Order")
note.add(abt.as_tab(), text="About")
note.add(ui.empty_page, text="Quit", custom_cmd=abt.quit_app)
note.pack(fill="both", expand=1)

root.mainloop()

if os.name == 'posix':
    removefont_lin(fbasepath+'Inter-Light.ttf')
    removefont_lin(fbasepath+'Inter-Regular.ttf')