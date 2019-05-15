import tkinter as tk


def start_main_window(height=335, width=425):

    def open_button_press():
        pass

    def settings_button_press():
        pass

    root = tk.Tk()

    root.title("EDRM")
    root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='logo.gif'))

    canvas = tk.Canvas(root, height=height, width=width)
    canvas.pack()

    frame = tk.Frame(root, bd=5)
    frame.place(relwidth=1, relheight=1)

    open_button = tk.Button(frame, text="Open Route", command=open_button_press)
    open_button.place(relx=1/20, rely=1/20, relwidth=1/5, relheight=1/10)

    settings_button = tk.Button(frame, text="Settings", command=settings_button_press)
    settings_button.place(relx=0.7, rely=1/20, relwidth=1/4, relheight=1/10)

    root.mainloop()


start_main_window()
