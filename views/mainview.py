import tkinter as tk
from tkinter import font as tkfont


class MainView(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Cambria', size=18, weight="bold", slant="italic")

        # Navigation frame
        navigation_frame = tk.Frame(self, bg="#000000", height=600, width=300)
        navigation_frame.pack(side=tk.LEFT)

        # Current Route button for navigation
        current_route_button = tk.Button(navigation_frame, bd=0, bg="#000000", fg="#efefef", text="Current Route")


        # Container
        container = tk.Frame(self, width=800)
        container.pack(side="top", fill="both", expand=True)

        self.mainloop()


mv = MainView()
