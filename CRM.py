import psycopg2
from tkinter import *

# Create the main window
root = Tk()
root.title("My Tkinter Application")
# root.iconbitmap("resources/icons/home.ico")
# root.geometry("400x400")

conn = psycopg2.connect(
    host="localhost",
    database="tkinter",
    user="postgres",
    password="I536ib9E6HVxgc"
)

cursor = conn.cursor()


def create_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS customers (
                   first_name VARCHAR(255),
                   last_name VARCHAR(255),
                   zipcode INT,
                   price_paid DECIMAL(10,2),
                   user_id SERIAL PRIMARY KEY
                   )""")
# create_table()


def alter_table():
    cursor.execute("""
        ALTER TABLE customers
        ADD COLUMN email VARCHAR(255),
        ADD COLUMN address_1 VARCHAR(255),
        ADD COLUMN address_2 VARCHAR(255),
        ADD COLUMN city VARCHAR(50),
        ADD COLUMN state VARCHAR(50),
        ADD COLUMN country VARCHAR(255),
        ADD COLUMN phone VARCHAR(255),
        ADD COLUMN payment_method VARCHAR(50),
        ADD COLUMN discount VARCHAR(255);
    """)
    conn.commit()


def list_tables():
    cursor.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public'
    """)
    for row in cursor.fetchall():
        table_name = row[0]
        text_widget = Text(root, wrap="word", width=50, height=10)  # Use "word" wrap
        text_widget.insert(END, f"Table: {table_name}\n")
        text_widget.grid(row=len(entry_fields)+3, column=0, columnspan=2)


def show_columns(table_name):
    cursor.execute(f"""
        SELECT column_name
        FROM information_schema.columns
        WHERE table_name = '{table_name}'
    """)
    columns = [row[0] for row in cursor.fetchall()]
    text_widget = Text(root, wrap="word", width=50, height=10)
    text_widget.insert(END, f"Columns in table '{table_name}':\n")
    for column in columns:
        text_widget.insert(END, f"- {column}\n")
    text_widget.grid(row=len(entry_fields)+4, column=0, columnspan=2)

# Function to create input fields for each column


def create_input_fields():
    global entry_fields
    entry_fields = {}

    # Column names
    columns = [
        "user_id",
        "first_name",
        "last_name",
        "zipcode",
        "price_paid",
        "email",
        "address_1",
        "address_2",
        "city",
        "state",
        "country",
        "phone",
        "payment_method",
        "discount"
    ]

    for i, column in enumerate(columns):
        Label(root, text=column.capitalize() + ":").grid(row=i, column=0, sticky=W)
        if column == "user_id":
            # User ID is auto-generated, so use a read-only field
            entry_fields[column] = Label(root, text="Auto-Generated")
        else:
            entry_fields[column] = Entry(root)
        entry_fields[column].grid(row=i, column=1)


# Function to insert data into the database
def insert_data():
    data = {}
    for column, entry in entry_fields.items():
        if column != 'user_id':
            data[column] = entry.get()
            entry_fields[column].delete(0, END)

    # Insert data into the database
    try:
        cursor.execute(
            """
            INSERT INTO customers (
                first_name, last_name, zipcode, price_paid, email, address_1, address_2,
                city, state, country, phone, payment_method, discount
            ) VALUES (%(first_name)s, %(last_name)s, %(zipcode)s, %(price_paid)s, %(email)s, 
                      %(address_1)s, %(address_2)s, %(city)s, %(state)s, %(country)s, 
                      %(phone)s, %(payment_method)s, %(discount)s)
            """,
            data
        )
        conn.commit()
    except Exception as e:
        print("Error inserting data:", e)


def list_customers():
    list_customer_query = Tk()
    list_customer_query.title("List of customers")
    cursor.execute("SELECT * FROM customers")
    result = cursor.fetchall()
    for index, x in enumerate(result):
        num = 0
        for y in x:
            lookup = Label(list_customer_query, text=y)
            lookup.grid(row=index, column=num)
            num += 1
    exit_btn = Button(list_customer_query, text="Quit", command=list_customer_query.destroy)
    exit_btn.grid(row=len(result), column=0, columnspan=2)
    return


# Create the input fields
create_input_fields()

# list_button = Button(root, text="List All Table", command=list_tables)
# list_button.grid(row=len(entry_fields), column=0, columnspan=2)

# alter_button = Button(root, text="Alter Table", command=alter_table)
# alter_button.pack()

# table_label = Label(root, text="Table Name:")
# table_label.grid(row=len(entry_fields)+1, column=0, columnspan=2, sticky=W)

# table_entry = Entry(root)
# table_entry.grid(row=len(entry_fields)+1, column=1, columnspan=2)


# table_button = Button(root, text="Show Column", command=lambda: show_columns(table_entry.get()))
# table_button.grid(row=len(entry_fields)+2, column=0, columnspan=2)

# Create the insert button
insert_button = Button(root, text="Insert Data", command=insert_data)
insert_button.grid(row=len(entry_fields)+1, column=0)

insert_button = Button(root, text="View Data", command=list_customers)
insert_button.grid(row=len(entry_fields)+1, column=1)

# Start the event loop
root.mainloop()
conn.close()
