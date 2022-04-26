class Dfs:
    def __init__(self,structure):
        self.struct = structure
        self.struct.tovisit.append(self.struct.actual_node)

    def func(self,graph):

        if all(elem in graph.tovisit + graph.visited for elem in graph.graph.neighbors(graph.actual_node)):
            graph.labels[graph.actual_node] = str(
                graph.order_label + 1)  # nadawanie odpowiedniej kolejności dla labeli, kolejności rysowania,
            graph.order_label += 1

            graph.visited.append(graph.actual_node)
            graph.size_map[graph.order.index(graph.actual_node)] = 500
            graph.tovisit.pop()

            if graph.tovisit:
               graph.actual_node = graph.tovisit[-1]

        else:
            for a in graph.graph.neighbors(graph.actual_node):
                if a not in graph.tovisit + graph.visited:
                    graph.tovisit.append(a)
                    if (graph.actual_node, a) in graph.width:
                        graph.width[graph.actual_node, a] = 1
                    else:
                        graph.width[ a,graph.actual_node] = 1
                    graph.size_map[graph.order.index(graph.actual_node)] = 500
                    graph.actual_node = a
                    break

        if not graph.tovisit and  graph.visited:
            graph.visited.append(graph.actual_node)
            graph.size_map[graph.order.index(graph.actual_node)] = 500
            graph.actual_node = -1
