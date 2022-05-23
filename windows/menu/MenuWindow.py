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
        self.varGraph = IntVar(value=0)
        self.numberOfN = StringVar(value="26")
        self.numberOfDegree = StringVar(value="3")
        self. n = 0
        self.degree = 2
        self.graph = None
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
        entryNumber = Entry(width=10, textvariable=self.numberOfN)
        entryNumber.place(x=600, y=250)
        labelN = Label(self.root, text='Numer of nodes', font=("Roboto", 12, 'bold'), bg="gray")
        labelN.place(x=570, y=220)
        entryNumber = Entry(width=10, textvariable=self.numberOfDegree)
        entryNumber.place(x=600, y=310)
        labelN = Label(self.root, text='Degree',  font=("Roboto", 12, 'bold'), bg="gray")
        labelN.place(x=600, y=280)

        labelA = Label(self.root, text='Choose algorithm', font=("Roboto", 14, 'bold'), bg="gray")
        labelA.place(x=580, y=340)
        R2 = Radiobutton(self.root, text="Bfs", value=1, variable=self.varAlg, font=("Roboto", 12, 'bold'), bg="gray")
        R2.place(x=600, y=370)
        R3 = Radiobutton(self.root, text="Dfs", value=2, variable=self.varAlg, font=("Roboto", 12, 'bold'), bg="gray")
        R3.place(x=600, y=400)
        R4 = Radiobutton(self.root, text="Dijkstra", value=3, variable=self.varAlg, font=("Roboto", 12, 'bold'), bg="gray")
        R4.place(x=600, y=430)

        R5 = Radiobutton(self.root, text="A*", value=4, variable=self.varAlg, font=("Roboto", 12, 'bold'),
                         bg="gray")
        R5.place(x=600, y=460)

        labelA = Label(self.root, text='Choose what type of graph you want', font=("Roboto", 14, 'bold'), bg="gray")
        labelA.place(x=550, y=500)
        R2 = Radiobutton(self.root, text="Tree", value=0, variable=self.varGraph, font=("Roboto", 12, 'bold'), bg="gray")
        R2.place(x=600, y=530)
        R3 = Radiobutton(self.root, text="Full graph", value=1, variable=self.varGraph, font=("Roboto", 12, 'bold'), bg="gray")
        R3.place(x=600, y=560)

        B = Button(self.root, text='Start', width=10, height=2, background="black", fg="white",
                   command=self.createWindowGraph, font=("Roboto", 14, 'bold'))
        B.place(x=570, y=600)


    def createWindowGraph(self):

        if self.varAlg.get()==0:
            self.varAlg = IntVar(value=1)


        if (self.n != int(self.numberOfN.get()) or self.degree !=int(self.numberOfDegree.get())):
            if self.numberOfN.get()!='':
                self.n = int(self.numberOfN.get())
            if self.numberOfDegree.get()!='':
                self.degree = int(self.numberOfDegree.get())
            self.graph = Graph()
            if self.varGraph.get()==0:
                self.graph.randomTree(self.n,self.degree)
            else:
                self.graph.randomGraph(self.n, self.degree)
        else:
            self.graph.dataReset()
        if self.n!=0:
            GraphVisualization.visualizationGraph(self.graph,self.varAlg.get())

