import sqlite3 as sql
import datetime
import random as rn

conn = sql.connect("test.db")
cursor = conn.cursor()

# Constants:
name = "name"
fields = "fields"

VARCHAR = "VARCHAR(50)"
INT = "INTEGER"
FLOAT = "FLOAT"
DATE = "DATE"

PRIMARY_KEY = "PRIMARY KEY"
FOREIGN_KEY = lambda key_field, foreign_table, foreign_key: "FOREIGN KEY ({0}) REFERENCES {1}({2})".format(
    key_field, foreign_table, foreign_key
)


def execute_sql(sql):
    global cursor
    cursor.execute(sql)
    return cursor.fetchall()


def close():
    conn.commit()
    conn.close()


def data_dict_fmt(raw_data, fieldnames):
    data = {key: [] for key in fieldnames}
    data["raw_data"] = raw_data
    for row in raw_data:
        for index, attr in enumerate(row):
            data[fieldnames[index]].append(attr[0])
    return data


def get_field_names(table):
    field_names = []
    for field_data in table[fields]:
        if len(field_data) > 1:
            field_names.append(field_data[0])
    return field_names


def create_table(table):
    global cursor
    schema_text = ""
    for column_def in table[fields]:
        if isinstance(column_def, str):
            schema_text = schema_text + column_def + ", "
        elif len(column_def) > 1:
            schema_text = schema_text + " ".join(column_def) + ", "
        else:
            pass

    create_cmd = f"CREATE TABLE IF NOT EXISTS {table[name]}({schema_text[:-2]})"
    cursor.execute(create_cmd)


def select_statement(table_name, cols="*", condition="*"):
    global cursor
    if condition == "*":
        sel_cmd = f"SELECT {cols} FROM {table_name}"
    else:
        sel_cmd = f"SELECT {cols} FROM {table_name} WHERE {condition}"
    cursor.execute(sel_cmd)
    data = cursor.fetchall()
    return data


def insert_from_dict(table, data_dict):
    global cursor
    attributes = str(tuple(data_dict.keys()))
    values = str(tuple(data_dict.values()))
    ins_cmd = "INSERT INTO {0}{1} VALUES {2}".format(table[name], attributes, values)
    print(ins_cmd)
    cursor.execute(ins_cmd)


meds = {
    name: "meds",
    fields: [
        ("id", INT, PRIMARY_KEY, "AUTOINCREMENT"),
        ("name", VARCHAR),
        ("manufacturer", VARCHAR),
        ("stock_qty", INT),
        ("mrp", FLOAT),
        ("gst_percent", INT),
    ],
}

customers = {
    name: "custs",
    fields: [
        ("cust_id", INT, PRIMARY_KEY, "AUTOINCREMENT"),
        ("name", VARCHAR),
        ("age", INT),
        ("sex", VARCHAR),
        ("address", VARCHAR),
        ("phone_no", INT),
    ],
}

orders = {
    name: "cust_orders",
    fields: [
        (
            "order_id",
            INT,
            "NOT NULL",
            "UNIQUE",
        ),
        ("cust_id", INT),
        ("med_id", INT),
        ("qty", INT),
        ("txn_date", VARCHAR),
        ("PRIMARY KEY (order_id, cust_id, med_id)"),
        (
            FOREIGN_KEY("med_id", meds[name], "id"),
            "ON DELETE CASCADE ON UPDATE NO ACTION",
        ),
        (
            FOREIGN_KEY("cust_id", customers[name], "cust_id"),
            "ON DELETE CASCADE ON UPDATE NO ACTION",
        ),
    ],
}

emp = {
    name: "employees",
    fields: [
        ("emp_id", VARCHAR, PRIMARY_KEY),
        ("dept", VARCHAR),
        ("password", VARCHAR),
    ],
}

inv_orders = {
    name: "inventory_order",
    fields: [
        ("order_id", INT, PRIMARY_KEY, "AUTOINCREMENT"),
        ("order_name", VARCHAR),
        ("order_date", DATE),
        ("med_id", INT),
        ("quantity", INT),
        ("status", VARCHAR),
        (FOREIGN_KEY("med_id", meds[name], "id"), " ON DELETE CASCADE"),
    ],
}


receipt = """
    ABC PHARMACY

    NAME:{0} AGE:{1} SEX:{2}                   DATE:{3}
    Presc. By: {4}


    MEDICINE    QTY    MRP    GST   AMOUNT
    {5}
                        NET AMOUNT:{6}

    """
def search_by_field(table, search_attr, value):
    data_list = list(
        execute_sql(f"SELECT * FROM {table[name]} WHERE {search_attr} LIKE '{value}%'")
    )
    return data_list


def get_table(table):
    data_list = list(execute_sql(f"SELECT * FROM {table[name]}"))
    return data_list


def register_new_customer(name, age, sex, addr, ph_no):
    execute_sql(
        f"INSERT INTO {customers[name]} VALUES ('{name}',{age},'{sex}','{stock_qty}',{ph_no}) "
    )

def delete_customer(cust_id):
    execute_sql(
        f"DELETE FROM {customers[name]} WHERE cust_id={cust_id};"
    )

