from windows.WindowsOption import *
from windows.GridCreate import *
from tkinter import *

class GridMenu:
    def __init__(self, root):
        self.root = root
        self.root.geometry('400x400')
        clear_window(root)
        self.canvas = Canvas(self.root, width=self.root.winfo_width(), height=self.root.winfo_height())
        self.canvas.pack()
        self.algorithm = None
        self.grid = None
        self.radio_btn_option = IntVar()
        self.init_window()

    def init_window(self):
        self.upload_grid_btn()
        self.create_grid_btn()
        self.algorithm_choose()
        self.start_button()

    def create_grid_btn(self):
        create_btn = Button(self.canvas, text="Create grid", width=10, background="black", fg="white", font="Roboto", command=self.create)
        create_btn.place(x=220, y=50)

    def upload_grid_btn(self):
        upload_btn = Button(self.canvas, text="Upload grid", width=10, background="black", fg="white", font="Roboto", command=self.upload)
        upload_btn.place(x=100, y=50)

    def set_algorithm(self):
        option = self.radio_btn_option.get()
        if option == 1:
            print("BFS")
        elif option == 2:
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
        print("Start")

    def upload(self):
        print("Upload")

    def create(self):
        print("Create")
        GridCreate(self.root)


