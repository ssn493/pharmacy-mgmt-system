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
from ui_utils import *


class user_login_page:
    def __init__(self, root):
        self.rootframe = ttk.Frame(root)
        self.rootframe.pack(fill="both", expand=1)
        grid_config(self.rootframe, cols=9)
        self.rootframe.grid_columnconfigure(4, weight=0)
        self.rootframe.grid_rowconfigure(0, weight=1)

        self.register_user_page = ttk.Frame(self.rootframe)
        self.register_user_page.grid(
            row=0, column=0, columnspan=4, sticky="nswe", ipadx=10, ipady=4
        )
        grid_config(self.register_user_page)

        self.login_user_page = ttk.Frame(self.rootframe)
        self.login_user_page.grid(
            row=0, column=5, columnspan=4, sticky="nswe", ipadx=10, ipady=4
        )
        grid_config(self.login_user_page)

        self.new_cust_reg_lbl = ttk.Label(
            self.register_user_page, text="Register New Customer", style="big.TLabel"
        )
        self.new_cust_reg_lbl.grid(
            row=0, column=0, columnspan=8, padx=10, pady=4, sticky="nswe"
        )

        l1 = ttk.Label(
            self.register_user_page, text="Customer Name", style="small.TLabel"
        )
        l1.grid(row=1, column=0, padx=10, pady=4, sticky="sw")

        self.new_cust_name_entry = ttk.Entry(self.register_user_page)
        self.new_cust_name_entry.grid(
            row=2, column=0, padx=10, pady=4, columnspan=8, sticky="nswe"
        )

        l2 = ttk.Label(self.register_user_page, text="Password", style="small.TLabel")
        l2.grid(row=3, column=0, padx=10, pady=4, sticky="sw")

        self.new_cust_pswd_entry = ttk.Entry(self.register_user_page, show="*")
        self.new_cust_pswd_entry.grid(
            row=4, column=0, padx=10, pady=4, columnspan=6, sticky="nswe"
        )
        self.new_cust_shown_pswd = False
        self.new_cust_show_pswd_btn = ttk.Button(
            self.register_user_page,
            text="Show Password",
            command=lambda: self.show_pswd(
                self.new_cust_pswd_entry, self.new_cust_shown_pswd
            ),
        )
        self.new_cust_show_pswd_btn.grid(
            row=4, column=6, columnspan=2, padx=10, pady=4, sticky="swe"
        )

        l3 = ttk.Label(self.register_user_page, text="Age", style="small.TLabel")
        l3.grid(row=5, column=0, padx=10, pady=4, sticky="sw")

        self.new_cust_age_entry = ttk.Entry(self.register_user_page)
        self.new_cust_age_entry.grid(
            row=6, column=0, padx=10, pady=4, columnspan=3, sticky="nswe"
        )

        l4 = ttk.Label(self.register_user_page, text="Sex", style="small.TLabel")
        l4.grid(row=5, column=4, padx=10, pady=4, sticky="sw")

        self.new_cust_sex_entry = ttk.Entry(self.register_user_page)
        self.new_cust_sex_entry.grid(
            row=6, column=4, padx=10, pady=4, columnspan=4, sticky="nswe"
        )

        l5 = ttk.Label(self.register_user_page, text="Address", style="small.TLabel")
        l5.grid(row=7, column=0, padx=10, pady=4, sticky="sw")

        self.new_cust_addr_entry = ttk.Entry(self.register_user_page)
        self.new_cust_addr_entry.grid(
            row=8, column=0, padx=10, pady=4, columnspan=8, sticky="nswe"
        )

        self.new_cust_reg_btn = ttk.Button(
            self.register_user_page,
            text="Register New Customer",
            style="accent.TButton",
        )
        self.new_cust_reg_btn.grid(
            row=9, column=0, columnspan=8, padx=10, pady=6, sticky="swe"
        )

        border = ttk.Frame(self.rootframe, style="hr.TFrame")
        border.grid(row=0, column=4, padx=4, pady=40, sticky="ns")

        # Existing User Login
        lx1 = ttk.Label(
            self.login_user_page, text="Customer Name", style="small.TLabel"
        )
        lx1.grid(row=1, column=0, padx=10, pady=4, sticky="sw")

        self.ex_cust_name_entry = ttk.Entry(self.login_user_page)
        self.ex_cust_name_entry.grid(
            row=2, column=0, padx=10, pady=4, columnspan=8, sticky="ew"
        )

        lx2 = ttk.Label(self.login_user_page, text="Password", style="small.TLabel")
        lx2.grid(row=3, column=0, padx=10, pady=4, sticky="sw")

        self.ex_cust_pswd_entry = ttk.Entry(self.login_user_page, show="*")
        self.ex_cust_pswd_entry.grid(
            row=4, column=0, padx=10, pady=4, columnspan=6, sticky="ew"
        )
        self.ex_cust_shown_pswd = False
        self.ex_cust_show_pswd_btn = ttk.Button(
            self.login_user_page,
            text="Show Password",
            command=lambda: self.show_pswd(
                self.ex_cust_pswd_entry, self.ex_cust_shown_pswd
            ),
        )
        self.ex_cust_show_pswd_btn.grid(
            row=4, column=6, columnspan=2, padx=10, pady=4, sticky="sew"
        )

    def show_pswd(self, widget, flag):
        if not flag:
            widget["show"] = ""
            flag = True
        else:
            widget["show"] = "*"
            flag = False

    def as_frame(self):
        return self.rootframe


