from graph.Graph import Graph
from windows.menu.MenuWindow import MenuWindow
from tkinter import *
from statsForGraph.Stats import Stats
from visualisation.GraphVisualization import GraphVisualization
if __name__ == '__main__':
    # stats = Stats()
    # stats.createStats()
    graph = Graph()
    graph.randomGraph(11,3)  # tworzenie grafu 3 stopnia(ilosc, stopnien)
    # graph.randomTree(10,2)  # tworzenie drzewa dowolnego stopnia (ilosc, stopnien)


    GraphVisualization.visualizationGraph(graph)    #metoda statyczna, bez potrzeby tworzenia instancji
    # graph.visualizationGraph()
    # root = Tk()
    # root.title("Path")
    # root.geometry("1280x900+100+50")
    #
    # menu = MenuWindow(root)
    # root.mainloop()