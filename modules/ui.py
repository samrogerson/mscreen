import tkinter as tk

#def spawn_screen():
    #def reply():
        #from tkinter.messagebox import showinfo
        #showinfo(title='popup', message='button pressed')

def print_it(event):
    print(event)
    #print(var.get())

def make_option_menus(screens):
    window = tk.Tk()
    #button = tk.Button(window, text='press', command=reply)
    #button.pack()

    vars = []
    omenus = []
    for screen_name, modes  in screens.items():
        vars.append(tk.StringVar())
        vars[-1].set(screen_name+"...")
        options = [ "{res} ({ref})".format(res=res,ref=ref) for res,ref in
                    zip(modes['resolutions'], modes['refresh_rates']) ]
        omenus.append(tk.OptionMenu(window, vars[-1],
                                    *options,
                                    command=print_it))
        omenus[-1].pack()

    window.mainloop()
