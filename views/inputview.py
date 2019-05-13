import tkinter as tk

HEIGHT = 170
WIDTH = 250

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bd=5)
frame.place(relwidth=1, relheight=1)

label = tk.Label(frame, text="Name:")
label.pack()

root.mainloop()
