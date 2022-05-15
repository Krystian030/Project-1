from pathVisualisation.GridBoard import *
from pathVisualisation.Node import *
from tkinter import *
import time

class GridVisualisation:

    def __init__(self, grid, root, width, height):
        self.grid = grid
        self.root = root
        self.clear_window(self.root)
        self.window_width = width
        self.window_height = height
        # self.outer_canvas, self.inner_canvas = self.create_canvas()
        self.outer_canvas, self.inner_canvas = self.create_canvas()
        self.btn_algorithm = self.create_btn_start_algorithm()
        self.radio_btn_option = IntVar()
        #       mark start, mark end, draw obstacles
        self.mode = [False, False, False]
        self.time_refresh = 0.1
        self.can_draw = False
        self.r1_btn, self.r2_btn, self.r3_btn, self.r4_btn = self.create_radio_btn()
        self.elements = [self.r1_btn, self.r2_btn, self.r3_btn, self.r4_btn, self.btn_algorithm]
        self.state_number = 0
        self.states = None
        self.auto_running = None

    @staticmethod
    def clear_window(to_clean):
        for widget in to_clean.winfo_children():
            widget.destroy()

    def create_btn_start_algorithm(self):
        btn = Button(self.outer_canvas, text="Start algorithm", width=20, background="black", fg="white",
                     command=self.start_algorithm)
        btn.place(x=1000, y=250)
        return btn

    def print_path(self, color):
        for node in self.grid.path:
            self.change_node_color(node, color)

    def inc_state(self):
        if self.state_number < len(self.states) - 1:
            self.state_number += 1
            self.update_grid_state_number(self.states[self.state_number])
        # ostatni state
        elif self.state_number == len(self.states) - 1:
            self.update_grid_state_number(self.states[self.state_number][:1])
            self.print_path("green")

    def dec_state(self):
        if self.state_number > 0:
            self.clear_state(self.states[self.state_number])
            if self.state_number == len(self.states) - 1:
                self.print_path("blue")
            self.state_number -= 1
            self.update_grid_state_number(self.states[self.state_number])

    def start_algorithm(self):
        self.grid.algorithm.start_algorithm()
        self.states = self.grid.algorithm.bfs_algorithm()

        # for x in self.states:
        #     for node in x:
        #         self.inner_canvas.itemconfig(node.rectId, fill=node.type.color)
        #     self.root.update()

        for element in self.elements:
            element.destroy()
        btn = Button(self.outer_canvas, text="Next", width=20, background="black", fg="white", command=self.inc_state)
        btn.place(x=1000, y=250)

        btn2 = Button(self.outer_canvas, text="Prev", width=20, background="black", fg="white", command=self.dec_state)
        btn2.place(x=1000, y=400)

        btn3 = Button(self.outer_canvas, text="Automat", width=20, background="black", fg="white", command=self.auto_run)
        btn3.place(x=1000, y=300)

        btn4 = Button(self.outer_canvas, text="Stop", width=20, background="black", fg="white",
                      command=self.stop_auto)
        btn4.place(x=1000, y=350)

    def clear_state(self, state):
        for node in state:
            self.inner_canvas.itemconfig(node.rectId, fill="white")
        self.root.update()

    def auto_run(self):
        self.auto_running = True
        start = self.state_number
        for i in range(start, len(self.states) - 1):
            if self.auto_running:
                self.state_number += 1
                for node in self.states[i]:
                    self.inner_canvas.itemconfig(node.rectId, fill=node.type.color)
                self.root.update()
            else:
                break
        if self.state_number == len(self.states) - 1:
            self.update_grid_state_number(self.states[self.state_number][:1])
            self.print_path("green")

    def stop_auto(self):
        # self.clear_state(self.states[self.state_number-1])
        self.auto_running = False

    def update_grid_state_number(self, state):
        for node in state:
            self.inner_canvas.itemconfig(node.rectId, fill=node.type.color)
        self.root.update()
        # time.sleep(self.time_refresh)
        # self.grid.node_to_change = []

    def set_mode(self):
        mode = self.radio_btn_option.get()
        for i in range(len(self.mode)):
            if i + 1 == mode:
                self.mode[i] = True
            else:
                self.mode[i] = False

    def create_radio_btn(self):
        r1 = Radiobutton(self.outer_canvas, text="Mark start", variable=self.radio_btn_option, value=1,
                         command=self.set_mode, width=20, font="Roboto")
        r1.place(x=950, y=50)

        r2 = Radiobutton(self.outer_canvas, text="Mark end", variable=self.radio_btn_option, value=2,
                         command=self.set_mode, width=20, font="Roboto")
        r2.place(x=950, y=100)

        r3 = Radiobutton(self.outer_canvas, text="Draw obstacles", variable=self.radio_btn_option, value=3,
                         command=self.set_mode, width=20, font="Roboto")
        r3.place(x=950, y=150)

        r4 = Radiobutton(self.outer_canvas, text="Set cost", variable=self.radio_btn_option, value=4,
                         command=self.set_mode, width=20, font="Roboto")
        r4.place(x=950, y=200)

        return r1, r2, r3, r4

    def create_canvas(self):
        outer_canvas = Canvas(self.root, width=self.window_width, height=self.window_height)
        outer_canvas.pack()

        inner_canvas = Canvas(outer_canvas, height=self.grid.height, width=self.grid.width)
        inner_canvas.place(x=0, y=0)

        return outer_canvas, inner_canvas

    def bind_func(self):
        self.inner_canvas.bind('<Button-1>', self.mouse_click)
        self.inner_canvas.bind('<ButtonRelease-1>', self.mouse_release)
        self.inner_canvas.bind('<B1-Motion>', self.mouse_move)

    def set_obstacle(self, event):
        rectId = self.grid.find_closest_node(self.inner_canvas, event)
        self.inner_canvas.itemconfig(rectId, fill="red")
        obstacle = self.grid.find_node_by_id(rectId)
        obstacle.type = 'obstacle'

    def mouse_move(self, event):
        if self.can_draw:
            self.set_obstacle(event)

    def set_start_node(self, event):
        rectId = self.grid.find_closest_node(self.inner_canvas, event)
        start_node = self.grid.find_node_by_id(rectId)
        if start_node is not None:
            self.mode[0] = False
            self.color_node(rectId, "green")
            self.grid.start_node = start_node

    def set_end_node(self, event):
        rectId = self.grid.find_closest_node(self.inner_canvas, event)
        end_node = self.grid.find_node_by_id(rectId)
        if end_node is not None:
            self.mode[1] = False
            self.color_node(rectId, "purple")
            self.grid.end_node = end_node

    def color_node(self, node, color):
        self.inner_canvas.itemconfig(node, fill=color)
        self.root.update()

    def change_node_color(self, node, color):
        self.inner_canvas.itemconfig(node.rectId, fill=color)
        self.root.update()
        time.sleep(self.time_refresh)

    def mouse_click(self, event):
        if self.mode[0] and self.grid.start_node is None:
            self.set_start_node(event)
        if self.mode[1] and self.grid.end_node is None:
            self.set_end_node(event)
        if self.mode[2]:
            self.can_draw = True
            self.mouse_move(event)

    def mouse_release(self, event):
        self.can_draw = False

    def display_grid_board(self):
        # clear window
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
                rect = self.inner_canvas.create_rectangle(x0, y0, x1, y1, outline='black', fill='white')
                node.append(Node(x, y, rect))
            nodes.append(node)
        self.inner_canvas.update()
        return nodes

    def update_grid(self):
        for node in self.grid.node_to_change:
            self.inner_canvas.itemconfig(node.rectId, fill=node.type.color)
        self.root.update()
        # time.sleep(self.time_refresh)
        self.grid.node_to_change = []
