import tkinter as tk
from tkinter import filedialog
from config.config import *


def set_info_content(commander_name, current_system_name, next_system_name):
    info_label_2.config(text=(commander_name + "\n" + current_system_name + "\n" + next_system_name))


def start_main_window(height=100, width=425):
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

    root = tk.Tk()

    root.title("EDRM")
    root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='../views/logo.gif'))
    root.iconbitmap(default='../views/logo.gif')

    canvas = tk.Canvas(root, height=height, width=width)
    canvas.pack()

    frame = tk.Frame(root, bd=5)
    frame.place(relwidth=1, relheight=1)

    open_button = tk.Button(frame, text="Open Route", command=open_button_press)
    open_button.place(relx=1-1/5, rely=0, relwidth=1/5, relheight=1/3)

    settings_button = tk.Button(frame, text="Settings", command=settings_button_press)
    settings_button.place(relx=1-1/5, rely=0.3+0.05, relwidth=1/5, relheight=1/3)

    info_label = tk.Label(frame, text="Commander Name:\nCurrent System:\nNext System:", justify="left")
    info_label.place(relx=0.03, rely=0.05, relwidth=1/4, relheight=0.6)

    info_label_2 = tk.Label(frame, text="\n \n \n", justify="left")
    info_label_2.place(relx=0.35, rely=0.05, relwidth=1/3, relheight=0.6)

    root.mainloop()
