from tkinter import *
from pathVisualisation.Node import Node
import time
from algorithms.Bfs import Bfs

class GridBoard:
    def __init__(self, root, width, height):
        self.btnBFS = None
        self.startNode = None
        self.endNode = None
        self.canDrawStart = False
        self.canDrawEnd = False
        self.outerCanvas = None
        self.canvas = None
        self.root = root
        self.width = width
        self.height = height
        self.rHeight = 900
        self.rWidth = 1280
        self.nodeSize = 20
        self.cols = int(width / self.nodeSize)
        self.rows = int(height / self.nodeSize)
        self.GridBoard = []
        self.path = []
        self.timeRefresh = 0.02
        self.timeRefresh2 = 0.000001
        self.canDraw = False
        self.gridOption = IntVar()
        self.canDrawObstacle = False

    def createBtnBFS(self):
        self.btnBFS = Button(self.root, text='Uruchom algorytm', width=20, background="black", fg="white", command= lambda: Bfs.bfsGridBoard(self))


        self.btnBFS.place(x=1000, y=250)

    def createRadioButtoins(self):
        self.r1 = Radiobutton(self.outerCanvas, text="Rysuj przeszkodę", variable=self.gridOption, value=1,
                         command=self.setFlags, width=20, font="Roboto")
        self.r1.place(x=950, y=100)
        self.r2 = Radiobutton(self.outerCanvas, text="Zaznacz start", variable=self.gridOption, value=2, command=self.setFlags, width=20, font="Roboto")
        self.r2.place(x=950, y=150)
        self.r3 = Radiobutton(self.outerCanvas, text="Zaznacz koniec", variable=self.gridOption, value=3, command=self.setFlags, width=20, font="Roboto")
        self.r3.place(x=950, y=200)

    def setDraw(self, drawObstacle, drawStart, drawEnd):
        self.canDrawObstacle = drawObstacle
        self.canDrawStart = drawStart
        self.canDrawEnd = drawEnd

    def setFlags(self):
        if self.gridOption.get() == 1:
            self.setDraw(True, False, False)
        if self.gridOption.get() == 2:
            self.setDraw(False, True, False)
        if self.gridOption.get() == 3:
            self.setDraw(False, False, True)
        print("Option: " + str(self.gridOption.get()))

    def printPath(self):
        if self.path:
            for node in self.path:
                self.canvas.itemconfig(node.rectId, fill="green")
                self.root.update()
                time.sleep(self.timeRefresh)

    def printChild(self, node):
        self.canvas.itemconfig(node.rectId, fill="orange")
        self.root.update()
        time.sleep(self.timeRefresh2)

    def printVisited(self, node):
        self.canvas.itemconfig(node.rectId, fill="blue")
        self.root.update()
        time.sleep(self.timeRefresh2)

    def printRed(self, node):
        self.canvas.itemconfig(node.rectId, fill="red")
        self.root.update()
        time.sleep(self.timeRefresh2)

    def printGreen(self, node):
        self.canvas.itemconfig(node.rectId, fill="green")
        self.root.update()
        time.sleep(self.timeRefresh2)

    def printActual(self, node):
        self.canvas.itemconfig(node.rectId, fill="black")
        self.root.update()
        time.sleep(self.timeRefresh2)

    def printWhite(self, node):
        self.canvas.itemconfig(node.rectId, fill="white")
        self.root.update()
        time.sleep(self.timeRefresh2)

    def mouseMove(self, event):
        coloring = "red"
        if self.canDraw:
            rectId = self.colorNode(event, coloring)



    def colorNode(self, event, color):
        node = self.canvas.find_closest(event.x, event.y)
        self.canvas.itemconfig(node, fill=color)
        return node

    def mouseRelease(self, event):
        self.canDraw = False

    def mouseClick(self, event):
        # node = self.canvas.find_closest(event.x, event.y)
        # print(node[0])
        if self.canDrawStart and self.startNode is None:
            rectId = self.colorNode(event, "green")
            self.startNode = self.find(rectId[0])
            self.canDrawStart = False
        if self.canDrawEnd and self.endNode is None:
            rectId = self.colorNode(event, "black")
            self.endNode = self.find(rectId[0])
            self.canDrawEnd = False
        if self.canDrawObstacle:
            self.canDraw = True
            self.mouseMove(event)

    def createCanvas(self):
        # create canvas
        self.outerCanvas = Canvas(self.root, width=self.rWidth, height=self.rHeight)
        self.outerCanvas.pack()
        self.canvas = Canvas(self.outerCanvas, height=self.height, width=self.width)
        self.canvas.place(x=0, y=0)
        self.canvas.bind('<Button-1>', self.mouseClick)
        self.canvas.bind('<ButtonRelease-1>', self.mouseRelease)
        self.canvas.bind('<B1-Motion>', self.mouseMove)

    def displayGridBoard(self):
        # clear window
        for widget in self.root.winfo_children():
            widget.destroy()

        self.createCanvas()
        self.createRadioButtoins()
        self.createBtnBFS()
        for y in range(0, self.rows):
            node = []
            for x in range(0, self.cols):
                x0 = x * self.nodeSize
                x1 = x0 + self.nodeSize
                y0 = y * self.nodeSize
                y1 = y0 + self.nodeSize
                rect = self.canvas.create_rectangle(x0, y0, x1, y1, outline='black', fill='white')
                node.append(Node(x, y, rect))
            self.GridBoard.append(node)
        self.canvas.update()

    def getNeighbours(self, node):
        possible_movements = []
        if node.y - 1 >= 0:
            possible_movements.append(self.GridBoard[node.y - 1][node.x])
        if node.x + 1 < len(self.GridBoard[node.y]):
            possible_movements.append(self.GridBoard[node.y][node.x + 1])
        if node.y + 1 < len(self.GridBoard):
            possible_movements.append(self.GridBoard[node.y + 1][node.x])
        if node.x - 1 >= 0:
            possible_movements.append(self.GridBoard[node.y][node.x - 1])

        return possible_movements

    def find(self, reactId):
        for x_nodes in self.GridBoard:
            for node in x_nodes:
                if node.rectId == reactId:
                    return node

    def createPath(self,node):
        self.path = [node]
        while node.parent is not None:
            node = node.parent
            self.path.append(node)
