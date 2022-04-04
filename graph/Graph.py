import networkx as nx
from matplotlib import pyplot as plt, animation
import random
import time
from algorithms.Bfs import Bfs
class Graph:
    def __init__(self):
        self.n = 0
        self.graph = None
        self.fig=plt.figure()
        self.position=None
        self.color_map = []
        self.size_map=[]
        self.actual_node=0
        self.width = {}
        self.degreeMap=[]
        self.labels={}
        self.visited = []
        self.tovisit=[]
        self.order=[]  # Rysowanie odbywa się wedle pozycji, a te pozycje zapisane są w tablicy order
        self.order_label=0
        self.prev_head=-1
    def createRandomGraph(self):
        # TODO
        pass
#
    def loadGraph(self):
        # TODO
        pass
    def randomGraph(self, n, density):
        self.n = n
        g=0
        while True:
            g+=1
            self.degreeMap.clear()
            for i in range(0, self.n):
                self.degreeMap.append(random.randint(1,3))
            self.graph = nx.random_regular_graph(3,self.n)
            if  nx.is_connected(self.graph):
                break

    def data_init(self):
        for node in self.graph:
            self.color_map.append("green")
            self.size_map.append(500)
        self.position = nx.spring_layout(self.graph,k=10,iterations=1000)
        for id in self.position.keys():
            self.order.append(id)
        for u,v in self.graph.edges:
            self.width[u,v] = 0.1
        self.color_map[self.order.index(self.actual_node)] = "red"
        self.size_map[self.order.index(self.actual_node)] = 1000
    def set_color(self):
        for a in self.tovisit:
            self.color_map[self.order.index(a)] = "yellow"
        for a in self.visited:
            self.color_map[self.order.index(a)] = "blue"
        if not self.actual_node == -1:
            self.color_map[self.order.index(self.actual_node)] = "red"
            if not self.prev_head == self.actual_node:
                self.labels[self.actual_node] = str(self.order_label+1)
                self.order_label+=1
                self.prev_head=self.actual_node

    def visualizationGraph(self):
        self.data_init()
        nx.draw(self.graph,self.position,node_size=self.size_map,node_color=self.color_map,font_size=11,with_labels=True,
                width=list(self.width.values()),labels=self.labels)
        plt.title("Graph n: " + str(self.n))
        alg=Bfs(self)

        def animate(frame):
            if self.actual_node<self.n:
                self.fig.clear()
                if not self.actual_node == -1:
                    alg.func(self)
                self.set_color()

                nx.draw(self.graph, self.position, node_size=self.size_map, node_color=self.color_map,
                            font_size=7, with_labels=True, width=list(self.width.values()),labels=self.labels)
        ani=animation.FuncAnimation(self.fig,animate, interval=1000,repeat=True)
        plt.show()
    def __str__(self):
        return "=== Graph ===\n" + "n: " + str(self.n)

