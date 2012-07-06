#!/usr/bin/python

import tkinter as tk
from tkinter import Tk, RIGHT, BOTH, RAISED, Frame, Button, ttk
from tkinter.ttk import Style

class xrUI(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        self.initUI()

    def initUI(self):

        self.parent.title("Buttons")
        self.style = Style()
        self.style.theme_use("default")

        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=1)

        self.pack(fill=BOTH, expand=1)

        closeButton = Button(self, text="Close")
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        okButton = Button(self, text="OK")
        okButton.pack(side=RIGHT)

def add_option_menus(screens, window):
    vars = []
    omenus = []
    for screen_name, modes  in screens.items():
        vars.append(tk.StringVar())
        vars[-1].set(screen_name+"...")
        options = [ "{res} ({ref})".format(res=res,ref=ref) for res,ref in
                    zip(modes['resolutions'], modes['refresh_rates']) ]
        omenus.append(tk.OptionMenu(window, vars[-1],
                                    *options))
        omenus[-1].pack()

def gen_ui(screens):
    window = Tk()
    window.geometry("300x200+300+300")
    add_option_menus(screens, window)

    app = xrUI(window)
    window.mainloop()
