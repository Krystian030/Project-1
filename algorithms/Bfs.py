class Bfs:
    def __init__(self,structure):
        self.struct = structure
#
    def func(self,graph):

        if graph.tovisit or not graph.visited:
            if all(elem in graph.tovisit + graph.visited for elem in graph.graph.neighbors(graph.actual_node)):
                graph.visited.append(graph.actual_node)
                graph.size_map[graph.order.index(graph.actual_node)] = 500
                graph.actual_node = graph.tovisit.pop(0)
                graph.size_map[graph.order.index(graph.actual_node)] = 1000
            else:
                for a in graph.graph.neighbors(graph.actual_node):
                    if a not in graph.tovisit and a not in graph.visited:
                        graph.tovisit.append(a)
                        if (graph.actual_node, a) in graph.width:
                            graph.width[graph.actual_node, a] =1
                        else:
                            graph.width[ a,graph.actual_node] = 1
                        break
        else:
            graph.visited.append(graph.actual_node)
            graph.size_map[graph.order.index(graph.actual_node)] = 500
            graph.actual_node = -1

