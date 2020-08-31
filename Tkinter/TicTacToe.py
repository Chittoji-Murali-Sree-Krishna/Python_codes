from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title('warlords - Tic-Tac_Toe')
root.geometry("400x400")
root.configure(bg='black')
clicked = True
count = 0


def disable_all_buttons():
    but1.config(state=DISABLED)
    but2.config(state=DISABLED)
    but3.config(state=DISABLED)

    but4.config(state=DISABLED)
    but5.config(state=DISABLED)
    but6.config(state=DISABLED)

    but7.config(state=DISABLED)
    but8.config(state=DISABLED)
    but9.config(state=DISABLED)


def whowon():
    global winner
    winner = False

    if but1["text"] == "X" and but2["text"] == "X" and but3["text"] == "X":
        but1.config(bg="red")
        but2.config(bg="red")
        but3.config(bg="red")
        winner = True
        messagebox.showinfo("", "X wins")
        disable_all_buttons()

    elif but4["text"] == "X" and but5["text"] == "X" and but6["text"] == "X":
        but4.config(bg="red")
        but5.config(bg="red")
        but6.config(bg="red")
        winner = True
        messagebox.showinfo("", "X wins")
        disable_all_buttons()

    elif but7["text"] == "X" and but8["text"] == "X" and but9["text"] == "X":
        but7.config(bg="red")
        but8.config(bg="red")
        but9.config(bg="red")
        winner = True
        messagebox.showinfo("", "X wins")
        disable_all_buttons()

    elif but1["text"] == "X" and but5["text"] == "X" and but9["text"] == "X":
        but1.config(bg="red")
        but5.config(bg="red")
        but9.config(bg="red")
        winner = True
        messagebox.showinfo("", "X wins")
        disable_all_buttons()

    elif but3["text"] == "X" and but5["text"] == "X" and but7["text"] == "X":
        but3.config(bg="red")
        but5.config(bg="red")
        but7.config(bg="red")
        winner = True
        messagebox.showinfo("", "X wins")
        disable_all_buttons()

    elif but1["text"] == "X" and but4["text"] == "X" and but7["text"] == "X":
        but1.config(bg="red")
        but4.config(bg="red")
        but7.config(bg="red")
        winner = True
        messagebox.showinfo("", "X wins")
        disable_all_buttons()

    elif but2["text"] == "X" and but5["text"] == "X" and but8["text"] == "X":
        but2.config(bg="red")
        but5.config(bg="red")
        but8.config(bg="red")
        winner = True
        messagebox.showinfo("", "X wins")
        disable_all_buttons()

    elif but3["text"] == "X" and but6["text"] == "X" and but9["text"] == "X":
        but3.config(bg="red")
        but6.config(bg="red")
        but9.config(bg="red")
        winner = True
        messagebox.showinfo("", "X wins")
        disable_all_buttons()

    elif but1["text"] == "O" and but2["text"] == "O" and but3["text"] == "O":
        but1.config(bg="red")
        but2.config(bg="red")
        but3.config(bg="red")
        winner = True
        messagebox.showinfo("", "O wins")
        disable_all_buttons()

    elif but4["text"] == "O" and but5["text"] == "O" and but6["text"] == "O":
        but4.config(bg="red")
        but5.config(bg="red")
        but6.config(bg="red")
        winner = True
        messagebox.showinfo("", "O wins")
        disable_all_buttons()

    elif but7["text"] == "O" and but8["text"] == "O" and but9["text"] == "O":
        but7.config(bg="red")
        but8.config(bg="red")
        but9.config(bg="red")
        winner = True
        messagebox.showinfo("", "O wins")
        disable_all_buttons()

    elif but1["text"] == "O" and but5["text"] == "O" and but9["text"] == "O":
        but1.config(bg="red")
        but5.config(bg="red")
        but9.config(bg="red")
        winner = True
        messagebox.showinfo("", "O wins")
        disable_all_buttons()

    elif but3["text"] == "O" and but5["text"] == "O" and but7["text"] == "O":
        but3.config(bg="red")
        but5.config(bg="red")
        but7.config(bg="red")
        winner = True
        messagebox.showinfo("", "O wins")
        disable_all_buttons()

    elif but1["text"] == "O" and but3["text"] == "O" and but7["text"] == "O":
        but1.config(bg="red")
        but3.config(bg="red")
        but7.config(bg="red")
        winner = True
        messagebox.showinfo("", "O wins")
        disable_all_buttons()

    elif but2["text"] == "O" and but5["text"] == "O" and but8["text"] == "O":
        but2.config(bg="red")
        but5.config(bg="red")
        but8.config(bg="red")
        winner = True
        messagebox.showinfo("", "O wins")
        disable_all_buttons()

    elif but3["text"] == "O" and but6["text"] == "O" and but9["text"] == "O":
        but3.config(bg="red")
        but6.config(bg="red")
        but9.config(bg="red")
        winner = True
        messagebox.showinfo("", "O wins")
        disable_all_buttons()

    if count == 9 and winner == False:
        messagebox.showinfo("", "its a tie")


def b_click(but):
    global clicked, count

    if but["text"] == "" and clicked == True:
        but["text"] = "X"
        clicked = False
        count += 1
        whowon()
    elif but["text"] == "" and clicked == False:
        but["text"] = "O"
        clicked = True
        count += 1
        whowon()
    else:
        messagebox.showerror(
            "Tic Tav Toe", "Hey! That box has already been selected\n Try another box ")


def play():
    global but1, but2, but3, but4, but5, but6, but7, but8, but9, clicked, count
    clicked = True
    count = 0
    but1 = Button(root, text="", font=("Monospace", 20),
                  height=3, width=6, bg="Silver", command=lambda: b_click(but1))
    but2 = Button(root, text="", font=("Monospace", 20),
                  height=3, width=6, bg="Silver", command=lambda: b_click(but2))
    but3 = Button(root, text="", font=("Monospace", 20),
                  height=3, width=6, bg="Silver", command=lambda: b_click(but3))

    but4 = Button(root, text="", font=("Monospace", 20),
                  height=3, width=6, bg="Silver", command=lambda: b_click(but4))
    but5 = Button(root, text="", font=("Monospace", 20),
                  height=3, width=6, bg="Silver", command=lambda: b_click(but5))
    but6 = Button(root, text="", font=("Monospace", 20),
                  height=3, width=6, bg="Silver", command=lambda: b_click(but6))

    but7 = Button(root, text="", font=("Monospace", 20),
                  height=3, width=6, bg="Silver", command=lambda: b_click(but7))
    but8 = Button(root, text="", font=("Monospace", 20),
                  height=3, width=6, bg="Silver", command=lambda: b_click(but8))
    but9 = Button(root, text="", font=("Monospace", 20),
                  height=3, width=6, bg="Silver", command=lambda: b_click(but9))

    but1.grid(row=0, column=0)
    but2.grid(row=0, column=1)
    but3.grid(row=0, column=2)

    but4.grid(row=1, column=0)
    but5.grid(row=1, column=1)
    but6.grid(row=1, column=2)

    but7.grid(row=2, column=0)
    but8.grid(row=2, column=1)
    but9.grid(row=2, column=2)


btn = Button(root, text="Restart", font=("Monospace", 20),
             height=1, width=6, bg="green", command=play)

btn.grid(row=3, column=1)
play()
root.mainloop()
