class Bfs:
    def __init__(self,structure):
        self.struct = structure
#
    def bfs(self,graph):

        if graph.tovisit or not graph.visited:
            if all(elem in graph.tovisit + graph.visited for elem in graph.graph.neighbors(graph.actual_node)):
                graph.visited.append(graph.actual_node)
                graph.actual_node = graph.tovisit.pop(0)
            else:
                for a in graph.graph.neighbors(graph.actual_node):
                    if a not in graph.tovisit and a not in graph.visited:
                        graph.tovisit.append(a)
                        graph.width[graph.order.index(graph.actual_node), a] =1
                        print (graph.width)
                        break
        else:
            graph.visited.append(graph.actual_node)
            graph.actual_node = -1

    def bfsGridBoard(board):
        start_node = board.startNode
        finish_node = board.endNode
        board.printGreen(start_node)
        board.printRed(finish_node)
        q = [start_node]
        while len(q) > 0:
            node = q.pop(0)  # FIFO
    
            node.visited = True
            if node != start_node:
                board.printActual(node)
            if node == finish_node:
                board.createPath(node)
                board.printPath()
                return 0
    
            children = board.getNeighbours(node)
            for child in children:
                if not child.visited:
                    child.parent = node
                    if not child in q:
                        q.append(child)
                        if child != finish_node:
                            board.printChild(child)
            if node != start_node:
                board.printVisited(node)
        return None