class emp_login_page:
    def __init__(self, root):
        self.rootframe = ttk.Frame(root)
        self.rootframe.pack(fill="both", expand=1)
        grid_config(self.rootframe)
        # Existing User Login
        lx1 = ttk.Label(self.rootframe, text="Employee Name", style="small.TLabel")
        lx1.grid(row=1, column=0, padx=10, pady=4, sticky="sw")

        self.emp_name_entry = ttk.Entry(self.rootframe)
        self.emp_name_entry.grid(
            row=2, column=0, padx=10, pady=4, columnspan=8, sticky="ew"
        )

        lx2 = ttk.Label(self.rootframe, text="Password", style="small.TLabel")
        lx2.grid(row=3, column=0, padx=10, pady=4, sticky="sw")

        self.emp_pswd_entry = ttk.Entry(self.rootframe, show="*")
        self.emp_pswd_entry.grid(
            row=4, column=0, padx=10, pady=4, columnspan=6, sticky="ew"
        )
        self.emp_shown_pswd = False
        self.emp_show_pswd_btn = ttk.Button(
            self.login_user_page,
            text="Show Password",
            command=lambda: self.show_pswd(self.emp_pswd_entry, self.emp_shown_pswd),
        )
        self.emp_show_pswd_btn.grid(
            row=4, column=6, columnspan=2, padx=10, pady=4, sticky="sew"
        )

    def show_pswd(self, widget, flag):
        if not flag:
            widget["show"] = ""
            flag = True
        else:
            widget["show"] = "*"
            flag = False

    def as_frame(self):
        return self.rootframe


class past_orders_page:
    def __init__(self, master):
        self.rootframe = ttk.Frame(master)
        self.rootframe.pack(fill="both", expand=1)
        grid_config(self.rootframe)
        self.rootframe.grid_rowconfigure(0, weight=1)

        self.past_orders = ttk.Frame(self.rootframe)
        self.past_orders.grid(row=0, column=1, columnspan=6)

    def as_tab(self):
        return self.rootframe

