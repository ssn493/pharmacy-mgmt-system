from tkinter import ttk
import tkinter as tk
import datetime
from pharmacy_backend import *
from theme import style
from ui_utils import *


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


class recent_orders_page:
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

        # customer details
        self.customer_details_page = ttk.Frame(self.menu.content_frame)
        grid_config(self.customer_details_page)

        self.cust_reg_lbl = ttk.Label(
            self.customer_details_page, text="Customer Details", style="big.TLabel"
        )
        self.cust_reg_lbl.grid(
            row=0, column=0, columnspan=8, padx=10, pady=6, sticky="nswe"
        )

        l2 = ttk.Label(
            self.customer_details_page, text="Phone Number", style="small.TLabel"
        )
        l2.grid(row=1, column=0, padx=10, pady=4, sticky="sw")

        self.cust_phone_number_entry = ttk.Entry(self.customer_details_page)
        self.cust_phone_number_entry.grid(
            row=2, column=0, padx=10, pady=4, columnspan=6, sticky="nswe"
        )
        self.cust_search_btn = ttk.Button(
            self.customer_details_page, text="Search", command=self.search_by_ph_no
        )
        self.cust_search_btn.grid(
            row=2, column=6, columnspan=2, padx=10, pady=4, sticky="swe"
        )
        l1 = ttk.Label(
            self.customer_details_page, text="Customer Name", style="small.TLabel"
        )
        l1.grid(row=3, column=0, padx=10, pady=4, sticky="sw")

        self.cust_name_entry = ttk.Entry(self.customer_details_page)
        self.cust_name_entry.grid(
            row=4, column=0, padx=10, pady=4, columnspan=8, sticky="nswe"
        )

        l3 = ttk.Label(self.customer_details_page, text="Age", style="small.TLabel")
        l3.grid(row=5, column=0, padx=10, pady=4, sticky="sw")

        self.cust_age_entry = ttk.Entry(self.customer_details_page)
        self.cust_age_entry.grid(
            row=6, column=0, padx=10, pady=4, columnspan=3, sticky="nswe"
        )

        l4 = ttk.Label(self.customer_details_page, text="Sex", style="small.TLabel")
        l4.grid(row=5, column=4, padx=10, pady=4, sticky="sw")

        self.cust_sex_entry = ttk.Entry(self.customer_details_page)
        self.cust_sex_entry.grid(
            row=6, column=4, padx=10, pady=4, columnspan=4, sticky="nswe"
        )

        l5 = ttk.Label(self.customer_details_page, text="Address", style="small.TLabel")
        l5.grid(row=7, column=0, padx=10, pady=4, sticky="sw")

        self.cust_addr_entry = ttk.Entry(self.customer_details_page)
        self.cust_addr_entry.grid(
            row=8, column=0, padx=10, pady=4, columnspan=8, sticky="nswe"
        )

        self.new_cust_reg_btn = ttk.Button(
            self.customer_details_page,
            text="Register New Customer",
            style="accent.TButton",
            state="disabled",
        )
        self.new_cust_reg_btn.grid(
            row=9, column=0, columnspan=8, padx=10, pady=6, sticky="swe"
        )

        self.new_cust_warn_label = ttk.Label(
            self.customer_details_page,
            text="Customer not found! Register new customer",
            style="accent.TLabel",
        )
        self.new_cust_warn_label.grid(
            row=10,
            column=3,
            columnspan=2,
            ipadx=6,
            ipady=6,
            padx=10,
            pady=6,
            sticky="swe",
        )
        hide_grid_widget(self.new_cust_warn_label)

        #########################
        # Medicine Details Page #
        #########################
        self.medicine_details_page = ttk.Frame(self.menu.content_frame)
        grid_config(self.medicine_details_page)

        l1 = ttk.Label(
            self.medicine_details_page, text="Medicine Name", style="small.TLabel"
        )
        l1.grid(row=0, column=0, padx=10, pady=4, sticky="sw")

        self.med_name_entry = ttk.Entry(self.medicine_details_page)
        self.med_name_entry.grid(
            row=1, column=0, padx=10, pady=4, columnspan=7, sticky="we"
        )

        self.med_dropdown = EntrySuggestions(self.med_name_entry)
        self.med_name_entry.bind("<KeyRelease>", self.med_suggestions)

        self.med_insert_btn = ttk.Button(
            self.medicine_details_page,
            text="Insert",
        )
        self.med_insert_btn.grid(row=1, column=7, padx=10, pady=4, sticky="ne")

        self.med_table = medTable(self.medicine_details_page)
        self.med_table.ins_row("Med 1")
        self.med_table.grid(row=2, column=0, padx=10, pady=4, columnspan=8, sticky="we")

        p = lambda: print(self.med_table.get_data())
        self.cnf_med_quantity = ttk.Button(
            self.medicine_details_page,
            text="Confirm Medication Quantity",
            style="accent.TButton",
            command=p,
        )
        self.cnf_med_quantity.grid(
            row=9, column=0, columnspan=8, padx=10, pady=6, sticky="swe"
        )

        #########################
        # Payment Details Page #
        #########################
        self.payment_details_page = ttk.Frame(self.menu.content_frame)
        grid_config(self.payment_details_page)

        l1 = ttk.Label(
            self.payment_details_page, text="Payment Date", style="small.TLabel"
        )
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

        self.menu.add(self.customer_details_page, text="Customer Details")
        self.menu.add(self.medicine_details_page, text="Medicines")
        self.menu.add(self.payment_details_page, text="Payment")
        self.menu.pack(fill="both", expand=1, padx=10)

        # Pagination
        self.n_btn = ttk.Button(
            master=self.rootframe,
            text="Next >",
            command=self.menu.next_page,
            style="borderless.TButton",
        )
        self.n_btn.pack(side="right", anchor="se", padx=24, pady=10)

        self.b_btn = ttk.Button(
            master=self.rootframe,
            text="< Back",
            command=self.menu.prev_page,
            style="borderless.TButton",
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
        self.cust_table.bind("<<TreeviewSelect>>", self.display_cust_data)

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
            self.cust_table, search_cust_by_name(search_textvar.get())
        )
        search_field.bind("Key-Release", s)

        self.cust_reg_lbl.config(text="Verify Customer Details")
        hide_grid_widget(self.new_cust_reg_btn)

    def display_cust_data(self, data):
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

    def med_suggestions(self, event):
        self.med_dropdown.data.clear()
        self.med_dropdown.data.extend(search_med_by_name(self.med_name_entry.get()))

        self.med_dropdown.update()

    def search_by_ph_no(self):
        ph_no = int(self.cust_phone_number_entry.get())
        data = search_cust_by_phone_no(ph_no)
        if data == []:
            show_grid_widget(self.new_cust_warn_label)
            self.new_cust_reg_btn["state"] = "normal"
        else:
            self.display_cust_data(data)

    def as_tab(self):
        return self.rootframe


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

        l2 = ttk.Label(self.rootframe, text="-_-", style="small.TLabel")
        l2.grid(row=2, column=3, padx=20, pady=5, sticky="ns")

        quit_btn = ttk.Button(
            self.rootframe,
            text="Quit",
            command=self.quit_app,
        )
        quit_btn.grid(row=4, column=3, padx=20, pady=5, sticky="swe")

    def quit_app(self):
        close()
        self.root_window.destroy()
        exit()

    def as_tab(self):
        return self.rootframe


