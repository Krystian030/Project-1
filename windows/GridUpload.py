from tkinter import *
from pathVisualisation.GridBoard import *
from tkinter import messagebox
from windows.WindowsOption import *
from windows.GridConfig import *
import os.path
path = 'resources/files/'


class GridUpload:
    def __init__(self, root, parent):
        self.root = root
        self.parent = parent
        clear_window(root)
        self.entry_file_name = None
        self.enter_file_name()
        self.upload_grid_button()
        self.back_button()

    def enter_file_name(self):
        label_file_name = Label(self.root, text='File name:', width=10, font=("Roboto", 12, 'bold'))
        label_file_name.place(x=10, y=50)

        self.entry_file_name = Entry(self.root, width=10)
        self.entry_file_name.place(x=110, y=53, width=100)

    def upload_grid_button(self):
        create_grid_button = Button(self.root, text="Upload", width=20, background="black", fg="white", command=self.upload_grid, font="Roboto")
        create_grid_button.place(x=100, y=300)

    def back_button(self):
        back_grid_button = Button(self.root, text="Back to menu", width=20, background="black", fg="white", command=self.parent.init_window, font="Roboto")
        back_grid_button.place(x=100, y=350)

    def check_data(self):
        file_name = self.entry_file_name.get()
        if len(file_name) == 0:
            return False
        file_name = path + file_name
        if not os.path.exists(file_name):
            return False
        return True

    def upload_grid(self):
        if self.check_data():
            file_name = path + self.entry_file_name.get()
            in_file = open(file_name, 'rb')
            grid = pickle.load(in_file, encoding='bytes')
            grid.root = self.root
            grid.grid_config_initialize(self.parent)
            # grid.grid_config.init_window_create_grid()
            # grid.grid_config.update_grid()
            self.parent.grid = grid
            self.parent.grid_name = self.entry_file_name.get()
            self.parent.init_window()
        else:
            messagebox.showerror("Error", "File not found")