class pos_page:
    def __init__(self, master, root_window):
        self.rootframe = ttk.Frame(master)
        self.rootframe.pack(fill="both", expand=1)

        self.menu = HorizontalNavMenu(self.rootframe)
        self.customer_details_page = ttk.Frame(self.menu.content_frame)

        self.cust_reg_lbl = ttk.Label(
            self.customer_details_page, text="Customer Details", style="big.TLabel"
        )
        self.cust_reg_lbl.grid(
            row=0, column=0, columnspan=8, padx=10, pady=6, sticky="nswe"
        )

        l2 = ttk.Label(self.user_page, text="Phone Number", style="small.TLabel")
        l2.grid(row=1, column=0, padx=10, pady=4, sticky="sw")

        self.cust_phone_number_entry = ttk.Entry(self.customer_details_page, show="*")
        self.cust_phone_number_entry.grid(
            row=2, column=0, padx=10, pady=4, columnspan=6, sticky="nswe"
        )
        self.cust_search_btn = ttk.Button(
            self.register_user_page,
            text="Search",
        )
        self.cust_search_btn.grid(
            row=4, column=6, columnspan=2, padx=10, pady=4, sticky="swe"
        )
        l1 = ttk.Label(
            self.customer_details_page, text="Customer Name", style="small.TLabel"
        )
        l1.grid(row=1, column=0, padx=10, pady=4, sticky="sw")

        self.cust_name_entry = ttk.Entry(self.customer_details_page)
        self.cust_name_entry.grid(
            row=2, column=0, padx=10, pady=4, columnspan=8, sticky="nswe"
        )


        l3 = ttk.Label(self.register_user_page, text="Age", style="small.TLabel")
        l3.grid(row=5, column=0, padx=10, pady=4, sticky="sw")

        self.cust_age_entry = ttk.Entry(self.register_user_page)
        self.cust_age_entry.grid(
            row=6, column=0, padx=10, pady=4, columnspan=3, sticky="nswe"
        )

        l4 = ttk.Label(self.register_user_page, text="Sex", style="small.TLabel")
        l4.grid(row=5, column=4, padx=10, pady=4, sticky="sw")

        self.cust_sex_entry = ttk.Entry(self.register_user_page)
        self.cust_sex_entry.grid(
            row=6, column=4, padx=10, pady=4, columnspan=4, sticky="nswe"
        )

        l5 = ttk.Label(self.register_user_page, text="Address", style="small.TLabel")
        l5.grid(row=7, column=0, padx=10, pady=4, sticky="sw")

        self.cust_addr_entry = ttk.Entry(self.register_user_page)
        self.cust_addr_entry.grid(
            row=8, column=0, padx=10, pady=4, columnspan=8, sticky="nswe"
        )

        self.new_cust_reg_btn = ttk.Button(
            self.register_user_page,
            text="Register New Customer",
            style="accent.TButton",
        )
        self.new_cust_reg_btn.grid(
            row=9, column=0, columnspan=4, padx=10, pady=6, sticky="swe"
        )

        border = ttk.Frame(self.rootframe, style="hr.TFrame")
        border.grid(row=10, column=4, padx=4, pady=40, sticky="ew")

        self.rootframe = ttk.Frame(master, style="border.TFrame")
        self.note = ttk.Notebook(self.rootframe)

        #########################
        # Medicine Details Page #
        #########################
        self.m = ttk.Frame(master, style="Table.TFrame")
        grid_config(self.m)

        self.sel_existing_cust_btn = ttk.Button(
            self.m, text="Search For Medicines", style="accent.TButton"
        )
        self.sel_existing_cust_btn.grid(
            row=9, column=0, columnspan=8, padx=10, pady=6, sticky="sew"
        )
        self.sel_existing_cust_btn.config(command=self.sel_existing_customer)

        l1 = ttk.Label(self.m, text="Medicine Name", style="small.TLabel")
        l1.grid(row=0, column=0, padx=10, pady=4, sticky="sw")

        self.med_name_entry = ttk.Entry(self.m)
        self.med_name_entry.grid(
            row=1, column=0, padx=10, pady=4, columnspan=7, sticky="ew"
        )

        self.med_search_btn = ttk.Button(
            self.m,
            text="Search",
        )
        self.med_search_btn.grid(row=1, column=7, padx=10, pady=4, sticky="ne")

        l2 = ttk.Label(self.m, text="Quantity", style="small.TLabel")
        l2.grid(row=2, column=0, padx=10, pady=4, sticky="sw")

        self.qty_entry = ttk.Entry(self.m)
        self.qty_entry.grid(
            row=3, column=0, padx=10, pady=4, columnspan=8, sticky="sew"
        )

        self.add_sel_btn = ttk.Button(
            self.m, text="Add Selected", style="accent.TButton"
        )
        self.add_sel_btn.grid(
            row=7, column=0, padx=10, pady=8, columnspan=8, sticky="ew"
        )


        #########################
        # Payment Details Page #
        #########################
        self.payment_details_page = ttk.Frame(master)
        grid_config(self.payment_details_page)

        l1 = ttk.Label(self.payment_details_page, text="Payment Date", style="small.TLabel")
        l1.grid(row=0, column=0, padx=10, pady=4, sticky="sw")

        self.datetime_entry = ttk.Entry(self.payment_details_page)
        self.datetime_entry.grid(
            row=1, column=0, padx=10, pady=4, columnspan=5, sticky="ew"
        )

        self.ct_btn = ttk.Button(
            self.payment_details_page,
            text="Insert Current Date",
            command=lambda: self.datetime_entry.insert(
                "0", str(datetime.datetime.now().date())
            ),
        )
        self.ct_btn.grid(row=1, column=6, columnspan=3, padx=10, pady=4, sticky="new")

        self.gen_recpt = ttk.Button(
            self.payment_details_page, text="Generate Receipt", style="accent.TButton"
        )
        self.gen_recpt.grid(row=3, column=0, padx=10, pady=8, columnspan=8, sticky="ew")

        var = tk.StringVar()
        self.payment_method_menu = ttk.OptionMenu(
            self.payment_details_page, var, *["Cash", "Credit/Debit Card", "UPI"]
        )
        # self.payment_method_menu.config()
        self.payment_method_menu.grid(
            row=2, column=0, padx=10, pady=8, columnspan=8, sticky="ew"
        )


        # self.note.add(self.c, text="Customer Details")
        self.menu.add(self.m, text="Medicines")
        self.menu.add(self.payment_details_page, text="Payment")
        self.menu.pack(fill="both", expand=1, padx=10)

        self.n_btn = ttk.Button(
            master=self.rootframe,
            text="Next >",
            command=self.menu.next_page,
        )
        self.n_btn.pack(side="right", anchor="se", padx=24, pady=10)

        self.b_btn = ttk.Button(
            master=self.rootframe,
            text="< Back",
            command=self.menu.prev_page,
        )
        self.b_btn.pack(side="left", anchor="sw", padx=24, pady=10)

        
    def sel_existing_customer(self):
        main = tk.Toplevel()
        main.title("Select Existing Customer")
        rootframe = ttk.Frame(main)
        rootframe.pack(fill="both", expand=1)
        grid_config(rootframe)

        self.cust_table = easy_treeview(rootframe, get_field_names(customers))
        ins_rows_treeview(self.cust_table, get_table(customers))
        self.cust_table.grid(
            row=0, column=0, rowspan=3, columnspan=8, padx=10, pady=6, sticky="nswe"
        )
        self.cust_table.bind("<<TreeviewSelect>>", self.display_cust_data())

        l1 = ttk.Label(rootframe, text="Search by name", style="small.TLabel")
        l1.grid(row=3, column=0, padx=10, pady=4, sticky="sw")

        search_textvar = tk.StringVar()
        search_field = ttk.Entry(rootframe, textvariable=search_textvar)
        search_field.grid(row=4, column=0, columnspan=8, padx=10, pady=4, sticky="swe")

        sel_button = ttk.Button(
            master=rootframe,
            text="Done!",
            style="accent.TButton",
            command=main.destroy,
        )
        sel_button.grid(row=5, column=0, columnspan=8, padx=10, pady=6, sticky="swe")

        s = lambda event: update_treeview(
            self.cust_table,
            search_cust_by_name(search_textvar.get())
        )
        search_field.bind('Key-Release', s)

        self.cust_reg_lbl.config(text="Verify Customer Details")
        hide_grid_widget(self.new_cust_reg_btn)

    def display_cust_data(self):
        data = self.cust_table.selection()[0]['values']
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

class about_page:
    def __init__(self, master, root_window):
        self.root_window = root_window
        self.rootframe = ttk.Frame(master)
        grid_config(self.rootframe, cols=7)
        l0 = ttk.Label(self.rootframe, text="About", style="big.TLabel")
        l0.grid(row=0, column=3, padx=15, pady=15, sticky="n")
        l1 = ttk.Label(
            self.rootframe,
            text="Made by Subhrojyoti Sen (@ssn493)",
        )
        l1.grid(row=1, column=3, padx=20, pady=5, sticky="ns")
        l2 = ttk.Label(
            self.rootframe, text="Moonlighting is illegal.", style="small.TLabel"
        )
        l2.grid(row=2, column=3, padx=20, pady=5, sticky="ns")
        quit_btn = ttk.Button(self.rootframe, text="Quit", command=self.quit_app)
        quit_btn.grid(row=4, column=3, padx=20, pady=5, sticky="swe")

    def quit_app(self):
        close()
        self.root_window.destroy()
        exit()

    def as_tab(self):
        return self.rootframe

class main(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
empty_page = ttk.Frame()
if __name__ == "__main__":
    pass
