import networkx as nx
from matplotlib import pyplot as plt, animation
import random
import time
class Graph:
    def __init__(self):
        self.n = None
        self.graph = None
        self.fig=plt.figure()
        self.color_map = []
        self.size_map=[]
        self.actual_node=0
        self.degreeMap=[]
        self.labels=[]
        self.visited = []
        self.tovisit=[]
        self.order=[] # Rysowanie odbywa się wedle pozycji, a te pozycje zapisane są w tablicy order
    def createRandomGraph(self):
        # TODO
        pass

    def loadGraph(self):
        # TODO
        pass

    # density - percent of density (1% - 100%) ok
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

    def set_color(self):
        if self.tovisit or not self.visited:

            if all(elem in self.tovisit+self.visited for elem in self.graph.neighbors(self.actual_node)):
                self.color_map[self.order.index(self.actual_node)] = "blue"
                self.visited.append(self.actual_node)
                self.actual_node=self.tovisit.pop(0)
                self.color_map[self.order.index(self.actual_node)] = "red"
            else:
                for a in self.graph.neighbors(self.actual_node):
                    if a not in self.tovisit and a not in self.visited:
                        self.tovisit.append(a)
                        break;
            for a in self.tovisit:
                self.color_map[self.order.index(a)] = "yellow"
            print(self.actual_node,"visi",self.visited,"to vi", self.tovisit)
            for a in self.graph.neighbors(self.actual_node):
                print(a, end=' ')
            print()
        else:
            self.color_map[self.order.index(self.actual_node)] = "blue"

    def visualizationGraph(self):
        for node in self.graph:
            self.color_map.append("green")
            self.size_map.append(500)
            self.labels.append(0)
        #TODO ustawianie grubości krawędzi w zależności czy przechodizmy przez niego
        #TODO tworzenie labelow
        pos = nx.spring_layout(self.graph,k=4,iterations=1000)
        print(pos.keys())
        for id in pos.keys():
            self.order.append(id)
        for i in range(0,self.n) :
            self.labels[self.order.index(i)]=str(i)

        self.color_map[self.order.index(self.actual_node)] = "red"
        print(self.labels)
        nx.draw(self.graph,pos,node_size=self.size_map,node_color=self.color_map,font_size=11,with_labels=self.labels)
        plt.title("Graph n: " + str(self.n))
        def animate(frame):
            if self.actual_node<self.n:
                self.fig.clear()
                self.set_color()
                nx.draw(self.graph, pos, node_size=self.size_map, node_color=self.color_map,
                            font_size=7, with_labels=self.labels)
        ani=animation.FuncAnimation(self.fig,animate,frames=4,interval=1000,repeat=True)

        plt.show()
    def __str__(self):
        return "=== Graph ===\n" + "n: " + str(self.n)

