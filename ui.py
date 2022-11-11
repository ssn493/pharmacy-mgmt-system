from tkinter import ttk
import tkinter as tk
import datetime
from pharmacy_backend import meds, customers
from theme import style


def grid_config(root, rows=8, cols=8):
    i = 0
    while i < cols:
        root.grid_columnconfigure(i, weight=1, minsize=40)
        i += 1


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


def easy_treeview(master, columns):
    tv = ttk.Treeview(master=master, columns=columns, show="headings")

    for column in columns:
        tv.column(column, width=100, anchor="c", stretch=tk.YES)
        tv.heading(column, text=str(column))

    return tv


def ins_row_treeview(tv, row_data):
    tv = ttk.Treeview()
    num_rows = len(tv.get_children())
    tv.insert(parent="", index=num_rows, iid=num_rows)


def ins_rows_treeview(tv, rows):
    tv = ttk.Treeview()
    num_rows = len(tv.get_children())
    i = 0
    for row in rows:
        tv.insert(parent="", index=num_rows + i, iid=num_rows + i)
        i += 1


def sel_data_dialog(table,search_attr):
    main = tk.Toplevel()
    main.title("Insert Selected Data")
    rootframe = ttk.Frame(self.main)
    grid_config(rootframe)

    tv = easy_treeview(master, columns)
    tv.grid(row=0 ,column=0 , rowspan=3 ,columnspan=8, padx=6, pady=6, sticky='nswe')

    l1 = ttk.Label(self.rootframe, text=f"Enter {search_attr}")
    l1.grid(row=3, column=0, )

    search_textvar = tk.StringVar()
    search_field = ttk.Entry(
        self.rootframe, textvariable=self.search_textvar, name="search"
    )
    search_btn = ttk.Button(self.rootframe, text="Search")
    sel_btn = ttk.Button(
        master=self.rootframe, text="Insert Selected Data", style="accent.TButton"
    )


class pos_page:
    def __init__(self, master, root_window):
        self.rootframe = ttk.Frame(master, style="border.TFrame")
        self.note = ttk.Notebook(self.rootframe)

        self.c = ttk.Frame(
            self.note,
        )

        l1 = ttk.Label(self.c, text="Customer Name", style="small.TLabel")
        l1.grid(row=0, column=0, padx=6, pady=2, sticky="sw")

        self.name_entry = ttk.Entry(self.c)
        self.name_entry.grid(row=1, column=0, padx=6, pady=2, columnspan=8, sticky="ew")

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

        self.cust_ins_btn = ttk.Button(
            self.c, text="Select Existing Customer", style="accent.TButton"
        )

        self.cust_ins_btn.grid(
            row=6, column=0, columnspan=8, padx=6, pady=6, sticky="sew"
        )

        self.cust_table = treeview_toplevel()
        self.cust_table.tv.config(columns=("1", "2", "3", "4"), show="headings")
        self.cust_table.tv.column("1", width=100, anchor="c", stretch=tk.YES)
        self.cust_table.tv.column("2", anchor="c", stretch=tk.YES)
        self.cust_table.tv.column("3", anchor="c", stretch=tk.YES)
        self.cust_table.tv.column("4", anchor="c", stretch=tk.YES)

        # Assigning the heading names to the
        # respective columns
        self.cust_table.tv.heading("1", text="Name")
        self.cust_table.tv.heading("2", text="Sex")
        self.cust_table.tv.heading("3", text="Age")
        self.cust_table.tv.heading("4", text="Address")

        self.cust_ins_btn.config(command=self.cust_table.run)
        grid_config(self.c)

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

        self.p = ttk.Frame(master, style="Table.TFrame")

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
        data["name"] = self.name_entry.get("1.0", "END")
        data["age"] = self.name_entry.get("1.0", "END")
        data["sex"] = self.name_entry.get("1.0", "END")
        data["addr"] = self.name_entry.get("1.0", "END")
        return data

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
        data["name"] = self.name_entry.get("1.0", "END")
        data["age"] = self.name_entry.get("1.0", "END")
        data["sex"] = self.name_entry.get("1.0", "END")
        data["addr"] = self.name_entry.get("1.0", "END")
        return data

    def as_tab(self):
        return self.rootframe


if __name__ == "__main__":
    root = tk.Tk()

    s = style(root)

    note = ttk.Notebook(root, style="ribbon.TNotebook")

    p = pos_page(note, root)
    note.add(p.as_tab(), text="Point-Of-Sale")
    note.pack(fill="both", expand=1)

    root.mainloop()
