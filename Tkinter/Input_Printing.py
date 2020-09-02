from tkinter import *

root = Tk()


def returnEntry(arg=None):

    result = myEntry.get()
    result1 = myEntry1.get()
    result2 = myEntry2.get()
    resultLabel.config(text=result)
    resultLabel1.config(text=result1)
    resultLabel2.config(text=result2)
    myEntry.delete(0, END)
    myEntry1.delete(0, END)
    myEntry2.delete(0, END)


def correct(inp):
    if inp.isdigit():
        return True
    elif inp == "":
        return True
    else:
        return False


label = Label(text="USER NAME")
myEntry = Entry(root, width=20)
label1 = Label(text="Email")
myEntry1 = Entry(root, width=20)
label2 = Label(text="Phone Number")
myEntry2 = Entry(root, width=20)

reg = root.register(correct)
myEntry2.config(validate="key", validatecommand=(reg, '%P'))


myEntry.focus()
myEntry1.focus()
myEntry.bind(returnEntry)
myEntry1.bind(returnEntry)
myEntry2.bind(returnEntry)

label.pack()
myEntry.pack()
label1.pack()
myEntry1.pack()
label2.pack()
myEntry2.pack()


enterEntry = Button(root, text="Enter", command=returnEntry)
enterEntry.pack(fill=X)

resultLabel = Label(root, text="")
resultLabel.pack(fill=X)
resultLabel1 = Label(root, text="")
resultLabel1.pack(fill=X)
resultLabel2 = Label(root, text="")
resultLabel2.pack(fill=X)


root.geometry("+750+400")

root.mainloop()
