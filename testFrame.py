from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

root = Tk()
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()


# import tkinter as tk
#
#
# class Ivis(tk.Frame):
#     def __init__(self):
#         tk.Frame.__init__(self)
#         self.pack()
#         self.master.title("Demo 1")
#         self.button1 = tk.Button(self, text = "Button 1", width = 25,
#                                command = self.new_window)
#         self.button1.grid(row = 0, column = 1, columnspan = 2, sticky = tk.W+tk.E+tk.N+tk.S)
#
#     def new_window(self):
#         self.newWindow = Demo2()
#
#
# class Demo2(tk.Frame):
#     def __init__(self):
#         new = tk.Frame.__init__(self)
#         new = tk.Toplevel(self)
#         new.title("Demo 2")
#         new.button = tk.Button(text = "Button 2", width = 25,
#                                command = self.close_window)
#         new.button.pack()
#
#     def close_window(self):
#         self.destroy()
#
#
# def main():
#     Ivis().mainloop()
#
#
# if __name__ == '__main__':
#     main()