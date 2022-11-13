from tkinter import ttk
import tkinter as tk
import datetime
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
from theme import style
from ui_utils import *


class treeview_toplevel:
    def __init__(self):
        self.main = tk.Toplevel()
        self.main.title("Insert Selected Data")
        self.rootframe = ttk.Frame(self.main)
        self.tv = ttk.Treeview(master=self.rootframe)

        self.search_textvar = tk.StringVar()

        self.search_cont = ttk.Frame(self.rootframe)
        self.search_field = ttk.Entry(
            self.search_cont, textvariable=self.search_textvar, name="search"
        )
        self.search_btn = ttk.Button(self.search_cont, text="Search")
        self.sel_btn = ttk.Button(
            master=self.rootframe, text="Insert Selected Data", style="accent.TButton"
        )
        self.main.withdraw()

    def config_behaviour(self, sel_cmd, search_cmd, search_field_text="Enter name"):
        self.sel_btn.config(command=sel_cmd)
        self.search_btn.config(command=search_cmd)
        self.search_field.config(name=search_field_text)

    def run(self):
        self.rootframe.pack(fill="both", expand=1, ipadx=6, ipady=6)
        self.tv.pack(fill="both", expand=2, padx=6, pady=4)
        self.search_cont.pack(fill="x", expand=1)
        self.search_btn.pack(side="left", padx=6, pady=4)
        self.search_field.pack(side="right", fill="x", expand=1, padx=6, pady=4)
        self.sel_btn.pack(fill="x", expand=1, padx=6, pady=4, anchor="s")
        self.main.deiconify()


