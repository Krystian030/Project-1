import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.n = None
        self.graph = None

    def createRandomGraph(self):
        # TODO
        pass

    def loadGraph(self):
        # TODO
        pass

    # density - percent of density (1% - 100%)
    def randomGraph(self, n, density):
        self.n = n
        self.graph = nx.erdos_renyi_graph(n, density)

    def visualizationGraph(self):
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos)
        plt.title("Graph n: " + str(self.n))
        plt.show()

    def __str__(self):
        return "=== Graph ===\n" + "n: " + str(self.n)