import tkinter # Tkinter -> tkinter in Python 3

class FancyListbox(tkinter.Listbox):

    def __init__(self, parent, *args, **kwargs):
        tkinter.Listbox.__init__(self, parent, *args, **kwargs)

        self.popup_menu = tkinter.Menu(self, tearoff=0)
        self.popup_menu.add_command(label="Delete",
                                    command=self.delete_selected)
        self.popup_menu.add_command(label="Select All",
                                    command=self.select_all)

        self.bind("<Button-3>", self.popup) # Button-2 on Aqua

    def popup(self, event):
        try:
            self.popup_menu.tk_popup(event.x_root, event.y_root, 0)
        finally:
            self.popup_menu.grab_release()

    def delete_selected(self):
        for i in self.curselection()[::-1]:
            self.delete(i)

    def select_all(self):
        self.selection_set(0, 'end')


root = tkinter.Tk()
flb = FancyListbox(root, selectmode='multiple')
for n in range(10):
    flb.insert('end', n)
flb.pack()
root.mainloop()

















# import tkinter
#
# from matplotlib.backends.backend_tkagg import (
#     FigureCanvasTkAgg, NavigationToolbar2Tk)
#
# # Implement the default Matplotlib key bindings.
# from matplotlib.backend_bases import key_press_handler
# from matplotlib.figure import Figure
# import matplotlib.pyplot as mpl
#
# import numpy as np
#
#
# root = tkinter.Tk()
# root.wm_title("Embedding in Tk")
#
# # fig = Figure(figsize=(5, 4), dpi=100)
# # t = np.arange(0, 3, .01)
# # fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))
#
# fig, ax = mpl.subplots(figsize=(5, 4), dpi=100)
# t = np.arange(0, 3, .01)
# ax.plot(t, 2 * np.sin(2 * np.pi * t))
#
# canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
# canvas.draw()
#
# toolbar = NavigationToolbar2Tk(canvas, root)
# toolbar.update()
#
#
# def on_key_press(event):
#     print("you pressed {}".format(event.key))
#     key_press_handler(event, canvas, toolbar)
#
#
# canvas.mpl_connect("key_press_event", on_key_press)
# # canvas.mpl_connect("key_press_event", key_press_handler)
#
# button = tkinter.Button(master=root, text="Quit", command=root.quit)
#
# # Packing order is important. Widgets are processed sequentially and if there
# # is no space left, because the window is too small, they are not displayed.
# # The canvas is rather flexible in its size, so we pack it last which makes
# # sure the UI controls are displayed as long as possible.
# button.pack(side=tkinter.BOTTOM)
# canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
#
# tkinter.mainloop()