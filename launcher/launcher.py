import tkinter as tk
from tkinter import ttk
import os
import subprocess
from tkinter import filedialog

root = tk.Tk()

listbox = ttk.Treeview(root, columns=("Name", "Type"))
listbox.heading("#0", text="")
listbox.heading("#1", text="Name")
listbox.heading("#2", text="Type")


def browse_dir():
    # open a file browser dialog and get the selected directory
    directory = filedialog.askdirectory()

    # clear the listbox
    listbox.delete(*listbox.get_children())

    # use the os module to get a list of all files in the selected directory
    files = os.listdir(directory)

    # loop through the list of files
    for file in files:
        # check if the file is an application (ends with ".exe" or ".lnk")
        if file.endswith(".exe") or file.endswith(".lnk"):
            # add the file to the listbox
            listbox.insert("", "end", text="", values=(
                file, file.split(".")[1]))


def launch_app():
    # get the selected application from the list
    app = listbox.item(listbox.selection())["values"][0]

    # use the os module to launch the selected application
    subprocess.Popen(app)


browse_button = tk.Button(root, text="Browse", command=browse_dir)
launch_button = tk.Button(root, text="Launch", command=launch_app)

listbox.pack(side="left", fill="both", expand=True)
browse_button.pack(side="top")
launch_button.pack(side="top")

root.mainloop()
