#!/usr/bin/python

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


def make_option_menus(screens):
    window = tk.Tk()
    window.geometry("300x200+300+300")
    app = xrUI(window)

    vars = []
    omenus = []
    for screen_name, modes  in screens.items():
        vars.append(tk.StringVar())
        vars[-1].set(screen_name+"...")
        options = [ "{res} ({ref})".format(res=res,ref=ref) for res,ref in
                    zip(modes['resolutions'], modes['refresh_rates']) ]
        omenus.append(tk.OptionMenu(window, vars[-1],
                                    *options))
                                    #command=print_it))
        omenus[-1].pack()

    window.mainloop()
