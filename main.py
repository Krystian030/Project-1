from graph.Graph import Graph
from windows.menu.MenuWindow import MenuWindow
from tkinter import *
from statsForGraph.Stats import Stats
if __name__ == '__main__':
    # stats = Stats()
    # stats.createStats()
    graph = Graph()
    graph.randomGraph(20,1)
    graph.visualizationGraph()
    # root = Tk()
    # root.title("Path")
    # root.geometry("1280x900+100+50")
    #
    # menu = MenuWindow(root)
    # root.mainloop()