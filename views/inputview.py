import tkinter as tk
from tkinter import messagebox
from utils.edsm import is_known
from config.config import *
import threading


def start_input_window(height=170, width=250):

    def ok_button_press():
        commander_name = name_entry.get()
        if not is_known(commander_name):
            messagebox.showerror("Error", "Commander is not known to EDSM")
        else:
            set_commander_name(commander_name)
            root.destroy()
            from views.mainview import start_main_window
            from main.EDRouteManager import loop_refresh
            threading.Thread(target=start_main_window).start()
            threading.Thread(target=loop_refresh).start()
            refresh_current_system()
            from views.mainview import set_info_content
            set_info_content(get_commander_name(), get_current_system(), "")

    root = tk.Tk()

    root.title("EDRM")
    root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='../views/logo.gif'))
    root.iconbitmap(default='../views/logo.gif')

    canvas = tk.Canvas(root, height=height, width=width)
    canvas.pack()

    frame = tk.Frame(root, bd=5)
    frame.place(relwidth=1, relheight=1)

    label = tk.Label(frame, text="Name:")
    label.place(relwidth=0.25, relheight=0.18, relx=0, rely=0)

    name_entry = tk.Entry(frame)
    name_entry.place(relwidth=0.45, relheight=0.18, relx=0.26, rely=0)

    ok_button = tk.Button(frame, text="Ok", command=ok_button_press)
    ok_button.place(relwidth=0.2, relheight=0.18, relx=0.72, rely=0)

    root.mainloop()


# start_input_window()
