import tkinter as tk
from tkinter import filedialog
from config.config import *


def start_main_window(height=335, width=425):

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
    root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='logo.gif'))

    canvas = tk.Canvas(root, height=height, width=width)
    canvas.pack()

    frame = tk.Frame(root, bd=5)
    frame.place(relwidth=1, relheight=1)

    open_button = tk.Button(frame, text="Open Route", command=open_button_press)
    open_button.place(relx=1-1/5, rely=0, relwidth=1/5, relheight=1/10)

    settings_button = tk.Button(frame, text="Settings", command=settings_button_press)
    settings_button.place(relx=1-1/5, rely=1/10+0.01, relwidth=1/5, relheight=1/10)

    info_label = tk.Label(frame, text="Commander Name:\nCurrent System:\nNext System:", justify="left")
    info_label.place(relx=0.03, rely=0.03, relwidth=1/4, relheight=1/7)

    info_label_2 = tk.Label(frame, text="Gobi007\nSagittarius A*\nSol", justify="left")
    info_label_2.place(relx=0.35, rely=0.03, relwidth=1/3.5, relheight=1/7)

    root.mainloop()


start_main_window()
