from tkinter import *
import sqlite3
# Create the main window
root = Tk()
root.title("My Tkinter Application")
root.iconbitmap('resources/icons/home.ico')
# root.geometry("400x400")

# conn = sqlite3.connect('address_book.db')
# cur = conn.cursor()

# cur.execute("""
#             CREATE TABLE IF NOT EXISTS addresses (
#             first_name text,
#             last_name text,
#             address text,
#             city text,
#             state text,
#             zipcode integer
#             )
#             """)


def submit():
    conn = sqlite3.connect('address_book.db')
    cur = conn.cursor()

    cur.execute("INSERT INTO addresses VALUES(:f_name,:l_name,:address,:city,:state,:zipcode)",
                {
                    'f_name': f_name.get(),
                    'l_name': l_name.get(),
                    'address': address.get(),
                    'city': city.get(),
                    'state': state.get(),
                    'zipcode': zipcode.get(),
                })

    conn.commit()
    conn.close()

    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


def query():
    conn = sqlite3.connect('address_book.db')
    cur = conn.cursor()

    cur.execute("SELECT *,oid FROM addresses")
    print(cur.fetchall())

    conn.close()
    # show_label = Label(root, text="Delete ID", anchor=W)
    # show_label.grid(row=12, column=0, padx=20, pady=(5, 0), sticky=W+E)


def delete():
    conn = sqlite3.connect('address_book.db')
    cur = conn.cursor()

    cur.execute("DELETE FROM addresses WHERE oid=" + delete_box.get())

    conn.commit()
    conn.close()
    delete_box.delete(0, END)


def update():
    conn = sqlite3.connect('address_book.db')
    cur = conn.cursor()

    cur.execute("""UPDATE addresses SET
                first_name = :first,
                last_name = :last,
                address = :address,
                city = :city,
                state = :state,
                zipcode = :zipcode
                WHERE oid=:oid""",
                {
                    'first': f_name_ed.get(),
                    'last': l_name_ed.get(),
                    'address': address_ed.get(),
                    'city': city_ed.get(),
                    'state': state_ed.get(),
                    'zipcode': zipcode_ed.get(),
                    'oid': delete_box.get()
                }
                )

    conn.commit()
    conn.close()
    editor.destroy()


def edit():
    global editor
    editor = Tk()
    editor.title("Update Record")
    editor.iconbitmap('resources/icons/home.ico')
    # editor.geometry("400x400")

    conn = sqlite3.connect('address_book.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM addresses WHERE oid=" + delete_box.get())
    result = cur.fetchall()

    global f_name_ed
    global l_name_ed
    global address_ed
    global city_ed
    global state_ed
    global zipcode_ed

    f_name_ed = Entry(editor, width=30)
    f_name_ed.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_ed = Entry(editor, width=30)
    l_name_ed.grid(row=1, column=1, padx=20)
    address_ed = Entry(editor, width=30)
    address_ed.grid(row=2, column=1, padx=20)
    city_ed = Entry(editor, width=30)
    city_ed.grid(row=3, column=1, padx=20)
    state_ed = Entry(editor, width=30)
    state_ed.grid(row=4, column=1, padx=20)
    zipcode_ed = Entry(editor, width=30)
    zipcode_ed.grid(row=5, column=1, padx=20)

    f_label = Label(editor, text="First Name", anchor=W)
    f_label.grid(row=0, column=0, padx=20, pady=(10, 0))
    l_label = Label(editor, text="Last Name", anchor=W)
    l_label.grid(row=1, column=0, padx=20)
    address_label = Label(editor, text="Address", anchor=W)
    address_label.grid(row=2, column=0, padx=20)
    city_label = Label(editor, text="city", anchor=W)
    city_label.grid(row=3, column=0, padx=20)
    state_label = Label(editor, text="state", anchor=W)
    state_label.grid(row=4, column=0, padx=20)
    zipcode_label = Label(editor, text="zipcode", anchor=W)
    zipcode_label.grid(row=5, column=0, padx=20)

    for record in result:
        f_name_ed.insert(0, record[0])
        l_name_ed.insert(0, record[1])
        address_ed.insert(0, record[2])
        city_ed.insert(0, record[3])
        state_ed.insert(0, record[4])
        zipcode_ed.insert(0, record[5])

    save_btn = Button(editor, text="Save", command=update).grid(row=6, column=0, columnspan=2, padx=10, pady=(5, 0),  sticky=W+E)
    cancel_btn = Button(editor, text="Cancel", command=editor.destroy).grid(row=7, column=0, columnspan=2, padx=10, pady=(5, 0),  sticky=W+E)

    conn.commit()
    conn.close()
    # delete_box.delete(0, END)


f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)
state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)
delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, padx=20, pady=(5, 0))

f_label = Label(root, text="First Name", anchor=W)
f_label.grid(row=0, column=0, padx=20, pady=(10, 0))
l_label = Label(root, text="Last Name", anchor=W)
l_label.grid(row=1, column=0, padx=20)
address_label = Label(root, text="Address", anchor=W)
address_label.grid(row=2, column=0, padx=20)
city_label = Label(root, text="city", anchor=W)
city_label.grid(row=3, column=0, padx=20)
state_label = Label(root, text="state", anchor=W)
state_label.grid(row=4, column=0, padx=20)
zipcode_label = Label(root, text="zipcode", anchor=W)
zipcode_label.grid(row=5, column=0, padx=20)
delete_label = Label(root, text="Delete ID", anchor=W)
delete_label.grid(row=9, column=0, padx=20, pady=(5, 0))


sub_btn = Button(root, text="Submit", command=submit).grid(row=6, column=0, columnspan=2, padx=10, pady=(5, 0),  sticky=W+E)
query_btn = Button(root, text="Query", command=query).grid(row=7, column=0, columnspan=2, padx=10, pady=(5, 0),  sticky=W+E)
del_btn = Button(root, text="Delete", command=delete).grid(row=10, column=0, columnspan=2, padx=10, pady=(5, 0),  sticky=W+E)
edit_btn = Button(root, text="Update", command=edit).grid(row=11, column=0, columnspan=2, padx=10, pady=(5, 0),  sticky=W+E)

# conn.commit()
# conn.close()

# Start the event loop
root.mainloop()
