from tkinter import *
import tkinter as tk


root = tk.Tk()
root.geometry("340x400")
root.title("Calculator Gui")

val = ""
A = 0
operator = ""


def btn_1_isclicked():
    global val
    val = val + "1"
    data.set(val)


def btn_2_isclicked():
    global val
    val = val + "2"
    data.set(val)


def btn_3_isclicked():
    global val
    val = val + "3"
    data.set(val)


def btn_4_isclicked():
    global val
    val = val + "4"
    data.set(val)


def btn_5_isclicked():
    global val
    val = val + "5"
    data.set(val)


def btn_6_isclicked():
    global val
    val = val + "6"
    data.set(val)


def btn_7_isclicked():
    global val
    val = val + "7"
    data.set(val)


def btn_8_isclicked():
    global val
    val = val + "8"
    data.set(val)


def btn_9_isclicked():
    global val
    val = val + "9"
    data.set(val)


def btn_0_isclicked():
    global val
    val = val + "0"
    data.set(val)


def btn_plus_clicked():
    global A
    global operator, val
    A = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)


def btn_minus_clicked():
    global A
    global operator, val
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)


def btn_mult_clicked():
    global A
    global operator, val
    A = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)


def btn_div_clicked():
    global A
    global operator, val
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)


def btn_c_pressed():
    global A, operator, val
    val = ""
    A = 0
    operator = ""
    data.set(val)


def result():
    global A, operator, val
    val2 = val
    if operator == "+":
        x = int((val2.split("+")[1]))
        C = A + x
        val = str(C)
        data.set(val)
    if operator == "-":
        x = int((val2.split("-")[1]))
        C = A - x
        val = str(C)
        data.set(val)
    if operator == "*":
        x = int((val2.split("*")[1]))
        C = A * x
        val = str(C)
        data.set(val)
    if operator == "/":
        x = int((val2.split("/")[1]))
        if x == 0:
            messagebox.showerror("Error", "Division By 0 Not Supported")
            A = ""
            val = ""
            data.set(val)
        else:
            C = int(A / x)
            data.set(C)


data = StringVar()
lbl = Label(
    root,
    text="Label",
    anchor=SE,
    font=("Monospace", 20),
    textvariable=data,
    background="#000000",
    fg="#ffff00",
)
lbl.pack(expand=True, fill="both")


btnrow1 = Frame(root)
btnrow1.pack(expand=True, fill="both")

btnrow2 = Frame(root)
btnrow2.pack(expand=True, fill="both")

btnrow3 = Frame(root)
btnrow3.pack(expand=True, fill="both")

btnrow4 = Frame(root)
btnrow4.pack(expand=True, fill="both")


btn1 = Button(
    btnrow1,
    text="1",
    font=("Monospace", 20),
    relief=GROOVE,
    border=0,
    command=btn_1_isclicked,
)
btn1.pack(side=LEFT, expand=True, fill="both",)

btn2 = Button(
    btnrow1,
    text="2",
    font=("Monospace", 20),
    relief=GROOVE,
    border=0,
    command=btn_2_isclicked,
)
btn2.pack(side=LEFT, expand=True, fill="both",)

btn3 = Button(
    btnrow1,
    text="3",
    font=("Monospace", 20),
    relief=GROOVE,
    border=0,
    command=btn_3_isclicked,
)
btn3.pack(side=LEFT, expand=True, fill="both",)

btnplus = Button(
    btnrow1,
    text="+",
    font=("Monospace", 20),
    relief=GROOVE,
    border=0,
    command=btn_plus_clicked,
)
btnplus.pack(side=LEFT, expand=True, fill="both",)


btn4 = Button(
    btnrow2,
    text="4",
    font=("Monospace", 20),
    relief=GROOVE,
    border=0,
    command=btn_4_isclicked,
)
btn4.pack(side=LEFT, expand=True, fill="both",)

btn5 = Button(
    btnrow2,
    text="5",
    font=("Monospace", 20),
    relief=GROOVE,
    border=0,
    command=btn_5_isclicked,
)
btn5.pack(side=LEFT, expand=True, fill="both",)

btn6 = Button(
    btnrow2,
    text="6",
    font=("Monospace", 20),
    relief=GROOVE,
    border=0,
    command=btn_6_isclicked,
)
btn6.pack(side=LEFT, expand=True, fill="both",)

btnminus = Button(
    btnrow2,
    text="-",
    font=("Monospace", 20),
    relief=GROOVE,
    border=0,
    command=btn_minus_clicked,
)
btnminus.pack(side=LEFT, expand=True, fill="both",)


btn7 = Button(
    btnrow3,
    text="7",
    font=("Monospace", 20),
    relief=GROOVE,
    border=0,
    command=btn_7_isclicked,
)
btn7.pack(side=LEFT, expand=True, fill="both",)

btn8 = Button(
    btnrow3,
    text="8",
    font=("Monospace", 20),
    relief=GROOVE,
    border=0,
    command=btn_8_isclicked,
)
btn8.pack(side=LEFT, expand=True, fill="both",)

btn9 = Button(
    btnrow3,
    text="9",
    font=("Monospace", 20),
    relief=GROOVE,
    border=0,
    command=btn_9_isclicked,
)
btn9.pack(side=LEFT, expand=True, fill="both",)

btnmult = Button(
    btnrow3,
    text="*",
    font=("Monospace", 20),
    relief=GROOVE,
    border=0,
    command=btn_mult_clicked,
)
btnmult.pack(side=LEFT, expand=True, fill="both",)


btnc = Button(
    btnrow4,
    text="C",
    font=("Monospace", 20),
    relief=GROOVE,
    border=0,
    command=btn_c_pressed,
)
btnc.pack(side=LEFT, expand=True, fill="both",)

btn0 = Button(
    btnrow4,
    text="0",
    font=("Monospace", 20),
    relief=GROOVE,
    border=0,
    command=btn_0_isclicked,
)
btn0.pack(side=LEFT, expand=True, fill="both",)

btnequal = Button(
    btnrow4,
    text="=",
    font=("Monospace", 20),
    relief=GROOVE,
    border=0,
    command=result,
)
btnequal.pack(side=LEFT, expand=True, fill="both",)

btndiv = Button(
    btnrow4,
    text="/",
    font=("Monospace", 20),
    relief=GROOVE,
    border=0,
    command=btn_div_clicked,
)
btndiv.pack(side=LEFT, expand=True, fill="both",)

root.mainloop()
