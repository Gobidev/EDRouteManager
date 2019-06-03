import tkinter as tk
from tkinter import messagebox
from utils.edsm import is_known
from config.config import *
from tkinter import ttk


def start_input_window(height=70, width=250):

    def ok_button_press():
        commander_name = name_entry.get()
        if not is_known(commander_name):
            messagebox.showerror("Error", "Commander is not known to EDSM")
        else:
            set_commander_name(commander_name)
            root.destroy()

    root = tk.Tk()

    root.title("EDRouteManager")
    root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='../views/logo.gif'))
    root.iconbitmap(default='../views/logo.gif')
    root.resizable(False, False)

    canvas = tk.Canvas(root, height=height, width=width)
    canvas.pack()

    frame = tk.Frame(root, bd=5)
    frame.place(relwidth=1, relheight=1)

    name_label = ttk.Label(frame, text="Name:")
    name_label.grid(padx=10, sticky="W")

    # api_label = tk.Label(frame, text="API-key (optional):")
    # api_label.place(relwidth=0.4, relheight=0.18, relx=0, rely=0.19)

    name_entry = ttk.Entry(frame)
    name_entry.grid(row=0, column=1, padx=10, ipadx=20)

    ok_button = ttk.Button(frame, text="Ok", command=ok_button_press)
    ok_button.grid(row=1, column=1, pady=10, ipadx=20)

    root.mainloop()
