from pathVisualisation.GridBoard import *
from windows.WindowsOption import *
from pathVisualisation.Node import *
from tkinter import *
from windows.GridConfig import *
import time
import copy


class GridVisualisation:

    def __init__(self, grid, root):
        self.grid = grid
        self.root = root
        self.time_refresh = 0.05
        self.state_number = 0
        self.states = None
        self.auto_running = None

    def init_grid_visualisation(self):
        clear_window(self.root)
        self.grid.grid_config_initialize(self)
        self.grid.grid_config.init_grid()
        self.update_grid_state_number(self.states[0])

        padding_x = self.grid.grid_config.width
        btn = Button(self.root, text="Next", width=20, background="black", fg="white", command=self.inc_state)
        btn.place(x=padding_x + 50, y=50)

        btn2 = Button(self.root, text="Prev", width=20, background="black", fg="white", command=self.dec_state)
        btn2.place(x=padding_x + 50, y=100)

        btn3 = Button(self.root, text="Automat", width=20, background="black", fg="white", command=self.auto_run)
        btn3.place(x=padding_x + 50, y=150)

        btn4 = Button(self.root, text="Stop", width=20, background="black", fg="white",
                      command=self.stop_auto)
        btn4.place(x=padding_x + 50, y=200)

        create_back_button = Button(self.root, text="Back to menu", width=20, background="black", fg="white",
                                    command=self.grid.parent.init_window, font="Roboto")
        create_back_button.place(x=padding_x + 50, y=350)


    def start_algorithm(self):
        self.grid.algorithm.start_algorithm()
        self.states = self.grid.algorithm.algorithm()

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

    def clear_state(self, state):
        for node in state:
            self.grid.grid_config.canvas.itemconfig(node.rectId, fill="white")
        self.root.update()

    def auto_run(self):
        self.auto_running = True
        start = self.state_number
        for i in range(start, len(self.states) - 1):
            if self.auto_running:
                self.state_number += 1
                self.update_grid_state_number(self.states[i])
                time.sleep(self.time_refresh)
            else:
                break
        if self.state_number == len(self.states) - 1:
            self.update_grid_state_number(self.states[self.state_number][:1])
            self.print_path("green")
            self.grid.board = self.states[0]

    def stop_auto(self):
        self.auto_running = False

    def update_grid_state_number(self, state):
        for node in state:
            if node.type is not None:
                self.grid.grid_config.canvas.itemconfig(node.rectId, fill=node.type.color)
        self.root.update()



    def color_node(self, node, color):
        self.grid.grid_config.canvas.itemconfig(node, fill=color)
        self.root.update()


    def change_node_color(self, node, color):
        self.grid.grid_config.canvas.itemconfig(node.rectId, fill=color)
        self.root.update()
        time.sleep(self.time_refresh)

    def update_grid(self):
        for node in self.grid.node_to_change:
            if node.type is not None:
                self.grid.grid_config.canvas.itemconfig(node.rectId, fill=node.type.color)
        self.root.update()
        # time.sleep(self.time_refresh)
        self.grid.node_to_change = []

