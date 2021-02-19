import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []

# save .txt file with list for .exe saved by user
if os.path.isfile('../save.txt'):
    with open('../save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

# adds applications selected by user
def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("executables", "*.exe"), ("all files", "*.*")))

    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(canvas, frame, text=app, bg="gray")
        label.pack()

#
def runApps():
    for app in apps:
        os.startfile(app)

# GUI color/sizing
canvas = tk.Canvas(root, height=700, width=600, bg="#b8d9f5")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheigh=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10,
                     pady=5, fg="white", bg="#42a4f5", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#42a4f5", command=runApps)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('../save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')