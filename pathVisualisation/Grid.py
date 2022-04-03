from tkinter import *
from pathVisualisation.Node import Node
import time


class Grid:
    def __init__(self, root, width, height):
        self.canvas = None
        self.root = root
        self.width = width
        self.height = height
        self.nodeSize = 20
        self.cols = int(width / self.nodeSize)
        self.rows = int(height / self.nodeSize)
        self.grid = []
        self.path = []
        self.timeRefresh = 0.02
        self.timeRefresh2 = 0.000001
        self.canDraw = False

    def printPath(self):
        if self.path:
            for node in self.path:
                self.canvas.itemconfig(node.rectId, fill="green")
                self.root.update()
                time.sleep(self.timeRefresh)

    def printChild(self,node):
        self.canvas.itemconfig(node.rectId, fill="orange")
        self.root.update()
        time.sleep(self.timeRefresh2)

    def printVisited(self,node):
        self.canvas.itemconfig(node.rectId, fill="blue")
        self.root.update()
        time.sleep(self.timeRefresh2)

    def printRed(self,node):
        self.canvas.itemconfig(node.rectId, fill="red")
        self.root.update()
        time.sleep(self.timeRefresh2)

    def printGreen(self,node):
        self.canvas.itemconfig(node.rectId, fill="green")
        self.root.update()
        time.sleep(self.timeRefresh2)

    def printActual(self,node):
        self.canvas.itemconfig(node.rectId, fill="black")
        self.root.update()
        time.sleep(self.timeRefresh2)

    def printWhite(self,node):
        self.canvas.itemconfig(node.rectId, fill="white")
        self.root.update()
        time.sleep(self.timeRefresh2)

    def mouseMove(self, event):
        # print("Mouse position: (%s %s)" % (event.x, event.y))
        if self.canDraw:
            node = self.canvas.find_closest(event.x, event.y)
            self.canvas.itemconfig(node, fill="red")

    def mouseRelease(self, event):
        self.canDraw = False

    def mouseClick(self, event):
        node = self.canvas.find_closest(event.x, event.y)
        print(node[0])
        self.canDraw = True
        #self.mouseMove(event)

    def createCanvas(self):
        # create canvas
        self.canvas = Canvas(self.root, height=self.height, width=self.width)
        self.canvas.grid(row=0, column=1)
        self.canvas.bind('<Button-1>', self.mouseClick)
        self.canvas.bind('<ButtonRelease-1>', self.mouseRelease)
        self.canvas.bind('<B1-Motion>', self.mouseMove)

    def displayGrid(self):
        # clear window
        for widget in self.root.winfo_children():
            widget.destroy()

        self.createCanvas()
        for y in range(0, self.rows):
            node = []
            for x in range(0, self.cols):
                x0 = x * self.nodeSize
                x1 = x0 + self.nodeSize
                y0 = y * self.nodeSize
                y1 = y0 + self.nodeSize
                rect = self.canvas.create_rectangle(x0, y0, x1, y1, outline='black', fill='white')
                node.append(Node(x, y, rect))
            self.grid.append(node)
        self.canvas.update()

    def getNeighbours(self, node):
        possible_movements = []
        if node.y - 1 >= 0:  # north
            possible_movements.append(self.grid[node.y - 1][node.x])
        if node.x + 1 < len(self.grid[node.y]):  # east
            possible_movements.append(self.grid[node.y][node.x + 1])
        if node.y + 1 < len(self.grid):  # south
            possible_movements.append(self.grid[node.y + 1][node.x])
        if node.x - 1 >= 0:  # west
            possible_movements.append(self.grid[node.y][node.x - 1])

        return possible_movements

    def find(self, x,y):
        for x_nodes in self.grid:
            for node in x_nodes:
                if node.x == x and node.y == y:
                    return node

def createPath(node):
    path = [node]
    while node.parent is not None:
        node = node.parent
        path.append(node)
    return path
