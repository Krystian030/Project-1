from functools import partial
from tkinter import *

from pathVisualisation.GridVisualisation import GridVisualisation
from pathVisualisation.Node import Node
import time
from pathVisualisation.GridVisualisation import *
from algorithms.Bfs import *
from windows.GridConfig import *

class GridBoard:
    def __init__(self, root, width, height):
        self.root = root
        self.node_size = 20
        self.width = width * self.node_size
        self.height = height * self.node_size
        self.start_node = None
        self.end_node = None
        self.algorithm = BfsGrid(self)
        self.path = []
        # self.grid_visualisation = GridVisualisation(self, self.root,  self.width, self.height)
        # self.board = self.grid_visualisation.display_grid_board()
        self.board = None
        self.grid_config = GridConfig(self.root, self, self.width, self.height)
        self.node_to_change = []

    def printPath(self):
        for node in self.path:
            self.grid_visualisation.change_node_color(node, "green")

    def getNeighbours(self, node):
        possible_movements = []
        if node.x + 1 < len(self.board[node.y]) and self.board[node.y][node.x + 1].type != 'obstacle':
            possible_movements.append(self.board[node.y][node.x + 1])
        if node.x - 1 >= 0 and self.board[node.y][node.x - 1].type != 'obstacle':
            possible_movements.append(self.board[node.y][node.x - 1])
        if node.y - 1 >= 0 and self.board[node.y - 1][node.x].type != 'obstacle':
            possible_movements.append(self.board[node.y - 1][node.x])
        if node.y + 1 < len(self.board) and self.board[node.y + 1][node.x].type != 'obstacle':
            possible_movements.append(self.board[node.y + 1][node.x])
        return possible_movements

    def find_node_by_id(self, rectId):
        for x_nodes in self.board:
            for node in x_nodes:
                if node.rectId == rectId:
                    return node

    @staticmethod
    def find_closest_node(canvas, event):
        rectId = canvas.find_closest(event.x, event.y)
        return rectId[0]

    def createPath(self, node):
        self.path = [node]
        while node.parent is not None:
            node = node.parent
            self.path.append(node)
