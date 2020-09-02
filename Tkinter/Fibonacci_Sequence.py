import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title('fibonacci sequence')


def fibonacci():
    inpt = int(inp.get())
    n1, n2 = 0, 1
    count = 0
    output = ''
    output2 = ''
    if inpt <= 0:
        output = 'please enter a positive number'
    elif inpt == 1:
        output = 'fibonacci sequence upto'
    else:
        output = 'fibonacci sequence upto'
        while count < inpt:
            output2 = n1
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1

    out = Label(root, text=output)
    out.pack()
    out2 = Label(root, text=output2)
    out2.pack()


inp = Entry(root, width=10)
inp.pack()
btn = Button(root, text='submit', command=fibonacci)
btn.pack()


root.mainloop()
