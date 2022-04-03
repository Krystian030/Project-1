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
            graph.visited.append(actual_node)
            graph.actual_node = -1

