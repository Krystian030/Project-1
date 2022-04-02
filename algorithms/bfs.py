from tkinter import *
from pathVisualisation.Grid import Grid, path_from

def bfs(maze):
    start_node = maze.find_node(0,0)
    finish_node = maze.find_node(11,0)
    q = [start_node]
    while len(q) > 0:
        node = q.pop(0)  # FIFO
        node.visited = True
        maze.printVisited(node)
        if node == finish_node:
            return path_from(node)

        children = maze.get_possible_movements(node)
        for child in children:
            if not child.visited:
                child.parent = node
                q.append(child)
                maze.printChild(child)
        maze.printChild(node)
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
