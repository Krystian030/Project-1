from tkinter import *
from pathVisualisation.Grid import Grid, path_from

def bfs(maze):
    start_node = maze.find_node(0,0)
    finish_node = maze.find_node(39,29)
    maze.printGreen(start_node)
    maze.printRed(finish_node)
    q = [start_node]
    while len(q) > 0:
        node = q.pop(0)  # FIFO

        node.visited = True
        if node != start_node:
            maze.printActual(node)
        if node == finish_node:
            return path_from(node)

        children = maze.get_possible_movements(node)
        for child in children:
            if not child.visited:
                child.parent = node
                if not child in q:
                    q.append(child)
                    if child != finish_node:
                        maze.printChild(child)
        if node != start_node:
            maze.printVisited(node)
    return None

root = Tk()
root.title("Path")
root.geometry("800x600")

maze = Grid(root, 800, 600)
maze.displayGrid()

maze.path = bfs(maze)
maze.printPath()
print('path length: ', len(maze.path))
for node in maze.path:
    print(f'({node.x}, {node.y})', end=' ')
print()

root.mainloop()
