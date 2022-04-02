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

    def visualizationGraph(self):
        for node in self.graph:
            self.color_map.append("green")
            self.size_map.append(500)

        #TODO ustawianie grubości krawędzi w zależności czy przechodizmy przez niego
        #TODO tworzenie labelow
        pos = nx.spring_layout(self.graph,k=4,iterations=1000)
        nx.draw(self.graph,pos,node_size=self.size_map,node_color=self.color_map,font_size=11,with_labels=True)
        plt.title("Graph n: " + str(self.n))


        def animate(frame):

            if self.actual_node<self.n:
                self.color_map[self.actual_node]="red"
                for i in self.graph.neighbors(self.actual_node):
                    #print(i)
                    self.fig.clear()

                    self.color_map[i]="blue"
                    nx.draw(self.graph, pos, node_size=self.size_map, node_color=self.color_map,
                            font_size=7, with_labels=True)
                self.color_map[self.actual_node] = "blue"
                self.actual_node+=1
        ani=animation.FuncAnimation(self.fig,animate,frames=4,repeat=True)

        plt.show()
    def __str__(self):
        return "=== Graph ===\n" + "n: " + str(self.n)