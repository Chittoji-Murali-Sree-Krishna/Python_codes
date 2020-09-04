from tkinter import *
import tkinter as tk
import random
import string
import sqlite3
from tkinter import messagebox


root = tk.Tk()
root.title('password manager')
root.configure(bg='black')
conn = sqlite3.connect('password.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS password(
Name text, 
Passwd text)
""")


def savedb():
    conn = sqlite3.connect('password.db')
    c = conn.cursor()
    c.execute("INSERT INTO password VALUES(:Name, :Passwd)", {
        'Name': name.get(),
        'Passwd': passw.get()
    })
    conn.commit()
    conn.close()
    name.delete(0, END)
    passwd.set('')
    messagebox.showinfo('sign-up', "saved successfully")


def search():
    Name = getp.get()
    with sqlite3.connect('password.db') as db:
        cursor = db.cursor()
    find_Passd = ('SELECT * FROM password WHERE Name = ?')
    cursor.execute(find_Passd, [(Name)])
    results = cursor.fetchall()
    if results:
        for i in results:
            Passwd = i[1]
            Name = i[0]
            password2.set('the password for '+Name+'is : '+Passwd)
            root.clipboard_append(Passwd)
            getp.delete(0, END)
            break
    else:
        messagebox.showerror(
            'password gen', 'there no such type of app in database')


def get_password():
    letters = string.ascii_letters
    letters2 = string.ascii_letters
    option = '_-*@~!$%?'
    option2 = '_-*@~!$%?'
    val = '123456789'
    val2 = '123456789'
    result_str = ''.join(random.choice(letters) for i in range(5))
    result_str2 = ''.join(random.choice(letters2) for j in range(8))
    opt = ''.join(random.choice(option) for k in range(2))
    opt2 = ''.join(random.choice(option2) for k in range(2))
    value = ''.join(random.choice(val) for l in range(3))
    value2 = ''.join(random.choice(val2) for l in range(3))
    passwd.set(result_str + opt+value+result_str2+opt2+value2)
    root.clipboard_append(passw.get())


def filled():
    nm = name.get()
    if len(nm) < 4:
        messagebox.showwarning(
            'password gen', 'this cant be proceeded without name & it must be more than 4 letters')
    else:
        get_password()


def filled2():
    nm = name.get()
    ps = passw.get()
    if nm == "" or ps == "":
        messagebox.showwarning(
            'password gen', 'you cant save empty values to database')
    else:
        savedb()


def filled3():
    gp = getp.get()
    if gp == "":
        messagebox.showwarning(
            'password gen', 'there are no empty values in databse')
    else:
        search()


passwd = StringVar()
password2 = StringVar()


mainl = Label(root, bg='black', fg='white', font=(
    'monospace', 25, 'bold'), text='Password Manager')
namel = Label(root, bg='black', fg='blue', font=(
    'monospace', 20, 'bold'), text='Enter App name : ')

passwl = Label(root, bg='black', fg='blue', font=(
    'monospace', 20, 'bold'), text='Your password : ')
infol = Label(root, bg='black', fg='orange',
              text='this will be automatically saved to your clipboard', font=('bold', 12))
showl = Label(root, bg='black', fg='white',
              text='To retrive the password from datbase', font=('monospace', 25, 'bold'))
getpl = Label(root, bg='black', fg='blue',
              text='Enter your App name :', font=('monospace', 20, 'bold'))
passl = Label(root, textvariable=password2, fg='green',
              bg='black', font=('monospace', 16, 'bold'))


name = Entry(root, bg='black', fg='red', font=('monospace', 16), width=25)
passw = Entry(root, font=('monospace', 16), borderwidth=0,
              textvariable=passwd, highlightthickness=0, width=25)
passw.config(state='disabled', disabledbackground='black',
             disabledforeground='green')
getp = Entry(root, bg='black', fg='red', font=('monospace', 16), width=25)


get = Button(root, bg='blue', font=('bold'),
             text='get password', command=filled)
get2 = Button(root, bg='green', font=('bold'),
              text='save password', command=filled2)
get3 = Button(root, bg='green', font=('bold'),
              text='search password', command=filled3)

mainl.grid(row=0, columnspan=4, column=0)
namel.grid(row=1, column=0)
passwl.grid(row=2, column=0)
infol.grid(row=5, column=1)
showl.grid(row=6, column=0, columnspan=4)
getpl.grid(row=7, column=0)
passl.grid(row=9, column=0, columnspan=4)

name.grid(row=1, column=1)
passw.grid(row=2, column=1)
getp.grid(row=7, column=1)


get.grid(row=3, column=1)
get2.grid(row=3, column=0)
get3.grid(row=8, column=1)


root.mainloop()
