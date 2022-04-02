from tkinter import *
from pathVisualisation.Grid import Grid, path_from

def a_star(maze):
    start_node = maze.find_node(0, 0)
    finish_node = maze.find_node(39, 29)
    maze.printGreen(start_node)
    maze.printRed(finish_node)
    start_node.cost = 0
    start_node.priority = 0
    pq = [start_node]
    while len(pq) > 0:
        pq.sort(key=lambda x: (x.priority))
        for i in pq:
            print(str(i.priority), end=' ')
        print()
        node = pq.pop(0)
        node.visited = True

        if node != start_node:
            maze.printActual(node)
        if node == finish_node:
            return path_from(node)

        children = maze.get_possible_movements(node)
        for child in children:
            if not child in pq:
                new_cost = node.cost + 1
                if new_cost < child.cost:
                    child.cost = new_cost
                    child.parent = node
                    a = abs(child.x - finish_node.x) + abs(child.y-finish_node.y)
                    print("odleglosc:" + str(a))
                    print("new_cost: " + str(new_cost))
                    child.priority = new_cost + a
                    print("child priority: " + str(child.priority))
                    pq.append(child)
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

maze.path = a_star(maze)
maze.printPath()
print('path length: ', len(maze.path))
for node in maze.path:
    print(f'({node.x}, {node.y})', end=' ')
print()

root.mainloop()
