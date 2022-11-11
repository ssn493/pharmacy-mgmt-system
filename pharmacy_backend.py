import sqlite3 as sql
import datetime
import random as rn

conn = sql.connect("test.db")
cursor = conn.cursor()

# Constants:
name = "name"
fields = "fields"

VARCHAR = "VARCHAR(50)"
INT = "INT"
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
        schema_text = schema_text + " ".join(column_def) + ", "
    create_cmd = f"CREATE TABLE IF NOT EXISTS {table[name]}({schema_text})"
    # cursor.execute(create_cmd)
    print(create_cmd)


def select_statement(table_name, cols="*", condition="*"):
    global cursor
    if condition == "*":
        sel_cmd = f"SELECT {cols} FROM {table_name}"
    else:
        sel_cmd = f"SELECT {cols} FROM {table_name} WHERE {condition}"
    cursor.execute(sel_cmd)
    raw_data = cursor.fetchall()
    data = data_dict_fmt(raw_data)
    return data


def insert_from_dict(name, data_dict):
    global cursor
    attributes = str(tuple(data_dict.keys()))
    values = str(tuple(data_dict.values()))
    ins_cmd = "INSERT INTO {0}{1} VALUES {2}".format(name, attributes, values)
    cursor.execute(ins_cmd)


meds = {
    name: "meds",
    fields: [
        ("id", INT, PRIMARY_KEY, "AUTOINCREMENT"),
        ("name", VARCHAR),
        ("manufacturer", VARCHAR),
        ("stock_quantity", INT),
        ("mrp", FLOAT),
        ("gst_percent", INT),
        (""),
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
    ],
}

prescriptions = {
    name: "prescs",
    fields: [
        ("presc_id", INT, PRIMARY_KEY, "AUTOINCREMENT"),
        ("cust_id", INT),
        ("doctor_name", VARCHAR),
        ("date_of_issue", DATE),
        (FOREIGN_KEY("cust_id", "custs", "cust_id")),
    ],
}

txn_orders = {
    name: "txns",
    fields: [
        ("uid", INT, PRIMARY_KEY, "AUTOINCREMENT"),
        ("o_id", INT),
        ("med_id", INT),
        ("qty", INT),
        ("txn_datetime", VARCHAR),
        (FOREIGN_KEY("med_id", meds[name], "id")),
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


def register_new_customer(data):
    insert_from_dict(customers[name], data)


def add_new_medicines(data):
    insert_from_dict(meds[name], data)


def add_presc(cust_id, doctor, medicines, date):
    """medicines => list of tuples containing med_id and quantity"""

    if execute_sql(f"SELECT * FROM {prescriptions[name]}") == []:
        presc_id = 0000
        insert_from_dict(
            prescriptions[name],
            {
                "presc_id": presc_id,
                "cust_id": cust_id,
                "doctor": doctor,
                "date_of_issue": date,
            },
        )
    else:
        prescriptions.insert_as_dict(
            {"cust_id": cust_id, "doctor": doctor, "date_of_issue": date}
        )
        presc_id = execute_sql(
            f"select top 1 presc_id from {prescriptions.name} order by presc_id"
        )
    for med in medicines:
        data = {
            "cust_id": cust_id,
            "presc_id": presc_id,
            "med_id": med[0],
            "quantity": med[1],
        }
        insert_from_dict(txn_orders[name], data)



def get_med_quantity(med_id):
    med_qty = select_statement(meds[name], "stock_quantity", f"id = {med_id}")
    med_qty = int(med_qty)
    return med_qty

def search_by_field(table, search_attr, value):
    data_list = list(execute_sql(f"SELECT * FROM {table[name]} WHERE {search_attr} LIKE {value}%"))
    return data_list


def search_meds(medicine_name):
    med_list = execute_sql(f"SELECT * FROM meds WHERE name LIKE {medicine_name}%")
    return med_list


def search_cust_by_name(cust_name):
    cust_list = execute_sql(f"SELECT * FROM cust WHERE name LIKE {cust_name}%")
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


if __name__ == "__main__":
    pass


conn.close()
