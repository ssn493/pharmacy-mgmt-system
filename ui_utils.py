import tkinter as tk
from tkinter import ttk
from pharmacy_backend import get_med_quantity
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
        self.menu_frame = ttk.Frame(self.root_frame, style="NavMenu.TFrame")
        self.menu_frame.pack(side="left", fill="both", expand=0, anchor="w")
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

        self.menu_img = tk.PhotoImage(
            master=self.root_frame,
            file="".join(
                [os.getcwd(), os.path.sep, "assets", os.path.sep, "menu_dark_btn.png"]
            ),
            name="menu_btn_image",
        )
        print(
            os.path.isfile(
                "".join(
                    [
                        os.getcwd(),
                        os.path.sep,
                        "assets",
                        os.path.sep,
                        "menu_dark_btn.png",
                    ]
                )
            )
        )
        self.menu_show_btn = ttk.Button(
            self.root_frame,
            image=self.menu_img,
            text="Menu",
            command=self.toggle_menu,
            style="menubtn.TButton",
        )
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

    def add(self, frame, text=None, custom_cmd=None):
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
            style="NavMenu.TButton",
        )
        if custom_cmd == None:
            menu_btn.config(command=lambda: self.show_frame(frame_index))
        else:
            menu_btn.config(command=custom_cmd)
        menu_btn.pack(fill="x", padx=0, ipadx=4, pady=0, ipady=4)
        self.menu_btn_widgets.append(menu_btn)

    def prev_page(self):
        if self.current_frame_index == 0:
            pass
        else:
            self.show_frame(self.current_frame_index - 1)

    def next_page(self):
        if self.current_frame_index == len(obj) - 1:
            pass
        else:
            self.show_frame(self.current_frame_index + 1)

    def pack(self, **pack_info):
        self.root_frame.pack(**pack_info)
        if self.content_frame_buffer != []:
            self.show_frame(0)


class HorizontalNavMenu:
    def __init__(self, master):
        self.root_frame = ttk.Frame(master)
        self.menu_frame = ttk.Frame(self.root_frame, style="NavMenu.TFrame")
        self.menu_frame.lift()
        self.menu_frame.pack(
            side="top", fill="none", expand=0, anchor="center", padx=15, pady=15
        )
        self.menu_data_widget = widget_packdata_fmt(self.menu_frame)

        self.content_frame = ttk.Frame(self.root_frame, style="verticalNavMenu.TFrame")
        self.content_frame.pack(
            side="top",
            fill="both",
            expand=1,
            ipady=4,
            ipadx=4,
        )

        self.current_frame_index = -1
        self.content_frame_buffer = []
        self.menu_btn_widgets = []
        self.pack_info = {"fill": "both", "expand": 1}

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

    def add(self, frame, text=None, custom_cmd=None):
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
            style="NavMenu.TButton",
        )
        if custom_cmd == None:
            menu_btn.config(command=lambda: self.show_frame(frame_index))
        else:
            menu_btn.config(command=custom_cmd)
        menu_btn.pack(
            side="left", fill="y", padx=0, ipadx=20, pady=0, ipady=4, anchor="center"
        )
        self.menu_btn_widgets.append(menu_btn)

    def toggle_menu(self):
        toggle_packed_widget(self.menu_data_widget)

    def prev_page(self):
        if self.current_frame_index <= 0:
            pass
        else:
            self.show_frame(self.current_frame_index - 1)

    def next_page(self):
        if self.current_frame_index >= len(self.content_frame_buffer) - 1:
            pass
        else:
            self.show_frame(self.current_frame_index + 1)

    def pack(self, **pack_info):
        self.root_frame.pack(**pack_info)
        if self.content_frame_buffer != []:
            self.show_frame(0)


class Table:
    def __init__(self, root, columns):
        self.rootframe = ttk.Frame(root)
        grid_config(self.rootframe, cols=len(columns))
        self.num_rows = 0
        self.num_cols = len(columns)
        self.row_widgets = []
        # code for creating table
        for j in range(self.num_cols):

            h = ttk.Label(root, text=columns[j], style='THeading.TLabel')
            h.grid(row=self.num_rows, column=j, sticky="we")

    def ins_row(self, lst):
        self.num_rows += 1
        col_widgets = []
        for j in range(self.num_cols):

            e = ttk.Entry(self.rootframe)
            e.grid(row=self.num_rows, column=j, sticky="we", style='Table.TEntry')
            e.insert(END, lst[j])
            col_widgets.append(e)
        self.row_widgets.append(col_widgets)

    def grid(**kwargs):
        self.rootframe.grid(**kwargs)

class medTable:
    def __init__(self, root, columns=['Name', 'Qty', 'Availability']):
        self.rootframe = ttk.Frame(root)
        grid_config(self.rootframe, cols=len(columns))
        self.rootframe.grid_columnconfigure(0, weight=3)
        self.num_rows = 0
        self.num_cols = 3
        self.row_widgets = []
    
        # code for creating table
        for j in range(self.num_cols):

            h = ttk.Label(self.rootframe, text=columns[j], style='THeading.TLabel')
            h.grid(row=self.num_rows, column=j, sticky="we")

        self.data = []

    def ins_row(self, lst):
        self.num_rows += 1
        col_widgets = []

        l = ttk.Label(self.rootframe, text=lst[0])
        l.grid(row=self.num_rows, column=0, sticky="we")

        e = ttk.Entry(self.rootframe, style='Table.TEntry')
        e.grid(row=self.num_rows, column=1, sticky="we")

        c = ttk.Button(self.rootframe,text='Check', style='accent.TButton', command=lambda: self.check_med_availability(l, e))
        e.grid(row=self.num_rows, column=1, sticky="we")

        col_widgets.append(self.num_rows)
        col_widgets.append(l)
        col_widgets.append(e)
        col_widgets.append(c)
        self.row_widgets.append(col_widgets)
        self.data.append(lst)

    def check_med_availability(self, med_name_lbl,qty_entry ):
        if int(qty_entry.get()) < get_med_quantity(med_name_entry['text']):
            med_name_lbl['style'] = 'success.TLabel'
        else:
            med_name_lbl['style'] = 'error.TLabel'

    def grid(self,**kwargs):
        self.rootframe.grid(**kwargs)
