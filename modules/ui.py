import tkinter as tk

def spawn_screen():

    def reply():
        from tkinter.messagebox import showinfo
        showinfo(title='popup', message='button pressed')

    def print_it(event):
        print(var.get())

    window = tk.Tk()
    button = tk.Button(window, text='press', command=reply)
    button.pack()

    var = tk.StringVar()
    var.set('a')
    omenu = tk.OptionMenu(window, var, 'a','b','c', command=print_it)
    omenu.pack()

    window.mainloop()
