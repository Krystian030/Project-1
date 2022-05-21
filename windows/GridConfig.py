from tkinter import *
from pathVisualisation.Node import *
from tkinter import messagebox
from pathVisualisation.GridVisualisation import *
import sys
import pickle
from datetime import datetime

NOTHING = -1
CLEAR = 0
START = 1
END = 2
DRAW_OBSTACLE = 3
DRAW_RIVER = 4
DRAW_GROUND = 5
OPTIONS = ['None', 'obstacle', 'river [cost = 5]', 'ground [cost = 3]']
path = 'resources/files/'

class GridConfig:
    def __init__(self, root, grid, width, height, parent):
        self.parent = parent
        self.root = root
        self.grid = grid
        self.width = width
        self.height = height
        self.window_height = self.height
        self.window_width = self.width
        self.canvas = None
        self.entry_file_name = StringVar()
        self.mode = None
        self.can_draw = False
        self.radio_btn_option = IntVar()
        self.list_option = StringVar()
        # self.init_window_create_grid()

    def init_grid(self):
        if self.width < 200:
            self.window_width = 200
        self.window_width += 300
        if self.height < 400:
            self.window_height = 400
        self.root.geometry(f'{self.window_width}x{self.window_height}')
        self.canvas = Canvas(self.root, height=self.grid.height, width=self.grid.width)
        self.canvas.place(x=0, y=(self.window_height - self.height)//2)
        self.display_grid_board()

    def init_window_create_grid(self):
        # if self.root.winfo_children() is not None:
        #     clear_window(self.root)
        # if self.width < 200:
        #     self.window_width = 200
        # self.window_width += 300
        # if self.height < 400:
        #     self.window_height = 400
        # self.root.geometry(f'{self.window_width}x{self.window_height}')
        # self.canvas = Canvas(self.root, height=self.grid.height, width=self.grid.width)
        # self.canvas.place(x=0, y=(self.window_height - self.height)//2)
        # self.display_grid_board()
        self.init_grid()
        self.create_button()
        self.back_button()
        self.create_save_button()
        self.enter_file_name()

    def set_mode(self, *args):
        if self.list_option.get() != 'None':
            list_opt = self.list_option.get()
            if list_opt == OPTIONS[1]:
                self.mode = DRAW_OBSTACLE
            elif list_opt == OPTIONS[2]:
                self.mode = DRAW_RIVER
            elif list_opt == OPTIONS[3]:
                self.mode = DRAW_GROUND
            if self.radio_btn_option.get() is not None:
                self.radio_btn_option.set(NOTHING)
        elif self.list_option.get() == 'None':
            if self.radio_btn_option.get() is not None:
                self.mode = self.radio_btn_option.get()

        print(self.mode)

    def create_button(self):
        r0 = Radiobutton(self.root, text="Clear", variable=self.radio_btn_option, value=CLEAR,
                         command=self.set_mode, width=20, font="Roboto")
        r0.place(x=self.width + 20, y=0)

        r1 = Radiobutton(self.root, text="Mark start", variable=self.radio_btn_option, value=START,
                         command=self.set_mode, width=20, font="Roboto")
        r1.place(x=self.width+20, y=30)

        r2 = Radiobutton(self.root, text="Mark end", variable=self.radio_btn_option, value=END,
                         command=self.set_mode, width=20, font="Roboto")
        r2.place(x=self.width+20, y=60)

        self.list_option.set(OPTIONS[0])

        type_label = Label(self.root, text='Choose node type:', width=20, font=("Roboto", 12, 'bold'))
        type_label.place(x=self.width + 30, y=90)

        draw_options = OptionMenu(self.root, self.list_option, *OPTIONS, command=self.set_mode)
        draw_options.place(x=self.width+100, y=120)

    def create_save_button(self):
        save_button = Button(self.root, text="Save", width=20, background="black", fg="white", command=self.save_grid_to_file, font="Roboto")
        save_button.place(x=self.width+30, y=self.window_height-70)

    def back_button(self):
        back_grid_button = Button(self.root, text="Back to menu", width=20, background="black", fg="white", command=self.parent.init_window, font="Roboto")
        back_grid_button.place(x=self.width+30, y=self.window_height-35)

    def enter_file_name(self):
        label_name = Label(self.root, text='File name:', font=("Roboto", 12, 'bold'))
        label_name.place(x=self.width+10, y=self.window_height-100, width=100)
        entry_file_name = Entry(self.root, width=10, textvariable=self.entry_file_name)
        entry_file_name.place(x=self.width+110, y=self.window_height-100+3, width=100)

    def save_grid_to_file(self):
        file_name = self.entry_file_name.get()
        if len(file_name) != 0:
            if self.grid.start_node is not None and self.grid.end_node is not None:
                final_name = f'{path}{self.entry_file_name.get()}'
                print(final_name)
                outfile = open(final_name, 'wb')
                self.grid.root = None
                self.grid.grid_config = None
                pickle.dump(self.grid, outfile)
                outfile.close()
                self.parent.grid = self.grid
                self.parent.grid_name = self.entry_file_name.get()
                self.parent.init_window()
            else:
                messagebox.showerror("Error", "Set start and end nodes")
        else:
            messagebox.showerror("Error", "Invalid file name")

    def upload_grid_from_file(self, file_name):
        in_file = open(file_name, 'rb')
        self.grid = pickle.load(in_file, encoding='bytes')
        self.grid.root = self.root
        self.grid.grid_config = self

    def set_start_node(self, event):
        rectId = self.grid.find_closest_node(self.canvas, event)
        start_node = self.grid.find_node_by_id(rectId)
        start_node.type = StartNode()
        if start_node is not None:
            self.mode = None
            self.canvas.itemconfig(rectId, fill=start_node.type.color)
            self.grid.start_node = start_node

    def set_end_node(self, event):
        rectId = self.grid.find_closest_node(self.canvas, event)
        end_node = self.grid.find_node_by_id(rectId)
        end_node.type = EndNode()
        if end_node is not None:
            self.mode = None
            self.canvas.itemconfig(rectId, fill=end_node.type.color)
            self.grid.end_node = end_node

    def mouse_click(self, event):
        if self.mode == START and self.grid.start_node is None:
            self.set_start_node(event)
        elif self.mode == END and self.grid.end_node is None:
            self.set_end_node(event)
        else:
            self.can_draw = True
            self.mouse_move(event)

    def mouse_release(self, event):
        self.can_draw = False

    def mouse_move(self, event):
        print(self.can_draw)
        print(self.mode)
        if self.can_draw:
            if self.mode == DRAW_OBSTACLE:
                self.set_obstacle(event)
            elif self.mode == DRAW_GROUND:
                self.set_ground(event)
            elif self.mode == DRAW_RIVER:
                self.set_river(event)
            elif self.mode == CLEAR:
                self.set_clear(event)

    def set_obstacle(self, event):
        rectId = self.grid.find_closest_node(self.canvas, event)
        obstacle = self.grid.find_node_by_id(rectId)
        obstacle.cost = sys.maxsize
        obstacle.type = Obstacle()
        self.canvas.itemconfig(rectId, fill=obstacle.type.color)

    def set_ground(self, event):
        rectId = self.grid.find_closest_node(self.canvas, event)
        ground = self.grid.find_node_by_id(rectId)
        ground.type = Ground()
        ground.cost = 3
        self.canvas.itemconfig(rectId, fill=ground.type.color)

    def set_river(self, event):
        rectId = self.grid.find_closest_node(self.canvas, event)
        river = self.grid.find_node_by_id(rectId)
        river.type = River()
        river.cost = 5
        self.canvas.itemconfig(rectId, fill=river.type.color)

    def set_clear(self, event):
        rectId = self.grid.find_closest_node(self.canvas, event)
        node_to_clear = self.grid.find_node_by_id(rectId)
        if self.grid.start_node == node_to_clear:
            self.grid.start_node = None
        elif self.grid.end_node == node_to_clear:
            self.grid.end_node = None
        node_to_clear.type = None
        node_to_clear.cost = sys.maxsize
        self.canvas.itemconfig(rectId, fill="white")

    def bind_func(self):
        self.canvas.bind('<Button-1>', self.mouse_click)
        self.canvas.bind('<ButtonRelease-1>', self.mouse_release)
        self.canvas.bind('<B1-Motion>', self.mouse_move)

    def update_grid(self):
        for nodes in self.grid.board:
            for node in nodes:
                if node.type is not None:
                    self.canvas.itemconfig(node.rectId, fill=node.type.color)
        self.root.update()

    def display_grid_board(self):
        self.bind_func()
        nodes = []
        node_size = self.grid.node_size
        for y in range(int(self.grid.height / node_size)):
            node = []
            for x in range(int(self.grid.width / node_size)):
                x0 = x * node_size
                x1 = x0 + node_size
                y0 = y * node_size
                y1 = y0 + node_size
                rect = self.canvas.create_rectangle(x0, y0, x1, y1, outline='black', fill='white')
                node.append(Node(x, y, rect))
            nodes.append(node)
        self.canvas.update()
        if self.grid.board is None or len(self.grid.board) == 0:
            self.grid.board = nodes