################################
#                              #
#  Inventory management pages  #
#                              #
################################


class inventory_order_page:
    def __init__(self, master, root_window):
        self.rootframe = ttk.Frame(master)
        self.note = ttk.Notebook(self.rootframe)

        self.filters = ttk.Frame(self.note)
        self.view = ttk.Frame(self.note)

        grid_config(self.filters)
        grid_config(self.view)

        self.invt_table = easy_treeview(
            self.view,
            columns=[
                "Order ID",
                "Order Name",
                "Order Date",
                "Item ID",
                "Quantity",
                "Amount",
                "Status",
            ],
        )
        self.invt_table.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            rowspan=6,
            columnspan=8,
            ipadx=6,
            ipady=4,
            sticky="nswe",
        )

        self.order_complete_btn = ttk.Button(
            self.view,
            text="Order completed",
            style="accent.TButton",
            command=self.orderRecievedBox,
            state=tk.DISABLED,
        )
        self.order_complete_btn.grid(row=7, column=0, padx=10, pady=6, sticky="sew")

        self.reset_btn = ttk.Button(
            self.view, text="Reset", style="accent.TButton", command=self.show_table
        )
        self.reset_btn.grid(row=7, column=7, padx=10, pady=6, sticky="sew")

        l1 = ttk.Label(self.filters, text="Item Id", style="small.TLabel")
        l1.grid(row=0, column=0, padx=10, pady=2, sticky="sw")

        setattr(self, "item_id", ttk.Entry(self.filters))
        getattr(self, "item_id").grid(
            row=1, column=0, padx=10, pady=2, sticky="sew", columnspan=8
        )

        l2 = ttk.Label(self.filters, text="Item Name", style="small.TLabel")
        l2.grid(row=2, column=0, padx=10, pady=2, sticky="sw")

        setattr(self, "item_name", ttk.Entry(self.filters))
        getattr(self, "item_name").grid(
            row=3, column=0, padx=10, pady=2, sticky="sew", columnspan=8
        )

        l3 = ttk.Label(self.filters, text="Status", style="small.TLabel")
        l3.grid(row=4, column=0, padx=10, pady=2, sticky="sw")

        setattr(self, "status", ttk.Entry(self.filters))
        getattr(self, "status").grid(
            row=5, column=0, padx=10, pady=2, sticky="sew", columnspan=8
        )

        self.show_table()

        self.invt_table.bind("<<TreeviewSelect>>", self.selected_item)

        self.apply_btn = ttk.Button(
            self.filters,
            text="Apply Filters",
            style="accent.TButton",
            command=self.select_from_filters,
        )
        self.apply_btn.grid(
            row=6, column=0, padx=10, pady=10, columnspan=8, sticky="ew"
        )

        self.note.add(self.view, text="Table View")
        self.note.add(self.filters, text="Filters")
        self.note.pack(fill="both", expand=1, padx=10)
        self.note.enable_traversal()

        self.rootframe.pack(fill="both", expand=1)

    def toggle_filters(self):
        if not self.show_filters:
            self.filters.pack(**self.filter_packinfo)
            self.show_filters = True
        else:
            self.filters.pack_forget()
            self.show_filters = False

    def selected_item(self, a):
        selectedItem = self.invt_table.selection()[0]
        status = self.invt_table.item(selectedItem)["values"][6]
        if status == "Pending":
            self.order_complete_btn.config(state=tk.NORMAL)
        else:
            self.order_complete_btn.config(state=tk.DISABLED)

    def show_table(self):
        self.order_complete_btn.config(state=tk.DISABLED)
        getattr(self, "item_id").delete(0, tk.END)
        getattr(self, "item_name").delete(0, tk.END)
        getattr(self, "status").delete(0, tk.END)
        for item in self.invt_table.get_children():
            self.invt_table.delete(item)
        for row in get_table("inventory_order"):
            self.invt_table.insert("", tk.END, values=row)

    def as_tab(self):
        return self.rootframe

    def close_win(self, top):
        top.destroy()

    def orderReceived(self, top):
        selectedItem = self.invt_table.selection()[0]
        order_id = self.invt_table.item(selectedItem)["values"][0]
        item_id = self.invt_table.item(selectedItem)["values"][3]
        change_order_status(int(order_id), int(item_id))
        top.destroy()
        self.select_from_filters()
        o.show_table()
        i.show_table()

        def orderRecievedBox(self):
            top = tk.Toplevel(root)
            top.geometry("300x150")
            rootframe = ttk.Frame(top)
            rootframe.pack(fill="both")
            grid_config(rootframe)

            selectedItem = self.invt_table.selection()[0]
            order_id = self.invt_table.item(selectedItem)["values"][0]
            item_name = self.invt_table.item(selectedItem)["values"][1]
            item_id = self.invt_table.item(selectedItem)["values"][3]

            l1 = ttk.Label(
                rootframe,
                text=f"Confirm Order {order_id}: {item_id}-{item_name} Received",
                style="small.TLabel",
            )
            l1.grid(row=0, column=0, padx=10, pady=2, sticky="sw", columnspan=6)

            confirm_row_btn = ttk.Button(
                rootframe,
                text="Yes",
                style="accent.TButton",
                command=lambda: self.orderReceived(top),
            )
            confirm_row_btn.grid(
                row=7, column=0, padx=10, pady=6, sticky="sew", columnspan=2
            )

            cancel_button = ttk.Button(
                rootframe,
                text="No",
                style="accent.TButton",
                command=lambda: self.close_win(top),
            )
            cancel_button.grid(
                row=7, column=2, padx=10, pady=6, sticky="sew", columnspan=2
            )

        def all_filter(self, row):
            d = {"item_id": 3, "item_name": 1, "status": 6}
            filter_list = ["item_id", "item_name", "status"]
            val = all(
                str(row[d[f]]) == getattr(self, f).get() or getattr(self, f).get() == ""
                for f in filter_list
            )
            return val

        def select_from_filters(self):
            self.invt_table.delete(*self.invt_table.get_children())
            for row in get_table("inventory_order"):
                if self.all_filter(row):
                    self.invt_table.insert("", "end", values=list(row))
            prev_tab(self.note)


