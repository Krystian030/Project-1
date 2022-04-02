import networkx as nx
from matplotlib import pyplot as plt, animation
import random
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
            for i in range(0, 100):
                self.degreeMap.append(random.randint(1,3))
            self.graph = nx.random_regular_graph(3,self.n)
            if  nx.check_planarity(self.graph):
                break
        print(g)
        print(self.degreeMap)
    def visualizationGraph(self):


        for node in self.graph:
            self.color_map.append("green")
            self.size_map.append(100)

        #ustawianie grubości krawędzi w zależności czy przechodizmy przez niego
        pos = nx.spring_layout(self.graph,k=1,iterations=0)
        nx.draw(self.graph,pos,node_size=self.size_map,node_color=self.color_map,alpha=0.8,with_labels=True,font_size=11)
        plt.title("Graph n: " + str(self.n))


        def animate(frame):
            self.fig.clear()
            if self.color_map[self.actual_node]=="green" and self.actual_node<self.n:
                self.color_map[self.actual_node]="blue"
                self.actual_node+=1
            nx.draw(self.graph,pos, node_size=self.size_map, node_color=self.color_map, alpha=0.8, with_labels=True,
                           font_size=7)
        ani=animation.FuncAnimation(self.fig,animate,frames=6,interval=1,repeat=True)

        plt.show()
    def __str__(self):
        return "=== Graph ===\n" + "n: " + str(self.n)