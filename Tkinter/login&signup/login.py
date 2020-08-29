import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3

root = tk.Tk()
root.configure(bg='black')
root.title('login site')


# for login
def login():
    while True:
        email = eml.get()
        password = passw.get()
        with sqlite3.connect("signup.db") as db:
            cursor = db.cursor()
        find_user = ("SELECT * FROM signup WHERE email = ? AND password = ?")
        cursor.execute(find_user, [(email), (password)])
        results = cursor.fetchall()
        if results:
            for i in results:
                user = i[0]
            messagebox.showinfo("login page", "welcome " + user)
            break
        else:
            messagebox.showerror("login page", "invalid credentials")
            break


# entries for the email and stuff
eml = Entry(root, bg='grey', fg='black')
passw = Entry(root, bg='grey', fg='black')
login = Button(root, bg='dodger blue', text='Login',
               fg='white', font=('bold'), command=login)


# labels for the entries
email_l = Label(root, text='Enter Your Email :', bg='black',
                fg='white', font=('monospace', 16, 'bold'))
passw_l = Label(root, text='Enter Your Password :', bg='black',
                fg='white', font=('monospace', 16, 'bold'))


# setiinng up place for the entries
eml.grid(row=1, column=1)
passw.grid(row=2, column=1)
login.grid(row=3, column=1)


# setting up place for the labels
email_l.grid(row=1, column=0)
passw_l.grid(row=2, column=0)

root.mainloop()
