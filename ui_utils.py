import tkinter as tk
from tkinter import ttk
import os


def grid_config(root, rows=8, cols=8):
    i = 0
    while i < cols:
        root.grid_columnconfigure(i, weight=1, minsize=40)
        i += 1


def widget_packdata_fmt(widget):
    hidden_widget = {}
    hidden_widget["widget"] = widget
    hidden_widget["packinfo"] = widget.pack_info()
    hidden_widget["hidden"] = False
    return hidden_widget


def hide_packed_widget(hidden_widget):
    hidden_widget["widget"].pack_forget()
    hidden_widget["hidden"] = True
    return hidden_widget


def show_packed_widget(hidden_widget):
    hidden_widget["widget"].pack(hidden_widget["packinfo"])
    hidden_widget["hidden"] = False
    return hidden_widget


def toggle_packed_widget(hidden_widget):
    if hidden_widget["hidden"]:
        show_packed_widget(hidden_widget)
    else:
        hide_packed_widget(hidden_widget)


def hide_grid_widget(widget):
    widget.grid_remove()


def show_grid_widget(widget):
    widget.grid()


def next_tab(notebk):
    all_tabs = notebk.tabs()
    sel_tab = notebk.select()

    if sel_tab == all_tabs[-1]:
        pass
    else:
        i = all_tabs.index(sel_tab)
        notebk.select(all_tabs[i + 1])


def prev_tab(notebk):
    all_tabs = notebk.tabs()
    sel_tab = notebk.select()

    if sel_tab == all_tabs[0]:
        pass
    else:
        i = all_tabs.index(sel_tab)
        notebk.select(all_tabs[i - 1])


def easy_treeview(master, columns):
    tv = ttk.Treeview(master=master, columns=columns, show="headings")

    for column in columns:
        tv.column(column, width=100, anchor="c", stretch=tk.YES)
        tv.heading(column, text=str(column))

    return tv


def ins_row_treeview(tv, row_data):
    num_rows = len(tv.get_children())
    tv.insert(parent="", index=num_rows, iid=num_rows, values=row_data)


def ins_rows_treeview(tv, rows):
    num_rows = len(tv.get_children())
    i = 0
    for row in rows:
        tv.insert(parent="", index=num_rows + i, iid=num_rows + i, values=row)
        i += 1


def update_treeview(tv, updated_data):
    for item in tv.get_children():
        tv.delete(item)
    ins_rows_treeview(tv, updated_data)


class VerticalNavMenu:
    def __init__(self, master, menu_button=False):
        self.root_frame = ttk.Frame(master)
        self.menu_button_flag = menu_button
        self.menu_frame = ttk.Frame(self.root_frame, style="verticalNavMenu.TFrame")
        self.menu_frame.pack(side="left", fill="both", expand=1, anchor="w")
        self.menu_data_widget = widget_packdata_fmt(self.menu_frame)

        self.content_frame = ttk.Frame(self.root_frame, style="verticalNavMenu.TFrame")
        self.content_frame.pack(
            side="right",
            fill="both",
            expand=7,
            ipady=4,
            ipadx=4,
        )

        self.current_frame_index = -1
        self.content_frame_buffer = []
        self.menu_btn_widgets = []
        self.pack_info = {"fill": "both", "expand": 1}

        if self.menu_button_flag:
            self.toggle_menu_button()
    
    def toggle_menu_button(self):
        menu_img = tk.PhotoImage(file=os.getcwd()+os.path.sep+'assets'+os.path.sep+"menu_dark_btn.png")
        self.menu_show_btn = ttk.Button(
            self.root_frame,
            image=menu_img,
            text="Menu",
            command=self.toggle_menu,
            style="menubtn.TButton",
        )
        self.menu_show_btn.image = menu_img
        self.menu_show_btn.lift()
        self.menu_show_btn.pack(in_=self.root_frame, anchor="nw")


    def toggle_menu(self):
        toggle_packed_widget(self.menu_data_widget)

    def show_frame(self, frame_index):
        if frame_index != self.current_frame_index:
            current_frame_data_widget = self.content_frame_buffer[
                self.current_frame_index
            ]
            frame_data_widget = self.content_frame_buffer[frame_index]

            hide_packed_widget(current_frame_data_widget)
            show_packed_widget(frame_data_widget)
            self.menu_btn_widgets[self.current_frame_index].state(["!pressed"])
            self.menu_btn_widgets[frame_index].state(["pressed"])
            self.current_frame_index = frame_index
            if self.menu_button_flag:
                self.toggle_menu()

    def add(self, frame, text=None):
        if not isinstance(text, str):
            raise Exception("Entered text is not valid")

        frame_index = len(self.content_frame_buffer)
        frame.pack(**self.pack_info)
        frame_data_widget = {
            "widget": frame,
            "packinfo": self.pack_info,
            "hidden": False,
        }
        hide_packed_widget(frame_data_widget)
        self.content_frame_buffer.append(frame_data_widget)

        menu_btn = ttk.Button(
            self.menu_frame,
            text=text,
            command=lambda: self.show_frame(frame_index),
            style="verticalNavMenu.TButton",
        )
        menu_btn.pack(fill="x", padx=0, ipadx=4, pady=0, ipady=4)
        self.menu_btn_widgets.append(menu_btn)

    def pack(self, **pack_info):
        self.root_frame.pack(**pack_info)
        if self.content_frame_buffer != []:
            self.show_frame(0)
