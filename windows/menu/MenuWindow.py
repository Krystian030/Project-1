from tkinter import *
import os
from windows.menu.GridMenu import GridMenu
from graph.Graph import Graph
from pathVisualisation.GridBoard import GridBoard
from visualisation.GraphVisualization import GraphVisualization
from functools import partial
class MenuWindow:

    def __init__(self, root):
        self.root = root
        self.bg = PhotoImage(file="resources/background.png")
        self.banner = PhotoImage(file="resources/banner.png")
        self.createBackground()
        self.createBanner()
        self.createBtnGridBoard()
        self.createBtnGraph()
        self.varAlg = IntVar(value=1)
        self.varGraph = IntVar()
        self.numberOfN = StringVar()
        self.numberOfDegree = StringVar()
    # set background
    def createBackground(self):
        bgLabel = Label(self.root, image=self.bg)
        bgLabel.place(x=-5, y=0)

    # set banner
    def createBanner(self):
        bannerLabel = Label(self.root, image=self.banner)
        bannerLabel.grid(row=1,column=1)

    # GridMenu
    def createGridMenu(self):
        GridMenu(self.root)
        pass
        # GridBoard(self.root, 800, 600)

    def createBtnGridBoard(self):
        B = Button(self.root, text='Grid', width=35, height=20, background="black", fg="white", command=self.createGridMenu)
        B.place(x=100, y=500)

    def createBtnGraph(self):
        B2 = Button(self.root, text='Graph algorithm', width=35, height=20, background="black", fg="white",
                   command=self.createOptionsForGraph)
        B2.place(x=600, y=500)


    def createOptionsForGraph(self):
        for ele in self.root.winfo_children():
            ele.destroy()
        self.createBackground()
        self.createBanner()
        entryNumber = Entry(width=4, textvariable=self.numberOfN)
        entryNumber.place(x=600, y=240)
        labelN = Label(self.root, text='Numer of nodes')
        labelN.place(x=570, y=220)
        entryNumber = Entry(width=4, textvariable=self.numberOfDegree)
        entryNumber.place(x=600, y=280)
        labelN = Label(self.root, text='Degree')
        labelN.place(x=570, y=260)

        labelA = Label(self.root, text='Choose algorithm')
        labelA.place(x=580, y=310)
        R2 = Radiobutton(self.root, text="Bfs", value=1, variable=self.varAlg)
        R2.place(x=600, y=340)
        R3 = Radiobutton(self.root, text="Dfs", value=2, variable=self.varAlg)
        R3.place(x=600, y=360)
        R4 = Radiobutton(self.root, text="Dijkstra", value=3, variable=self.varAlg)
        R4.place(x=600, y=380)

        labelA = Label(self.root, text='Choose what type of graph you want')
        labelA.place(x=550, y=420)
        R2 = Radiobutton(self.root, text="Tree", value=0, variable=self.varGraph)
        R2.place(x=600, y=450)
        R3 = Radiobutton(self.root, text="Full graph", value=1, variable=self.varGraph)
        R3.place(x=600, y=470)

        B = Button(self.root, text='Start', width=5, height=2, background="black", fg="white",
                   command=self.createWindowGraph)
        B.place(x=600, y=500)


    def createWindowGraph(self):
        if self.varAlg.get()==0:
            self.varAlg = IntVar(value=1)
        n = 0
        degree = 2
        if self.numberOfN.get()!='':
            n = int(self.numberOfN.get())
        if self.numberOfDegree.get()!='':
            degree = int(self.numberOfDegree.get())
        graph = Graph()
        if self.varGraph.get()==0:
            graph.randomTree(n,degree)
        else:
            graph.randomGraph(n, degree)
        if n!=0:
            GraphVisualization.visualizationGraph(graph,self.varAlg.get())

