from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sqlite3

root = tk.Tk()
root.title('contact book')
root.configure(bg='black')
conn = sqlite3.connect('contactbook.db')
c = conn.cursor()


c.execute("""CREATE TABLE IF NOT EXISTS contact(
    Name text,
    Mobile int,
    Email text,
    Address text)
    """)


def contacts():
    conn = sqlite3.connect('contactbook.db')
    c = conn.cursor()

    c.execute("INSERT INTO contact VALUES(:Name,:Mobile,:Email,:Address)", {
        'Name': name.get(),
        'Mobile': mobile.get(),
        'Email': email.get(),
        'Address': address.get('1.0', 'end-1c')
    })
    conn.commit()
    conn.close()
    name.delete(0, END)
    email.delete(0, END)
    mobile.delete(0, END)
    messagebox.showinfo('contactbook', 'successfully updated')


def query():
    conn = sqlite3.connect('contactbook.db')
    c = conn.cursor()

    c.execute("SELECT *, oid FROM contact")
    records = c.fetchall()
    # print(records)
    print_records = ""
    for record in records:
        print_records += str(record) + "\n"
    file = open("user.txt", "w")
    file.write(print_records)
    file.close()
    query_label = Label(root, text=print_records)
    query_label.pack()
    conn.commit()
    conn.close()


def correct(inp):
    if inp.isdigit():
        return True
    elif inp == "":
        return True
    else:
        return False


def mobilelen():
    pn = mobile.get()
    if len(pn) < 10:
        messagebox.showwarning("hey", "mobile number is invalid")
    elif len(pn) > 10:
        messagebox.showwarning("hey", "mobile number is invalid")
    else:
        contacts()


def filled():
    n = name.get()
    a = address.get('1.0', 'end-1c')
    p = mobile.get()
    e = email.get()
    if n == "" or a == "" or p == "" or e == "":
        messagebox.showerror("fileds are empty", "Please fill all the fields")
    else:
        mobilelen()


name_l = Label(text="Enter First Name: ", bg='black',
               fg='white', font=('Monospace', 14, 'bold'), height=2)
address_l = Label(text="Enter Address: ", bg='black',
                  fg='white', font=('Monospace', 14, 'bold'), height=2)
email_l = Label(text="Enter Email: ", bg='black',
                fg='white', font=('Monospace', 14, 'bold'), height=2)
mobile_l = Label(text="Enter  Mobile_No.: ", bg='black',
                 fg='white', font=('Monospace', 14, 'bold'), height=2)


name = Entry(root, fg='black', width=44)
mobile = Entry(root, fg='black', width=44)
email = Entry(root, fg='black', width=44)
address = Text(root, height=4, width=50)

reg = root.register(correct)
mobile.config(validate="key", validatecommand=(reg, '%P'))


submit = Button(root, text='submit', bg='dodger blue',
                font=('bold'), command=filled)
query_bt = Button(root, text="Save to .txt", command=query)

name_l.pack()
name.pack()
mobile_l.pack()
mobile.pack()
email_l.pack()
email.pack()
address_l.pack()
address.pack()
submit.pack()
query_bt.pack()
root.mainloop()
