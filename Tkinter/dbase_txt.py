import sqlite3
from tkinter import *
import tkinter as tk

root = tk.Tk()
root.title('teaching my dumb mind')
root.configure(bg="black")

conn = sqlite3.connect('address.db')

c = conn.cursor()

c.execute("""CREATE TABLE addresses(
first_name text,
last_name text,
address text,
city text,
state text,
pincode int)""")


def submit():

    conn = sqlite3.connect('address.db')

    c = conn.cursor()

    c.execute(
        "INSERT INTO addresses VALUES (:first_name, :last_name, :address, :city, :state, :pincode)",
        {
            'first_name': first_name.get(),
            'last_name': last_name.get(),
            'address': address.get(),
            'city': city.get(),
            'state': state.get(),
            'pincode': pincode.get()
        })
    conn.commit()
    conn.close()

    first_name.delete(0, END)
    last_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    pincode.delete(0, END)


def query():
    conn = sqlite3.connect('address.db')
    c = conn.cursor()

    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    # print(records)
    print_records = ""
    for record in records:
        print_records += str(record) + "\n"
    file = open("user.txt", "w")
    file.write(print_records)
    file.close()
    conn.commit()
    conn.close()


first_name = Entry(root, width=30)
last_name = Entry(root, width=30)
address = Entry(root, width=30)
city = Entry(root, width=30)
state = Entry(root, width=30)
pincode = Entry(root, width=30)
submit_bt = Button(root, text="Add to Database", command=submit)
query_bt = Button(root, text="Save to .txt", command=query)


first_name_l = Label(root, text="First Name")
last_name_l = Label(root, text="Last Name")
address_l = Label(root, text="Address")
city_l = Label(root, text="City")
state_l = Label(root, text="State")
pincode_l = Label(root, text="Pincode")

first_name.grid(row=0, column=1)
last_name.grid(row=1, column=1)
address.grid(row=2, column=1)
city.grid(row=3, column=1)
state.grid(row=4, column=1)
pincode.grid(row=5, column=1)
submit_bt.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
query_bt.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


first_name_l.grid(row=0, column=0)
last_name_l.grid(row=1, column=0)
address_l.grid(row=2, column=0)
city_l.grid(row=3, column=0)
state_l.grid(row=4, column=0)
pincode_l.grid(row=5, column=0)


conn.commit()

conn.close()
root.mainloop()
