import tkinter as tk

HEIGHT = 170
WIDTH = 250


def ok_button_press():
    pass


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
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