class pos_page:
    def __init__(self, master, root_window):
        self.rootframe = ttk.Frame(master, style="border.TFrame")
        self.note = ttk.Notebook(self.rootframe)

        #########################
        # Customer Details Page #
        #########################
        self.c = ttk.Frame(
            self.note,
        )

        self.cust_reg_lbl = ttk.Label(
            self.c, text="Register New Customer", style="big.TLabel"
        )
        self.cust_reg_lbl.grid(
            row=0, column=0, columnspan=8, padx=6, pady=2, sticky="ew"
        )

        l1 = ttk.Label(self.c, text="Customer Name", style="small.TLabel")
        l1.grid(row=1, column=0, padx=6, pady=2, sticky="sw")

        self.cust_name_entry = ttk.Entry(self.c)
        self.cust_name_entry.grid(
            row=2, column=0, padx=6, pady=2, columnspan=8, sticky="ew"
        )

        l2 = ttk.Label(self.c, text="Age", style="small.TLabel")
        l2.grid(row=3, column=0, padx=6, pady=2, sticky="sw")

        self.cust_age_entry = ttk.Entry(self.c)
        self.cust_age_entry.grid(
            row=4, column=0, padx=6, pady=2, columnspan=3, sticky="ew"
        )

        l3 = ttk.Label(self.c, text="Sex", style="small.TLabel")
        l3.grid(row=3, column=4, padx=6, pady=2, sticky="sw")

        self.cust_sex_entry = ttk.Entry(self.c)
        self.cust_sex_entry.grid(
            row=4, column=4, padx=6, pady=2, columnspan=4, sticky="ew"
        )

        l4 = ttk.Label(self.c, text="Address", style="small.TLabel")
        l4.grid(row=5, column=0, padx=6, pady=2, sticky="sw")

        self.cust_addr_entry = ttk.Entry(self.c)
        self.cust_addr_entry.grid(
            row=6, column=0, padx=6, pady=2, columnspan=8, sticky="ew"
        )

        self.reg_new_cust_btn = ttk.Button(
            self.c,
            text="Register New Customer",
            style="accent.TButton",
            command=self.reg_new_cust,
        )
        self.reg_new_cust_btn.grid(
            row=7, column=0, columnspan=8, padx=6, pady=6, sticky="sew"
        )

        l5 = ttk.Label(self.c, text="or", style="big.TLabel")
        l5.grid(row=8, column=0, columnspan=8, padx=6, pady=2, sticky="ew")

        self.sel_existing_cust_btn = ttk.Button(
            self.c, text="Select Existing Customer", style="accent.TButton"
        )
        self.sel_existing_cust_btn.grid(
            row=9, column=0, columnspan=8, padx=6, pady=6, sticky="sew"
        )
        self.sel_existing_cust_btn.config(command=self.sel_existing_customer)
        grid_config(self.c)

        #########################
        # Medicine Details Page #
        #########################
        self.m = ttk.Frame(master, style="Table.TFrame")

        l1 = ttk.Label(self.m, text="Medicine Name", style="small.TLabel")
        l1.grid(row=0, column=0, padx=6, pady=2, sticky="sw")

        self.med_name_entry = ttk.Entry(self.m)
        self.med_name_entry.grid(
            row=1, column=0, padx=6, pady=2, columnspan=7, sticky="ew"
        )

        self.med_search_btn = ttk.Button(
            self.m,
            text="Search",
        )
        self.med_search_btn.grid(row=1, column=7, padx=6, pady=2, sticky="ne")

        l2 = ttk.Label(self.m, text="Quantity", style="small.TLabel")
        l2.grid(row=2, column=0, padx=6, pady=2, sticky="sw")

        self.qty_entry = ttk.Entry(self.m)
        self.qty_entry.grid(row=3, column=0, padx=6, pady=2, columnspan=8, sticky="sew")

        self.add_sel_btn = ttk.Button(
            self.m, text="Add Selected", style="accent.TButton"
        )
        self.add_sel_btn.grid(
            row=7, column=0, padx=6, pady=8, columnspan=8, sticky="ew"
        )

        grid_config(self.m)

        #########################
        # Payment Details Page #
        #########################
        self.p = ttk.Frame(master)

        l1 = ttk.Label(self.p, text="Payment Date", style="small.TLabel")
        l1.grid(row=0, column=0, padx=6, pady=2, sticky="sw")

        self.datetime_entry = ttk.Entry(self.p)
        self.datetime_entry.grid(
            row=1, column=0, padx=6, pady=2, columnspan=5, sticky="ew"
        )

        self.ct_btn = ttk.Button(
            self.p,
            text="Insert Current Date",
            command=lambda: self.datetime_entry.insert(
                "0", str(datetime.datetime.now().date())
            ),
        )
        self.ct_btn.grid(row=1, column=6, columnspan=3, padx=6, pady=2, sticky="new")

        self.gen_recpt = ttk.Button(
            self.p, text="Generate Receipt", style="accent.TButton"
        )
        self.gen_recpt.grid(row=3, column=0, padx=6, pady=8, columnspan=8, sticky="ew")

        var = tk.StringVar()
        self.payment_method_menu = ttk.OptionMenu(
            self.p, var, *["Cash", "Credit/Debit Card", "UPI"]
        )
        # self.payment_method_menu.config()
        self.payment_method_menu.grid(
            row=2, column=0, padx=6, pady=8, columnspan=8, sticky="ew"
        )

        grid_config(self.p)

        self.note.add(self.c, text="Customer Details")
        self.note.add(self.m, text="Medicines")
        self.note.add(self.p, text="Payment")
        self.note.pack(fill="both", expand=1, padx=10)

        self.n_btn = ttk.Button(
            master=self.rootframe, text="Next >", command=lambda: next_tab(self.note)
        )
        self.n_btn.pack(side="right", anchor="se", padx=26, pady=4)

        self.b_btn = ttk.Button(
            master=self.rootframe, text="< Back", command=lambda: prev_tab(self.note)
        )
        self.b_btn.pack(side="left", anchor="sw", padx=26, pady=4)

        self.rootframe.pack(fill="both", expand=1)

    def sel_existing_customer(self):
        search_attr = "name"

        main = tk.Toplevel()
        main.title("Select Existing Customer")
        rootframe = ttk.Frame(main)
        rootframe.pack(fill="both", expand=1)
        grid_config(rootframe)

        self.cust_table = easy_treeview(rootframe, get_field_names(customers))
        ins_rows_treeview(self.cust_table, get_table(customers))
        self.cust_table.grid(
            row=0, column=0, rowspan=3, columnspan=8, padx=6, pady=6, sticky="nswe"
        )

        l1 = ttk.Label(rootframe, text=f"Enter {search_attr}", style="small.TLabel")
        l1.grid(row=3, column=0, padx=6, pady=2, sticky="sw")

        search_textvar = tk.StringVar()
        search_field = ttk.Entry(rootframe, textvariable=search_textvar)
        search_field.grid(row=4, column=0, columnspan=8, padx=6, pady=2, sticky="swe")

        sel_button = ttk.Button(
            master=rootframe,
            text="Insert Selected Data",
            style="accent.TButton",
            command=self.display_cust_data,
        )
        sel_button.grid(row=5, column=0, columnspan=8, padx=6, pady=6, sticky="swe")

        s = lambda: update_treeview(
            self.cust_table,
            search_by_field(customers, search_attr, search_textvar.get()),
        )
        search_field.config(validate="key", validatecommand=s)

        self.cust_reg_lbl.config(text="Verify Customer Details")
        hide_grid_widget(self.reg_new_cust_btn)

    def display_cust_data(self):
        data = self.cust_table.selection()
        print(data)
        self.cust_name_entry.insert(tk.END, data[1])
        self.cust_age_entry.insert(tk.END, data[2])
        self.cust_sex_entry.insert(tk.END, data[3])
        self.cust_addr_entry.insert(tk.END, data[4])

    def reg_new_cust(self):
        data = {}
        data["name"] = self.cust_name_entry.get()
        data["age"] = self.cust_age_entry.get()
        data["sex"] = self.cust_sex_entry.get()
        data["address"] = self.cust_addr_entry.get()

        insert_from_dict(customers, data)

    def as_tab(self):
        return self.rootframe


