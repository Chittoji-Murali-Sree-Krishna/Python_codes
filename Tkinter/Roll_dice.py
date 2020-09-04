import tkinter as tk
from tkinter import *
import random


root = tk.Tk()
root.title('roll dice')
front = 'white'
back1 = 'beige'
back2 = 'black'
root.config(bg=back1)


dc = StringVar()
dc1 = StringVar()
total = StringVar()
dc.set('?')
dc1.set('?')


def diceRoll():
    value = random.randint(1, 6)
    # dc.set(value)
    value2 = random.randint(1, 6)
    # dc1.set(value2)
    val = str(value)
    val2 = str(value2)
    total.set('The values of Dice1: '+val+' Dice2: '+val2)
    if value == 1:
        dice1.config(fg='green')
        dc.set('*')
    elif value == 2:
        dice1.config(fg='red')
        dc.set('* *')
    elif value == 3:
        dice1.config(fg='yellow')
        dc.set('* * *')
    elif value == 4:
        dice1.config(fg='blue')
        dc.set('* *\n'
               '* *')
    elif value == 5:
        dice1.config(fg='lime')
        dc.set('* * *\n'
               '* *')
    elif value == 6:
        dice1.config(fg='orange')
        dc.set('* * *\n'
               '* * *')
    if value2 == 1:
        dice2.config(fg='green')
        dc1.set('*')
    elif value2 == 2:
        dice2.config(fg='red')
        dc1.set('* *')
    elif value2 == 3:
        dice2.config(fg='yellow')
        dc.set('* * *')
    elif value2 == 4:
        dice2.config(fg='blue')
        dc1.set('* *\n'
                '* *')
    elif value2 == 5:
        dice2.config(fg='lime')
        dc1.set('* * *\n'
                '* *')
    elif value2 == 6:
        dice2.config(fg='orange')
        dc.set('* * *\n'
               '* * *')


head = Label(root, bg=back1, fg='green', font=(
    'monospace', 25, 'bold'), text='Roll the Dice')
head.grid(row=0, column=0, columnspan=3)
lab1 = Label(root, bg=back1, width=30)
lab1.grid(row=1, column=0)
dice1 = Label(root, bg=back2, fg=front, height=4, width=8,
              textvariable=dc, font=('monospace', 20, 'bold'))
dice1.grid(row=1, column=1)
lab = Label(root, bg=back1, width=10)
lab.grid(row=1, column=2)
dice2 = Label(root, bg=back2, fg=front, height=4,
              width=8, textvariable=dc1, font=('monospace', 20, 'bold'))
dice2.grid(row=1, column=3)
roll = Button(root, bg='cyan', fg='black', text='ROLL',
              font=('bold'), command=diceRoll)
roll.grid(row=2, column=2)
vol = Label(root, textvariable=total, font=(
    'monospace', 20, 'bold'), bg=back1, fg='red')
vol.grid(row=3, column=0, columnspan=4)

root.mainloop()
