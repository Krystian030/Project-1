import networkx as nx
import random
import time
import tkinter as Tk
import copy
from matplotlib import pyplot as plt, animation
from algorithms.Bfs import Bfs
from algorithms.Dfs import Dfs
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Graph:
    def __init__(self):
        self.n = 0
        self.graph = None
        self.fig=plt.figure()
        self.position=None
        self.color_map = []     #mapa kolorów node'ów
        self.size_map=[]        #mapa rozmiarów node
        self.actual_node=0      #pierwszy node
        self.width = {}
        self.labels={}
        self.visited = []   #zmienne obrazujące które wierzchołki musimy jeszcze przejrzeć, a które zostały sprawdzone w całości
        self.tovisit=[]
        self.order=[]  # Rysowanie odbywa się wedle pozycji, a te pozycje zapisane są w tablicy order
        self.order_label=0  #zmienne pomocnicze w przedzielaniu labeli na nodach
        self.prev_head=-1

    def createRandomGraph(self):
        # TODO
        pass
#
    def loadGraph(self):
        # TODO
        pass
#tworzenie grafu, wyśiwtlanego na ekranie
    def randomGraph(self, n, density):
        self.n = n
        while True:
            self.graph = nx.random_regular_graph(3,self.n)
            if  nx.is_connected(self.graph):
                break
#Inicjalizacja daych pomocniczych do grafu
    def data_init(self):
        self.color_map = ["green"] * self.n
        self.size_map = [500]*self.n
        self.position = nx.spring_layout(self.graph,k=10,iterations=1000)
        for id in self.position.keys():
            self.order.append(id)
        for u,v in self.graph.edges:
            self.width[u,v] = 0.1
        self.color_map[self.order.index(self.actual_node)] = "red"
        self.size_map[self.order.index(self.actual_node)] = 1000

#funkcja służaca do nadawania kolorów grafu, niebieskie to węzły przejrzane w całości, ikażdy ich sąsiad został przejrzany, zółty node przejrzany, ale jeszcze jego
#sąsiedzi są do przejrzenia, zielony-nieruszony, a niebieski to aktualnie przeglądany
    def set_color(self):
        for a in self.tovisit:
            self.color_map[self.order.index(a)] = "yellow"
        for a in self.visited:
            self.color_map[self.order.index(a)] = "blue"
        if not self.actual_node == -1:
            self.color_map[self.order.index(self.actual_node)] = "red"
            self.size_map[self.order.index(self.actual_node)] = 1000


    def visualizationGraph(self):
        self.data_init()
        stan_list = []
        root = Tk.Tk()
        root.wm_title("Graph n: " + str(self.n))
        # Quit when the window is done
        root.wm_protocol('WM_DELETE_WINDOW', root.quit)
        canvas = FigureCanvasTkAgg(self.fig, master=root)
        def drawCanvas():
            self.fig.clear()
            plt.clf()
            self.set_color()
            nx.draw_networkx(self.graph, self.position, node_size=self.size_map, node_color=self.color_map,
                             font_size=7, with_labels=True, labels=self.labels, width=list(self.width.values()))
            plt.axis('off')
            canvas.draw()
        drawCanvas()
        canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        alg=Dfs(self)
        def nextGraph():
            if self.actual_node<self.n and self.actual_node!= -1:
                stan_list.append(copy.deepcopy(self))
                if not self.actual_node == -1:
                    alg.func(self)
            drawCanvas()

        def prevGraph():
            if stan_list:
                self.__dict__.update(stan_list[-1].__dict__)
                stan_list.pop()
                drawCanvas()

        button_next = Tk.Button(root, text="next", command=nextGraph)
        button_next.pack()
        button_prev = Tk.Button(root, text="prev", command=prevGraph)
        button_prev.pack()

        Tk.mainloop()

    def __str__(self):
        return "=== Graph ===\n" + "n: " + str(self.n)

