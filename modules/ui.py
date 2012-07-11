#!/usr/bin/python

import tkinter as tk
from tkinter import Tk, RIGHT, BOTH, RAISED, Frame, Button, ttk
from tkinter.ttk import Style

print(dir(tk))



def add_option_menus(screens, frame):
    vars = []
    omenus = []
    for screen_name, modes  in screens.items():
        vars.append(tk.StringVar())
        vars[-1].set(screen_name+"...")
        options = [ "{res} ({ref})".format(res=res,ref=ref) for res,ref in
                    zip(modes['resolutions'], modes['refresh_rates']) ]
        omenus.append(tk.OptionMenu(frame, vars[-1], *options))
        omenus[-1].pack()

def gen_ui(screens):
    window = Tk()
# size + offset
    window.geometry("300x200+300+300")
    window.title("mscreen")


    xr_ui = Frame(window)
    xr_ui.pack(fill=BOTH,expand=1)
    add_option_menus(screens, xr_ui)

    sel_buttons = Frame(window)
    frame = Frame(sel_buttons, relief=RAISED, borderwidth=1)
    frame.pack(fill=BOTH, expand=1)
    sel_buttons.pack(fill=BOTH, expand=1)
    closeButton = Button(sel_buttons, text="Close")
    closeButton.pack(side=RIGHT, padx=5, pady=5)
    okButton = Button(sel_buttons, text="OK")
    okButton.pack(side=RIGHT)

    window.mainloop()
