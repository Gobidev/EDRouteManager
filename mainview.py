import tkinter as tk
from tkinter import filedialog
from config.config import *
import threading
from tkinter import ttk
from tkinter import messagebox
from utils.edsm import is_known


def set_info_content(commander_name, current_system_name, next_system_name):
    info_label_2.config(text=(commander_name + "\n" + current_system_name + "\n" + next_system_name))


def start_main_window(height=160, width=450):
    global info_label_2

    def open_button_press():
        root.filename = filedialog.askopenfilename(
            initialdir="/", title="Select file", filetypes=(("csv files", "*.csv"), ("all files", "*.*"))
        )
        set_file_path(root.filename)

    def ok_button_press():
        commander_name = name_entry.get()
        if not is_known(commander_name):
            messagebox.showerror("Error", "Commander is not known to EDSM")
        else:
            set_commander_name(commander_name)
            info_label.config(state="normal")
            info_label_2.config(state="normal")
            open_button.config(state="normal")
            from main.EDRouteManager import loop_refresh
            threading.Thread(target=loop_refresh).start()

    root = tk.Tk()

    root.title("EDRouteManager")
    root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='../views/logo.gif'))
    root.iconbitmap(default='../views/logo.gif')
    root.resizable(False, False)

    canvas = tk.Canvas(root, height=height, width=width)
    canvas.pack()

    frame = tk.Frame(root, bd=15)
    frame.place(relwidth=1, relheight=1)

    open_button = ttk.Button(frame, text="Open Route", command=open_button_press, state="disabled")
    open_button.grid(row=0, column=2, rowspan=3, padx=10, ipadx=20, sticky="E")

    info_label = ttk.Label(frame, text="Commander Name:\nCurrent System:\nNext System:", state="disabled")
    info_label.grid(row=0, column=0, padx=5, rowspan=3, sticky="W")

    info_label_2 = ttk.Label(frame, state="disabled")
    info_label_2.grid(row=0, column=1, padx=10, rowspan=3, sticky="W")

    # inputs
    name_label = ttk.Label(frame, text="Name:")
    name_label.grid(row=3, column=0, padx=5, pady=5, sticky="W")

    name_entry = ttk.Entry(frame)
    name_entry.grid(row=3, column=1, columnspan=2, padx=5, pady=5, ipadx=80)

    api_label = ttk.Label(frame, text="API-key (coming soon):", state="disabled")
    api_label.grid(row=4, column=0, padx=5, pady=5, sticky="W")

    api_entry = ttk.Entry(frame, state="disabled")
    api_entry.grid(row=4, column=1, columnspan=2, padx=5, pady=5, ipadx=80)

    ok_button = ttk.Button(frame, text="Ok", command=ok_button_press)
    ok_button.grid(row=5, columnspan=3, ipadx=20)

    if get_commander_name() == "key not found in config":
        name_entry.focus()
    else:
        info_label.config(state="normal")
        info_label_2.config(state="normal")
        open_button.config(state="normal")
        open_button.focus()

    root.mainloop()
