import tkinter as tk
from tkinter import *
import time
from tkinter import messagebox
from tkinter import font

from passlib.crypto.scrypt import validate

root = tk.Tk()
root.title('coundown timer')
root.config(bg='black')


def correct(inp):
    if inp.isdigit():
        return True
    elif inp == "":
        return True
    else:
        return False


hour = IntVar()
minute = IntVar()
second = IntVar()
secons = StringVar()


hour.set(00)
minute.set(00)
second.set(00)

secons.set(' Hours:Mins:Secs')


def submit():
    sec = seconds.get()
    min = minutes.get()
    hor = hours.get()
    cout = int(hor)*3600 + int(min)*60 + int(sec)
    while cout > -1:
        mins, secs = divmod(cout, 60)
        hors = 0
        if mins > 60:
            hors, mins = divmod(mins, 60)
        hour.set("{0:2d}".format(hors))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
        root.update()
        time.sleep(1)
        if (cout == 0):
            messagebox.showinfo("timer", "Time's up ")
        cout -= 1


seconds = Entry(root, width=3, font=(
    'monospace', 20, 'bold'), textvariable=second, fg='blue', bg='black')
minutes = Entry(root, width=3, font=(
    'monospace', 20, 'bold'), textvariable=minute, fg='green', bg='black')
hours = Entry(root, width=3, font=('monospace', 20, 'bold'),
              textvariable=hour, fg='red', bg='black')
start = Button(root, text='start timer', command=submit, bg='cyan', fg='black')
secon = Label(root, bg='black', fg='orange', textvariable=secons,
              font=('monospace', 25, 'bold'))
secon.grid(row=0, column=0, columnspan=4)
empty = Label(root, bg='black', fg='black')

hours.grid(row=1, column=1)
minutes.grid(row=1, column=2)
seconds.grid(row=1, column=3)
empty.grid(row=2, column=2)
start.grid(row=3, column=2)


reg = root.register(correct)
seconds.config(validate="key", validatecommand=(reg, '%P'))
minutes.config(validate="key", validatecommand=(reg, '%P'))
hours.config(validate="key", validatecommand=(reg, '%P'))

root.mainloop()
