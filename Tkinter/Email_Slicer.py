import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title('Email slicer')
root.configure(bg='black')
var = StringVar()
fvar = StringVar()
far = StringVar()


def Email():
    email = emil.get()
    user = email[:email.index('@')]
    var.set('Name: '+user)
    domain = email[email.index('@')+1:email.index('.')]
    fvar.set('Domian: '+domain)
    output = 'Your username {} and your domain name is {}'.format(user, domain)
    far.set(output)


emil = Entry(root, width=50)
emil_l = Label(root, text='Enter your email', bg='black', fg='white')
Button = Button(root, text='submit', command=Email)
result = Label(root, textvariable=var, bg='black', fg='white')
result2 = Label(root, textvariable=fvar, bg='black', fg='white')
result3 = Label(root, textvariable=far, bg='black', fg='white')
emil_l.pack()
emil.pack()
Button.pack()
result.pack()
result2.pack()
result3.pack()
root.mainloop()
