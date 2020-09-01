import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox

root = tk.Tk()
root.title('basic projects')
root.configure(bg='black')
var = StringVar()
fvar = StringVar()


def game():
    inpt = int(inp.get())
    if guess == inpt:
        var.set('you guessed the correct number')
        fvar.set('')
    elif guess < inpt:
        fvar.set('your guess is more than the answer')
    elif guess > inpt:
        fvar.set('your guess is less than the answer')
    else:
        fvar.set('you guess is wrong')
    inp.delete(0, END)


def show():
    messagebox.showinfo('guessed number', guess)


heading = Label(root, text='Guess the number from 1 to 201', fg='white',
                font=('monospace', 20, 'bold'), bg='black')
heading.pack()
guess = random.randint(1, 201)

inp = Entry(root, bg='black', fg='blue',
            font=('monospace', 16))
inp.pack()

result = Label(root, textvariable=var, bg='black',
               fg='green', font=('monospace', 20, 'bold'))
result.pack()
result2 = Label(root, textvariable=fvar, bg='black',
                fg='red', font=('monospace', 20, 'bold'))
result2.pack()
submit = Button(root, text='submit', command=game)
submit.pack()
answer = Button(root, text='show number', command=show)
answer.pack()


root.mainloop()
