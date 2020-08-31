import tkinter as tk
from tkinter import *
import sqlite3
from tkinter import messagebox
from PIL import ImageTk, Image

root = tk.Tk()
root.title('signup database')
root.configure(bg='black')
conn = sqlite3.connect('signup.db')
c = conn.cursor()

# creating the table if it does not exists
c.execute("""CREATE TABLE IF NOT EXISTS signup(
first_name text, 
last_name text,
email text,
password text,
mobile int)
""")


# for entering the values into the table which created in the database
def signup():
    conn = sqlite3.connect('signup.db')
    c = conn.cursor()

    c.execute("INSERT INTO signup VALUES(:first_name, :last_name, :email, :password, :mobile)",
              {
                  'first_name': f_name.get(),
                  'last_name': l_name.get(),
                  'email': email.get(),
                  'password': password.get(),
                  'mobile': mobile.get()
              })
    conn.commit()
    conn.close()

    f_name.delete(0, END)
    l_name.delete(0, END)
    email.delete(0, END)
    password.delete(0, END)
    password2.delete(0, END)
    mobile.delete(0, END)
    messagebox.showinfo('sign-up', "Sign-up, Successful")


# for phone number
def correct(inp):
    if inp.isdigit():
        return True
    elif inp == "":
        return True
    else:
        return False


# for the mobile number lenght
def mobilelen():
    pn = mobile.get()
    if len(pn) < 10:
        messagebox.showwarning("hey", "mobile number is invalid")
    elif len(pn) > 10:
        messagebox.showwarning("hey", "mobile number is invalid")
    else:
        signup()


# for validating the password
def passwordCheck():
    p1 = password.get()
    p2 = password2.get()
    if p1 == p2:
        mobilelen()
    else:
        messagebox.showerror("incorrect", "passwords are not matching")


# for checking the fields if filled or not
def filled():
    fn = f_name.get()
    ln = l_name.get()
    p = mobile.get()
    e = email.get()
    pas1 = password.get()
    pas2 = password2.get()
    if fn == "" or ln == "" or p == "" or e == "" or pas1 == "" or pas2 == "":
        messagebox.showerror("fileds are empty", "Please fill all the fields")
    else:
        passwordCheck()


# for entries
f_name = Entry(root, bg='grey', fg='black', width=30)
l_name = Entry(root, bg='grey', fg='black', width=30)
email = Entry(root, bg='grey', fg='black', width=30)
password = Entry(root, bg='grey', fg='black', width=30)
password2 = Entry(root, bg='grey', fg='black', width=30)
mobile = Entry(root, bg='grey', fg='black', width=30)
my_img = ImageTk.PhotoImage(Image.open("/home/wargun/Pictures/mylogo.png"))
submit = Button(root, text='submit', bg='dodger blue',
                font=('bold'), command=filled)

# validating mobile fields
reg = root.register(correct)
mobile.config(validate="key", validatecommand=(reg, '%P'))


# labels for entries
f_name_l = Label(text="Enter First Name: ", bg='black',
                 fg='white', font=('Monospace', 14, 'bold'), height=2)
l_name_l = Label(text="Enter Last Name: ", bg='black',
                 fg='white', font=('Monospace', 14, 'bold'), height=2)
email_l = Label(text="Enter Your Email: ", bg='black',
                fg='white', font=('Monospace', 14, 'bold'), height=2)
phone_l = Label(text="Enter Your Ph_No.: ", bg='black',
                fg='white', font=('Monospace', 14, 'bold'), height=2)
password_l = Label(text="Enter Your Password: ", bg='black',
                   fg='white', font=('Monospace', 14, 'bold'), height=2)
password2_l = Label(text="Retype Password Again: ", bg='black',
                    fg='white', font=('Monospace', 14, 'bold'), height=2)
my_label = Label(image=my_img, bg='black')
my_label2 = Label(root, text='signup form', bg='black',
                  fg='white', font=('monospace', 30, 'bold'))

# for the place of the entries
f_name.grid(row=1, column=1)
l_name.grid(row=2, column=1)
email.grid(row=3, column=1)
mobile.grid(row=4, column=1)
password.grid(row=5, column=1)
password2.grid(row=6, column=1)

# for the place of the labels
f_name_l.grid(row=1, column=0)
l_name_l.grid(row=2, column=0)
email_l.grid(row=3, column=0)
phone_l.grid(row=4, column=0)
password_l.grid(row=5, column=0)
password2_l.grid(row=6, column=0)
submit.grid(row=7, column=1)
my_label.grid(row=0, column=0)
my_label2.grid(row=0, column=1)
root.mainloop()