class inventory_page:
    def __init__(self, master):
        self.rootframe = ttk.Frame(master)
        self.note = ttk.Notebook(self.rootframe)

        self.c = ttk.Frame(self.note)

        l1 = ttk.Label(self.c, text="Customer Name", style="small.TLabel")
        l1.grid(row=0, column=0, padx=6, pady=2, sticky="sw")

        self.name_entry = ttk.Entry(self.c)
        self.name_entry.grid(row=1, column=0, padx=6, pady=2, columnspan=6, sticky="ew")

        l2 = ttk.Label(self.c, text="Age", style="small.TLabel")
        l2.grid(row=2, column=0, padx=6, pady=2, sticky="sw")

        self.age_entry = ttk.Entry(self.c)
        self.age_entry.grid(row=3, column=0, padx=6, pady=2, columnspan=3, sticky="ew")

        l3 = ttk.Label(self.c, text="Sex", style="small.TLabel")
        l3.grid(row=2, column=4, padx=6, pady=2, sticky="sw")

        self.sex_entry = ttk.Entry(self.c)
        self.sex_entry.grid(row=3, column=4, padx=6, pady=2, columnspan=4, sticky="ew")

        l4 = ttk.Label(self.c, text="Address", style="small.TLabel")
        l4.grid(row=4, column=0, padx=6, pady=2, sticky="sw")

        self.addr_entry = ttk.Entry(self.c)
        self.addr_entry.grid(row=5, column=0, padx=6, pady=2, columnspan=8, sticky="ew")

        self.cust_table = ttk.Treeview(self.c, columns=["a", "b", "c", "d"])
        self.cust_table.grid(row=6, column=0, columnspan=8, rowspan=2)

        grid_config(self.c)

        self.m = ttk.Frame(master)

        l1 = ttk.Label(self.m, text="Medicine Name", style="small.TLabel")
        l1.grid(row=0, column=0, padx=6, pady=2, sticky="sw")

        self.med_name_entry = ttk.Entry(self.m)
        self.med_name_entry.grid(
            row=1, column=0, padx=6, pady=2, columnspan=7, sticky="ew"
        )

        self.med_search_btn = ttk.Button(
            self.m,
            text="Search",
        )
        self.med_search_btn.grid(row=1, column=7, padx=6, pady=2, sticky="ne")

        l2 = ttk.Label(self.m, text="Quantity", style="small.TLabel")
        l2.grid(row=2, column=0, padx=6, pady=2, sticky="sw")

        self.qty_entry = ttk.Entry(self.m)
        self.qty_entry.grid(row=3, column=0, padx=6, pady=2, columnspan=8, sticky="sew")

        self.add_sel_btn = ttk.Button(
            self.m, text="Add Selected", style="accent.TButton"
        )
        self.add_sel_btn.grid(
            row=7, column=0, padx=6, pady=8, columnspan=8, sticky="ew"
        )

        grid_config(self.m)

        self.p = ttk.Frame(master)

        l1 = ttk.Label(self.p, text="Payment Date", style="small.TLabel")
        l1.grid(row=0, column=0, padx=6, pady=2, sticky="sw")

        self.datetime_entry = ttk.Entry(self.p)
        self.datetime_entry.grid(
            row=1, column=0, padx=6, pady=2, columnspan=5, sticky="ew"
        )

        self.ct_btn = ttk.Button(
            self.p,
            text="Insert Current Date",
            command=lambda: self.datetime_entry.insert(
                "0", str(datetime.datetime.now().date())
            ),
        )
        self.ct_btn.grid(row=1, column=6, columnspan=3, padx=6, pady=2, sticky="new")

        self.gen_recpt = ttk.Button(
            self.p, text="Generate Receipt", style="accent.TButton"
        )
        self.gen_recpt.grid(row=3, column=0, padx=6, pady=8, columnspan=8, sticky="ew")

        var = tk.StringVar()
        self.payment_method_menu = ttk.OptionMenu(
            self.p, var, *["Cash", "Credit/Debit Card", "UPI"]
        )
        self.payment_method_menu.grid(
            row=2, column=0, padx=6, pady=8, columnspan=8, sticky="ew"
        )

        grid_config(self.p)

        self.note.add(self.c, text="Customer Details")
        self.note.add(self.m, text="Medicines")
        self.note.add(self.p, text="Payment")
        self.note.pack(fill="both", expand=1, padx=10)

        self.n_btn = ttk.Button(
            master=self.rootframe, text="Next >", command=lambda: next_tab(self.note)
        )
        self.n_btn.pack(side="right", anchor="se", padx=26, pady=4)

        self.b_btn = ttk.Button(
            master=self.rootframe, text="< Back", command=lambda: prev_tab(self.note)
        )
        self.b_btn.pack(side="left", anchor="sw", padx=26, pady=4)

        self.rootframe.pack(fill="both", expand=1)

    def get_cust_data(self):
        data = {}
        data["name"] = self.name_entry.get()
        data["age"] = self.name_entry.get()
        data["sex"] = self.name_entry.get()
        data["addr"] = self.name_entry.get()
        return data

    def as_tab(self):
        return self.rootframe


