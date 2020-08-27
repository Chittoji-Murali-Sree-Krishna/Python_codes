import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []


def addApp():
    for widget in frame.winfo_children():
        widget.destroy()
    filename = filedialog.askopenfilename(initialdir="~", title="Select Files",
                                          filetypes=(("Debian", ".deb"), ("Executables",".exe"), ("RedHat Package Manager",".rpm"), ("python", ".py"), ("Html", ".html"), ("Zipped", ".zip"), ("all files", "*.*")))

    apps.append(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()


def runApps():
    for app in apps:
        os.startfile(app)


canvas = tk.Canvas(root, height=700, width=700, bg='#000000')
canvas.pack()

frame = tk.Frame(root, bg='lightgreen')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10,
                     pady=5, fg='white', bg='coral', command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10,
                    pady=5, fg='white', bg='coral')
runApps.pack()

root.mainloop()