class item_page:
    def __init__(self, master, root_window):
        self.rootframe = ttk.Frame(master)
        self.note = ttk.Notebook(self.rootframe)

        self.filters = ttk.Frame(self.note)
        self.view = ttk.Frame(self.note)

        grid_config(self.filters)
        grid_config(self.view)

        self.search_entry = ttk.Entry(self.view)
        self.search_entry.grid(
            row=0, column=1, padx=10, pady=2, columnspan=7, sticky="we"
        )

        self.search_btn = ttk.Button(self.view, text="Search by Item Name")
        self.search_btn.grid(row=0, column=0, padx=10, pady=2, sticky="swe")

        self.search_entry.bind("<KeyRelease>", self.searchItem)

        self.item_table = easy_treeview(
            self.view,
            columns=[
                "Item Id",
                "Item Name",
                "Stock Quantity",
                "Amount",
                "Total Amount",
                "Description",
            ],
        )
        self.item_table.grid(
            row=2,
            column=0,
            padx=10,
            pady=10,
            rowspan=6,
            columnspan=8,
            ipadx=6,
            ipady=4,
            sticky="nswe",
        )

        self.edit_row_btn = ttk.Button(
            self.view, text="Edit row", style="accent.TButton"
        )
        self.edit_row_btn.grid(row=7, column=0, padx=10, pady=6, sticky="sew")

        self.place_order = ttk.Button(
            self.view, text="Place Order", command=self.placeOrderBox, state=tk.DISABLED
        )
        self.place_order.grid(row=7, column=5, padx=10, pady=6, sticky="w")

        self.add_item = ttk.Button(
            self.view, text="+ Add item", command=self.addItemBox
        )
        self.add_item.grid(row=7, column=6, padx=10, pady=6, sticky="w")

        self.delete_row_btn = ttk.Button(
            self.view,
            text="- Delete item",
            command=self.deleteItemBox,
            state=tk.DISABLED,
        )
        self.delete_row_btn.grid(row=7, column=7, padx=10, pady=6, sticky="w")

        l1 = ttk.Label(self.filters, text="Item Id", style="small.TLabel")
        l1.grid(row=0, column=0, padx=10, pady=2, sticky="sw")

        setattr(self, "item_id", ttk.Entry(self.filters))
        getattr(self, "item_id").grid(
            row=1, column=0, padx=10, pady=2, sticky="sw", columnspan=8
        )

        l2 = ttk.Label(self.filters, text="Item Name", style="small.TLabel")
        l2.grid(row=2, column=0, padx=10, pady=2, sticky="sw")

        setattr(self, "item_name", ttk.Entry(self.filters))
        getattr(self, "item_name").grid(
            row=3, column=0, padx=10, pady=2, sticky="sw", columnspan=8
        )

        l3 = ttk.Label(self.filters, text="Sex", style="small.TLabel")
        l3.grid(row=4, column=4, padx=10, pady=2, sticky="sw")

        setattr(self, "date", ttk.Entry(self.filters))
        getattr(self, "date").grid(
            row=3, column=0, padx=10, pady=2, sticky="sw", columnspan=8
        )

        l4 = ttk.Label(self.filters, text="Address", style="small.TLabel")
        l4.grid(row=4, column=0, padx=10, pady=2, sticky="sw")

        self.show_table()

        self.addr_entry = ttk.Entry(self.filters)
        self.addr_entry.grid(
            row=5, column=0, padx=10, pady=2, columnspan=8, sticky="ew"
        )

        self.apply_btn = ttk.Button(
            self.filters, text="Apply Filters", style="accent.TButton"
        )
        self.apply_btn.grid(
            row=6, column=0, padx=10, pady=10, columnspan=8, sticky="ew"
        )

        self.item_table.bind("<<TreeviewSelect>>", self.selected_item)

        self.note.add(self.view, text="Table View")
        self.note.add(self.filters, text="Filters")
        self.note.pack(fill="both", expand=1, padx=10)
        self.note.enable_traversal()

        self.rootframe.pack(fill="both", expand=1)

    def selected_item(self, a):
        self.place_order.config(state=tk.NORMAL)
        self.delete_row_btn.config(state=tk.NORMAL)

    def show_table(self):
        self.place_order.config(state=tk.DISABLED)
        self.delete_row_btn.config(state=tk.DISABLED)
        for item in self.item_table.get_children():
            self.item_table.delete(item)
        for row in get_table("items"):
            self.item_table.insert("", tk.END, values=row)

    def searchItem(self, a):
        search_val = self.search_entry.get()
        for item in self.item_table.get_children():
            self.item_table.delete(item)
        for row in search_item(search_val):
            self.item_table.insert("", tk.END, values=row)

    def as_tab(self):
        return self.rootframe

    def close_win(self, top):
        top.destroy()

    def get_order_data(self, e1, e2, e3, top):
        item_num = int(e1.get())
        item_name = e2.get()
        qty = int(e3.get())
        place_order(item_num, item_name, qty)
        self.close_win(top)
        o.show_table()

    def add_item_data(self, e1, e2, e3, e4, e5, top):
        item_num = int(e1.get())
        item_name = e2.get()
        qty = int(e3.get())
        amt = int(e4.get())
        item_desc = e5.get()
        addItemtoDB(item_num, item_name, qty, amt, item_desc)
        self.close_win(top)
        i.show_table()

    def addItemBox(self):
        top = tk.Toplevel(root)
        top.geometry("750x350")
        rootframe = ttk.Frame(top)
        rootframe.pack(fill="both", expand=1)
        grid_config(rootframe)

        l1 = ttk.Label(rootframe, text="Item Id", style="small.TLabel")
        l1.grid(row=0, column=0, padx=10, pady=2, sticky="sw")

        e1 = ttk.Entry(rootframe)
        e1.grid(row=1, column=0, padx=10, pady=2, sticky="sew", columnspan=8)

        l2 = ttk.Label(rootframe, text=f"Item Name", style="small.TLabel")
        l2.grid(row=2, column=0, padx=10, pady=2, sticky="sw")

        e2 = ttk.Entry(rootframe)
        e2.grid(row=3, column=0, padx=10, pady=2, sticky="sew", columnspan=8)

        l3 = ttk.Label(rootframe, text="Quantity", style="small.TLabel")
        l3.grid(row=4, column=0, padx=10, pady=2, sticky="sw")

        e3 = ttk.Entry(rootframe)
        e3.grid(row=5, column=0, padx=10, pady=2, sticky="sew", columnspan=8)

        l4 = ttk.Label(rootframe, text="Amount", style="small.TLabel")
        l4.grid(row=6, column=0, padx=10, pady=2, sticky="sw")

        e4 = ttk.Entry(rootframe)
        e4.grid(row=7, column=0, padx=10, pady=2, sticky="sew", columnspan=8)

        l5 = ttk.Label(rootframe, text="Item Description", style="small.TLabel")
        l5.grid(row=8, column=0, padx=10, pady=2, sticky="sw")

        e5 = ttk.Entry(rootframe)
        e5.grid(row=9, column=0, padx=10, pady=2, sticky="sew", columnspan=8)

        confirm_row_btn = ttk.Button(
            rootframe,
            text="Confirm",
            style="accent.TButton",
            command=lambda: self.add_item_data(e1, e2, e3, e4, e5, top),
        )
        confirm_row_btn.grid(row=10, column=0, padx=10, pady=6, sticky="sew")

        cancel_button = ttk.Button(
            rootframe,
            text="Cancel",
            style="accent.TButton",
            command=lambda: self.close_win(top),
        )
        cancel_button.grid(row=11, column=5, padx=10, pady=6, sticky="sew")

    def delete_item_data(self, item_id, top):
        deleteItemfromDB(item_id)
        self.close_win(top)
        i.show_table()
        o.show_table()

    def deleteItemBox(self):
        top = tk.Toplevel(root)
        top.geometry("750x250")
        rootframe = ttk.Frame(top)
        rootframe.pack(fill="both", expand=1)
        grid_config(rootframe)

        selectedItem = self.item_table.selection()[0]
        item_id = self.item_table.item(selectedItem)["values"][0]

        l1 = ttk.Label(
            rootframe, text="Do you want to delete item?", style="small.TLabel"
        )
        l1.grid(row=0, column=0, padx=10, pady=2, sticky="sw", columnspan=6)

        confirm_row_btn = ttk.Button(
            rootframe,
            text="Yes",
            style="accent.TButton",
            command=lambda: self.delete_item_data(item_id, top),
        )
        confirm_row_btn.grid(
            row=7, column=0, padx=10, pady=6, sticky="sew", columnspan=2
        )

        cancel_button = ttk.Button(
            rootframe,
            text="No",
            style="accent.TButton",
            command=lambda: self.close_win(top),
        )
        cancel_button.grid(row=7, column=2, padx=10, pady=6, sticky="sew", columnspan=2)

    def placeOrderBox(self):
        top = tk.Toplevel(root)
        top.geometry("750x250")
        rootframe = ttk.Frame(top)
        rootframe.pack(fill="both", expand=1)
        grid_config(rootframe)

        selectedItem = self.item_table.selection()[0]
        item_id = self.item_table.item(selectedItem)["values"][0]
        item_name = self.item_table.item(selectedItem)["values"][1]

        l1 = ttk.Label(rootframe, text="Item Id", style="small.TLabel")
        l1.grid(row=0, column=0, padx=10, pady=2, sticky="sw")

        e1 = ttk.Entry(rootframe)
        e1.insert(0, item_id)
        e1.grid(row=1, column=0, padx=10, pady=2, sticky="sew", columnspan=8)

        l2 = ttk.Label(rootframe, text=f"Item Name", style="small.TLabel")
        l2.grid(row=2, column=0, padx=10, pady=2, sticky="sw")

        e2 = ttk.Entry(rootframe)
        e2.insert(0, item_name)
        e2.grid(row=3, column=0, padx=10, pady=2, sticky="sew", columnspan=8)

        l3 = ttk.Label(rootframe, text="Quantity", style="small.TLabel")
        l3.grid(row=4, column=0, padx=10, pady=2, sticky="sw")

        e3 = ttk.Entry(rootframe)
        e3.grid(row=5, column=0, padx=10, pady=2, sticky="sew", columnspan=8)

        confirm_row_btn = ttk.Button(
            rootframe,
            text="Confirm",
            style="accent.TButton",
            command=lambda: self.get_order_data(e1, e2, e3, top),
        )
        confirm_row_btn.grid(row=7, column=0, padx=10, pady=6, sticky="sew")

        cancel_button = ttk.Button(
            rootframe,
            text="Cancel",
            style="accent.TButton",
            command=lambda: self.close_win(top),
        )
        cancel_button.grid(row=7, column=5, padx=10, pady=6, sticky="sew")


def main():
    root = tk.Tk()
    # root = ttk.Frame(main)
    # root.pack(fill="both", expand=1)

    s = style(root)

    # a = login_page(root)

    note = VerticalNavMenu(root, menu_button=True)

    pos = pos_page(note.content_frame, root_window=root)
    abt = about_page(master=note.content_frame, root_window=root)

    note.add(pos.as_tab(), text="New Order")
    note.add(abt.as_tab(), text="About")
    note.add(ttk.Frame(), text="Quit", custom_cmd=abt.quit_app)
    note.pack(fill="both", expand=1)

    root.mainloop()
    return root


if __name__ == "__main__":
    main()