class about_page:
    def __init__(self, master, root_window):
        self.root_window = root_window
        self.rootframe = ttk.Frame(master)
        l0 = ttk.Label(self.rootframe, text="About", style="big.TLabel")
        l0.pack(padx=20, pady=15, anchor="n", expand=1)
        l1 = ttk.Label(
            self.rootframe,
            text="Made by Subhrojyoti Sen and an unnamed intern at Bajaj Finserv and HRC.",
        )
        l1.pack(padx=20, pady=5, anchor="n", expand=1)
        l2 = ttk.Label(
            self.rootframe, text="Moonlighting is illegal.", style="small.TLabel"
        )
        l2.pack(padx=20, pady=5, anchor="n", expand=1)
        quit_btn = ttk.Button(self.rootframe, text="Quit", command=self.quit_app)
        quit_btn.pack(padx=20, pady=10, anchor="center")

    def quit_app(self):
        close()
        self.root_window.destroy()
        exit()

    def as_tab(self):
        return self.rootframe


if __name__ == "__main__":
    root = tk.Tk()

    s = style(root)

    note = ttk.Notebook(root, style="ribbon.TNotebook")

    p = pos_page(note, root_window=root)
    abt = about_page(master=note, root_window=root)

    note.add(p.as_tab(), text="Point-Of-Sale")
    note.add(abt.as_tab(), text="About")
    note.pack(fill="both", expand=1)

    root.mainloop()
