from windows.WindowsOption import *
from windows.GridCreate import *
from windows.GridUpload import *
from tkinter import *
from tkinter import messagebox
from algorithms.Bfs import *

class GridMenu:
    def __init__(self, root):
        self.root = root
        self.canvas = None
        self.algorithm = None
        self.grid = None
        self.grid_name = None
        self.radio_btn_option = IntVar()
        self.init_window()

    def init_window(self):
        clear_window(self.root)
        self.root.geometry('400x400')
        self.canvas = Canvas(self.root, width=self.root.winfo_width(), height=self.root.winfo_height())
        self.canvas.pack()
        self.upload_grid_btn()
        if self.grid is None:
            self.create_grid_btn()
        else:
            self.grid_label_name()
            self.change_grid_btn()
        self.algorithm_choose()
        self.start_button()

    def grid_label_name(self):
        label_width = Label(self.root, text=f'Grid name: {self.grid_name}', width=10, font=("Roboto", 12, 'bold'))
        label_width.place(x=130, y=100)

    def create_grid_btn(self):
        create_btn = Button(self.canvas, text="Create grid", width=10, background="black", fg="white", font="Roboto", command=self.create)
        create_btn.place(x=220, y=50)

    def change_grid_btn(self):
        create_btn = Button(self.canvas, text="Change grid", width=10, background="black", fg="white", font="Roboto", command=self.change)
        create_btn.place(x=220, y=50)

    def upload_grid_btn(self):
        upload_btn = Button(self.canvas, text="Upload grid", width=10, background="black", fg="white", font="Roboto", command=self.upload)
        upload_btn.place(x=100, y=50)

    def set_algorithm(self):
        option = self.radio_btn_option.get()
        if option == 1:
            print("BFS")
            self.algorithm = BfsGrid(self.grid)
        elif option == 2:
            self.algorithm = "XDD"
            print("A*")

    def algorithm_choose(self):
        label_choose_algorithm = Label(self.canvas, text='Choose algorithm: ', width=20, font=("Roboto", 16, 'bold'))
        label_choose_algorithm.place(x=60, y=120)
        r1 = Radiobutton(self.canvas, text="BFS", variable=self.radio_btn_option, value=1, width=20, command=self.set_algorithm,  font="Roboto")
        r1.place(x=75, y=170)

        r2 = Radiobutton(self.canvas, text="A*", variable=self.radio_btn_option, value=2, width=20, command=self.set_algorithm, font="Roboto")
        r2.place(x=75, y=220)

    def start_button(self):
        start_button = Button(self.canvas, text="Start", width=20, background="black", fg="white", command=self.start, font="Roboto")
        start_button.place(x=100, y=280)

    def start(self):
        print(self.algorithm)
        if self.grid is not None and self.algorithm is not None:
            print("STAAAAAAAART")
            self.grid.root = self.root
            self.grid.algorithm = self.algorithm
            self.grid.algorithm_visualisation()
        else:
            messagebox.showerror("Error", "Set algorithm and grid")

    def upload(self):
        GridUpload(self.root, self)

    def create(self):
        GridCreate(self.root, self)

    def change(self):
        self.grid.root = self.root
        self.grid.grid_config_initialize(self)
        clear_window(self.root)
        self.grid.grid_config.init_window_create_grid()
        self.grid.grid_config.entry_file_name.set(self.grid_name)
        self.grid.grid_config.update_grid()