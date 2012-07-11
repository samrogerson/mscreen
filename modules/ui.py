#!/usr/bin/python

import tkinter as tk
from tkinter import Tk, RIGHT, LEFT, BOTH, RAISED, Frame, Button, ttk
from tkinter.ttk import Style

class XRUI(Tk):
    def __init__(self, screens):
        Tk.__init__(self)
        self.initUI(screens)


    def close(self):
        from _tkinter import TclError
        try:
            self.destroy()
        except TclError as e:
            print(e)


    def initUI(self, screens):
        self.geometry("+300+300")
        self.title("mscreen")

        xr_ui = Frame(self)
        xr_ui.pack(fill=BOTH,expand=1)
        self.add_option_menus(screens, xr_ui)

        sel_buttons = Frame(self)
        sel_buttons.pack(fill=BOTH, expand=1)
        self.add_buttons(sel_buttons)

        self.mainloop()

    def update_screens():
        print(var.get())

    def add_option_menus(self, screens, frame):
        vars = []
        omenus = []

        frame.rowconfigure(0, pad=3)
        frame.rowconfigure(1, pad=3)

        max_len = 0
        for screen_name, modes  in screens.items():
            vars.append(tk.StringVar())
            vars[-1].set(screen_name+"...")
            options = [ "{res} ({ref})".format(res=res,ref=ref) for res,ref in
                        zip(modes['resolutions'], modes['refresh_rates']) ]
            max_len = max(max_len, max( map(len, options)))
            omenus.append(tk.OptionMenu(frame, vars[-1], *options))

        for r,omenu in enumerate(omenus):
            omenu.config(width=max_len, anchor='w')
            omenu.grid(row=r, padx=5 )

    def add_buttons(self, frame):
        closeButton = Button(frame, text="Close", command=self.close)
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        okButton = Button(frame, text="OK", command=self.update_screens)
        okButton.pack(side=RIGHT)
