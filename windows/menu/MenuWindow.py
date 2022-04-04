from tkinter import *
import os

from graph.Graph import Graph
from pathVisualisation.GridBoard import GridBoard


class MenuWindow:

    def __init__(self, root):
        self.root = root
        self.bg = PhotoImage(file="resources/background.png")
        self.banner = PhotoImage(file="resources/banner.png")
        self.createBackground()
        self.createBanner()
        self.createBtnGridBoard()
        self.createBtnGraph()

    # set background
    def createBackground(self):
        bgLabel = Label(self.root, image=self.bg)
        bgLabel.place(x=-5, y=0)

    # set banner
    def createBanner(self):
        bannerLabel = Label(self.root, image=self.banner)
        bannerLabel.grid(row=1,column=1)

    # GridBoard
    def createBtnGridBoard(self):
        g = GridBoard(self.root, 800, 600)
        B = Button(self.root, text='Grid algorithms', width=35, height=20, background="black", fg="white", command=g.displayGridBoard)
        B.place(x=100, y=500)

    def createBtnGraph(self):
        graph = Graph()
        graph.randomGraph(6,1)
        B2 = Button(self.root, text='Graph algorithm', width=35, height=20, background="black", fg="white",
                   command=graph.visualizationGraph)
        B2.place(x=600, y=500)
