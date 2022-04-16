import random
class RandomAlgorithm:
    def __init__(self,structure):
        self.struct = structure
        self.struct.tovisit.append(self.struct.actual_node)

    def func(self,graph):

        if all(elem in graph.tovisit + graph.visited for elem in graph.graph.neighbors(graph.actual_node)):

            graph.visited.append(graph.actual_node)
            graph.size_map[graph.order.index(graph.actual_node)] = 500
            graph.tovisit.pop()
            if graph.tovisit:
               graph.actual_node = graph.tovisit[-1]

        else:

            graphNeighbors = list(graph.graph.neighbors(graph.actual_node))
            graphNeighbors = list(set(graphNeighbors) - set(graph.visited))
            graphNeighbors = list(set(graphNeighbors) - set(graph.tovisit))
            choice = random.choice(graphNeighbors)
            graph.tovisit.append(choice)
            if (graph.actual_node, choice) in graph.width:
                graph.width[graph.actual_node, choice] = 1
            else:
                graph.width[ choice,graph.actual_node] = 1
            graph.size_map[graph.order.index(graph.actual_node)] = 500
            graph.actual_node = choice


        if not graph.tovisit and  graph.visited:
            graph.visited.append(graph.actual_node)
            graph.size_map[graph.order.index(graph.actual_node)] = 500
            graph.actual_node = -1

