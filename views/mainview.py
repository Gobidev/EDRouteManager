import tkinter as tk
from tkinter import filedialog
from config.config import *
import threading
from tkinter import ttk


def set_info_content(commander_name, current_system_name, next_system_name):
    info_label_2.config(text=(commander_name + "\n" + current_system_name + "\n" + next_system_name))


def start_main_window(height=80, width=425):
    global info_label_2

    def open_button_press():
        root.filename = filedialog.askopenfilename(
            initialdir="/", title="Select file", filetypes=(("csv files", "*.csv"), ("all files", "*.*"))
        )
        set_file_path(root.filename)

    def settings_button_press():
        root.destroy()
        from views.inputview import start_input_window
        start_input_window()
        threading.Thread(target=start_main_window).start()
        refresh_current_system()
        set_info_content(get_commander_name(), get_current_system(), "")
        from main.EDRouteManager import loop_refresh
        threading.Thread(target=loop_refresh).start()

    root = tk.Tk()

    root.title("EDRouteManager")
    root.tk.call('wm', 'iconphoto', root.w, tk.PhotoImage(file='../views/logo.gif'))
    root.iconbitmap(default='../views/logo.gif')
    root.resizable(False, False)

    canvas = tk.Canvas(root, height=height, width=width)
    canvas.pack()

    frame = tk.Frame(root, bd=15)
    frame.place(relwidth=1, relheight=1)

    open_button = ttk.Button(frame, text="Open Route", command=open_button_press)
    open_button.grid(row=0, column=2, padx=10, ipadx=20, sticky="E")

    settings_button = ttk.Button(frame, text="Settings", command=settings_button_press)
    settings_button.grid(row=1, column=2, padx=10, ipadx=20, sticky="E")

    info_label = ttk.Label(frame, text="Commander Name:\nCurrent System:\nNext System:", justify="left")
    info_label.grid(row=0, column=0, padx=5, rowspan=3, sticky="W")

    info_label_2 = ttk.Label(frame, text="\n \n \n", justify="left")
    info_label_2.grid(row=0, column=1, padx=10, rowspan=3, sticky="W")

    root.mainloop()
