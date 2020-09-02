from tkinter import *
import tkinter as tk
import xml.etree.ElementTree as etree
from tkinter import messagebox
import time
import os
import fnmatch
import shutil

# for the main app
root = tk.Tk()
root.title("just learning")
root.configure(bg="black")
data = etree.Element("DATA")


# for writing in xml
def saveData():
    t = time.localtime()
    timestamp = time.strftime('%b-%d-%Y_%H:%M', t)

    user = etree.SubElement(data, 'NAME')
    user.text = name.get()

    mobile = etree.SubElement(data, 'PHONE')
    mobile.text = phone.get()

    Email = etree.SubElement(data, 'EMAIL')
    Email.text = email.get()

    Pass = etree.SubElement(data, 'PASSWORD')
    Pass.text = password.get()

    tree = etree.ElementTree(data)
    tree.write(timestamp + "data.xml")
    return


# for phone number
def correct(inp):
    if inp.isdigit():
        return True
    elif inp == "":
        return True
    else:
        return False


# for checking the fields if filled or not
def filled():
    n = name.get()
    p = phone.get()
    e = email.get()
    pas1 = password.get()
    pas2 = password2.get()
    if n == "" or p == "" or e == "" or pas1 == "" or pas2 == "":
        messagebox.showerror("fileds are empty", "Please fill all the fields")
    else:
        saveData()


def mobilelen():
    pn = phone.get()
    if len(pn) < 10:
        messagebox.showwarning("hey", "mobile number is invalid")
    elif len(pn) > 10:
        messagebox.showwarning("hey", "mobile number is invalid")
    else:
        passwordCheck()
# for validating the password


def passwordCheck():
    p1 = password.get()
    p2 = password2.get()
    if p1 == p2:
        filled()
    else:
        messagebox.showerror("incorrect", "passwords are not matching")
# making global values


def createWidget():
    global phone, email, name, password


# for labels
head_l = Label(text="Welcome to my site, noob.com", bg='black',
               fg='yellowgreen', font=('Monospace', 20, 'bold'))

space = Label(bg='black')

name_l = Label(text="Enter Your Name: ", bg='black',
               fg='white', font=('Monospace', 14, 'bold'), height=2)

email_l = Label(text="Enter Your Email: ", bg='black',
                fg='white', font=('Monospace', 14, 'bold'), height=2)

phone_l = Label(text="Enter Your Ph_No.: ", bg='black',
                fg='white', font=('Monospace', 14, 'bold'), height=2)

password_l = Label(text="Enter Your Password: ", bg='black',
                   fg='white', font=('Monospace', 14, 'bold'), height=2)

password2_l = Label(text="Same Password Again: ", bg='black',
                    fg='white', font=('Monospace', 14, 'bold'), height=2)


# for Entry tags
name = Entry(root, bg='grey', fg='black', width=30)
email = Entry(root, bg='grey', fg='black', width=30)
phone = Entry(root, bg='grey', fg='black', width=30)
password = Entry(root, bg='grey', fg='black', width=30)
password2 = Entry(root, bg='grey', fg='black', width=30)
submit = Button(root, text='Submit', command=mobilelen)
# validating fields
reg = root.register(correct)
phone.config(validate="key", validatecommand=(reg, '%P'))

# for displaying labels on the screen
head_l.grid(row=0, columnspan=3)
space.grid(row=1)
name_l.grid(row=2, column=0)
email_l.grid(row=3, column=0)
phone_l.grid(row=4, column=0)
password_l.grid(row=5, column=0)
password2_l.grid(row=6, column=0)
submit.grid(row=7, column=1)

# for displaying entries on screen
name.grid(row=2, column=1)
email.grid(row=3, column=1)
phone.grid(row=4, column=1)
password.grid(row=5, column=1)
password2.grid(row=6, column=1)

createWidget()
root.mainloop()
