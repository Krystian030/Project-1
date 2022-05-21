from tkinter import *
from pathVisualisation.GridBoard import *
from tkinter import messagebox
from windows.WindowsOption import *


class GridCreate:
    def __init__(self, root):
        self.root = root
        clear_window(root)
        self.entry_width = None
        self.entry_height = None
        self.enter_dimension_grid()
        self.create_grid_button()

    def enter_dimension_grid(self):
        # set_width
        label_width = Label(self.root, text='Width:', width=10, font=("Roboto", 12, 'bold'))
        label_width.place(x=10, y=50)

        self.entry_width = Entry(self.root, width=10)
        self.entry_width.place(x=100, y=53)

        # set_height
        label_height = Label(self.root, text='Height:', width=10, font=("Roboto", 12, 'bold'))
        label_height.place(x=10, y=100)

        self.entry_height = Entry(self.root, width=10)
        self.entry_height.place(x=100, y=103)

    def create_grid_button(self):
        create_grid_button = Button(self.root, text="Create grid", width=20, background="black", fg="white", command=self.create_grid, font="Roboto")
        create_grid_button.place(x=100, y=300)

    def check_data(self):
        if len(self.entry_width.get()) == 0:
            return False
        if len(self.entry_height.get()) == 0:
            return False
        return True

    def create_grid(self):
        print('create grid')
        if self.check_data():
            try:
                width = int(self.entry_width.get())
                height = int(self.entry_height.get())
            except ValueError:
                messagebox.showerror("Error", "Invalid data")
            else:
                clear_window(self.root)
                GridBoard(self.root, width, height)
        else:
            messagebox.showerror("Error", "Invalid data")
