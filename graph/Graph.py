import networkx as nx
import random
import tkinter as Tk
import copy
from matplotlib import pyplot as plt, animation
from algorithms.Bfs import Bfs
from algorithms.Dfs import Dfs
from algorithms.dijkstra import Dijkstra
from algorithms.RandomAlgorithm import RandomAlgorithm
from algorithms.RandomAlgorithmWithRepeats import RandomAlgorithmWithRepeats
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Graph:
    def __init__(self):
        self.n = 0
        self.graph = None
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
        self.edgeLabels = {}
        self.actualChecked = -1

#
    def loadGraph(self):
        # TODO
        pass
#tworzenie grafu, wyśiwtlanego na ekranie
    def randomTree(self, n, degree):
        self.n = n
        while True:
            self.graph = nx.full_rary_tree(degree,self.n)     #tworzenie innego grafu(tree) w tym miejscu
            if  nx.is_connected(self.graph):
                for u, v in self.graph.edges:
                    self.edgeLabels[u, v] = random.randint(0, 10)
                self.position = nx.spring_layout(self.graph)
                break
    def randomGraph(self, n,degree):
        if (n * degree)%2 == 0:
            self.n = n
        else:
            print("Zeby utworzyć graf tego stopni o podanej liczbie wierzchołków n * negree musi być parzyste")
            self.n = n+1
        while True:
            self.graph = nx.random_regular_graph(degree,self.n)     #tworzenie innego grafu(tree) w tym miejscu
            if  nx.is_connected(self.graph):
                for u, v in self.graph.edges:
                    self.edgeLabels[u, v] = random.randint(0, 10)
                self.position = nx.spring_layout(self.graph)
                break
#Inicjalizacja daych pomocniczych do grafu
    def data_init(self):
        self.color_map = ["green"] * self.n
        self.size_map = [500]*self.n

        for id in self.position.keys():
            self.order.append(id)
        for u,v in self.graph.edges:
            self.width[u,v] = 0.1
        self.color_map[self.order.index(self.actual_node)] = "red"
        self.size_map[self.order.index(self.actual_node)] = 1000
    def dataReset(self):
        self.color_map = []     # mapa kolorów node'ów
        self.size_map = []      # mapa rozmiarów node
        self.actual_node = 0    # pierwszy node
        self.width = {}
        self.labels = {}
        self.visited = []       # zmienne obrazujące które wierzchołki musimy jeszcze przejrzeć, a które zostały sprawdzone w całości
        self.tovisit = []
        self.order = []         # Rysowanie odbywa się wedle pozycji, a te pozycje zapisane są w tablicy order
        self.order_label = 0    # zmienne pomocnicze w przedzielaniu labeli na nodach
        self.prev_head = -1

        self.data_init()
        self.actualChecked = -1
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
        if self.actualChecked !=-1:
            self.color_map[self.order.index(self.actualChecked)] = "orange"


    def __str__(self):
        return "Graph n: " + str(self.n)

