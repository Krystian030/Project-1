from graph.Graph import Graph
from windows.menu.MenuWindow import MenuWindow
from tkinter import *

if __name__ == '__main__':
    # graph = Graph()
    # graph.randomGraph(100,1)
    # graph.visualizationGraph()
    root = Tk()
    root.title("Path")
    root.geometry("1280x900+100+50")

    menu = MenuWindow(root)
    root.mainloop()