from tkinter import *
from pathVisualisation.GridBoardBoard import GridBoard, path_from

def a_star(board):
    start_node = board.find_node(0, 0)
    finish_node = board.find_node(39, 29)
    board.printGreen(start_node)
    board.printRed(finish_node)
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
            board.printActual(node)
        if node == finish_node:
            return path_from(node)

        children = board.get_possible_movements(node)
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
                        board.printChild(child)
        if node != start_node:
            board.printVisited(node)
    return None


root = Tk()
root.title("Path")
root.geometry("800x600")

board = GridBoard(root, 800, 600)
board.displayGridBoard()

board.path = a_star(board)
board.printPath()
print('path length: ', len(board.path))
for node in board.path:
    print(f'({node.x}, {node.y})', end=' ')
print()

root.mainloop()