def add_new_medicine(med_id, name, manufacturer, stock_qty, mrp, gst_percent):
    execute_sql(
        f"INSERT INTO {meds[name]} VALUES ({med_id},'{name}','{manufacturer}',{stock_qty},{mrp},{gst_percent}) "
    )

def delete_medicine(med_id):
    execute_sql(
        f"DELETE FROM {meds[name]} WHERE med_id={med_id};"
    )



# ui helper functions:
def get_med_quantity(med_name):
    med_qty = execute_sql(f"SELECT stock_qty FROM {meds[name]} WHERE name = {med_name}")
    med_qty = int(med_qty)
    return med_qty


def check_med_availability(med_name, qty):
    return get_med_quantity(med_name) >= qty


def search_med_by_name(medicine_name):
    med_list = execute_sql(f"SELECT * FROM meds WHERE name LIKE '{medicine_name}%'")
    return med_list


def search_cust_by_name(cust_name):
    cust_list = execute_sql(
        f"SELECT * FROM {customers[name]} WHERE name LIKE '{cust_name}%'"
    )
    return cust_list


def search_cust_by_phone_no(phone_no):
    cust_list = execute_sql(
        f"SELECT * FROM {customers[name]} WHERE phone_no={phone_no}"
    )
    return cust_list


def filter_custs(name_cond, age_cond, sex_cond):
    rel_ops = "<>="
    if name_cond == "" or not name_cond[0] in rel_ops:
        name_cond_str = ""
        n = False
    else:
        name_cond_str = "Name {}".format(name_cond)
    if age_cond == "" or not age_cond[0] in rel_ops:
        age_cond_str = ""
        a = False
    else:
        age_cond_str = "Age {}".format(age_cond)

    if sex_cond == "" or not sex_cond[0] in rel_ops:
        sex_cond_str = ""
        s = False
    else:
        sex_cond_str = "Sex {}".format(sex_cond)

    if not (n and a and s):
        cmd = "SELECT * FROM custs"
    else:
        cmd = (
            f"SELECT * FROM custs WHERE {name_cond_str} {age_cond_str} {sex_cond_str};"
        )


def cust_create_new_order(cust_id, medicine_data, txn_date):
    if execute_sql(f"SELECT * FROM {orders[name]}") == []:
        order_id = 0000
    else:
        order_id = f"(SELECT MAX(order_id)+1 FROM {orders[name]})"
    for data_item in medicine_data:
        med_id, qty = data_item
        execute_sql(
            f"INSERT INTO {orders[name]} VALUES ({order_id}, {cust_id}, {med_id}, {qty}, {txn_date})"
        )


def cust_show_past_orders(cust_id):
    order_list = execute_sql(
        f"SELECT DISTINCT order_id FROM {orders[name]} WHERE cust_id={cust_id}"
    )
    return order_list


def cust_show_order_details(order_id):
    medicine_details = execute_sql(
        f"SELECT {meds[name]}.name, {orders[name]}.qty FROM {meds[name]},{orders[name]} WHERE {meds[name]}.id={orders[name]}.med_id AND {orders[name]}.order_id={order_id}"
    )
    return list(medicine_details)


def login_emp(emp_id, password):
    stored_password = execute_sql(
        f"SELECT password FROM {emp[name]} WHERE emp_id={emp_id}"
    )
    if password == str(stored_password):
        return True
    else:
        return False


def place_inv_order(medid, med_name, qty):
    global cursor
    select_cmd = f"SELECT mrp FROM {meds[name]} WHERE med_id={med_id};"
    cursor.execute(select_cmd)
    val = cursor.fetchone()[0]
    amt = val * qty
    insert_cmd = f"""INSERT INTO {inv_orders[name]} (order_name,order_date,item_id,quantity,order_amount,status) 
                    VALUES('{med_name}', '{datetime.date.today()}', 
                    {med_id},{qty},{amt} ,'Pending' );"""
    # print(insert_cmd)
    cursor.execute(insert_cmd)
    conn.commit()


def change_inv_order_status(order_id, med_id):
    global cursor
    update_cmd = (
        f"UPDATE {inv_orders[name]} SET status='Received' WHERE order_id={order_id};"
    )
    select_cmd = f"SELECT stock_qty,amount FROM {meds[name]} WHERE med_id={med_id};"
    # write select cmd for fetching qty of order placed from inventory orders
    # and add it with stock_qty and update it in items table
    select2_cmd = f"SELECT quantity FROM {inv_orders[name]}  WHERE order_id={order_id};"

    cursor.execute(select_cmd)
    result = cursor.fetchone()
    val1 = result[0]
    amt = result[1]

    cursor.execute(select2_cmd)
    val2 = cursor.fetchone()[0]

    updated_qty = val1 + val2
    updated_amt = updated_qty * amt
    update2_cmd = f"UPDATE {meds[name]}  SET stock_qty={updated_qty} , total_amount= {updated_amt} WHERE med_id={med_id};"

    cursor.execute(update_cmd)
    cursor.execute(update2_cmd)
    conn.commit()


execute_sql("PRAGMA foreign_keys=on")
create_table(customers)
create_table(meds)
create_table(orders)
create_table(emp)
create_table(inv_orders)

if __name__ == "__main__":
    conn.close()
