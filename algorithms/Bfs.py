from pathVisualisation.Node import *
import copy

class Bfs:
    def __init__(self, structure):
        self.struct = structure
        self.struct.labels[self.struct.actual_node] = 0

    #
    def func(self, graph):
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
                            graph.width[graph.actual_node, a] = 1
                        else:
                            graph.width[a, graph.actual_node] = 1
                        if a not in graph.labels:
                            graph.labels[a] = str(
                                graph.order_label + 1)  # nadawanie odpowiedniej kolejności dla labeli, kolejności rysowania,
                            graph.order_label += 1

                        break


        else:
            graph.visited.append(graph.actual_node)
            graph.size_map[graph.order.index(graph.actual_node)] = 500
            graph.actual_node = -1


class BfsGrid:
    def __init__(self, grid):
        self.grid = grid
        # Type of nodes
        self.start = StartNode()
        self.end = EndNode()
        self.actual_node = Actual()
        self.visited = Visited()
        self.to_visit = ToVisit()
        self.path = Path()
        self.start_node = None
        self.q = None
        self.end_node = None
        self.state = []
        self.states = []

    def start_algorithm(self):
        self.start_node = self.grid.start_node
        self.end_node = self.grid.end_node
        self.start_node.type = self.start
        self.end_node.type = self.end
        # self.grid.node_to_change.extend([self.start_node, self.end_node])
        self.states.append(copy.deepcopy([self.start_node, self.end_node]))
        # queue
        self.q = [self.start_node]

    def bfs_algorithm(self):
        while len(self.q) > 0:
            node = self.q.pop(0)

            node.visited = True
            if node != self.start_node:
                node.type = self.actual_node
                # self.grid.node_to_change.append(node)
                self.state.append(node)
            if node == self.end_node:
                self.grid.createPath(node)
                # self.grid.printPath()
                for node in self.grid.path:
                    node.type = self.path
                    # self.grid.node_to_change.apend(node)
                    self.state.append(node)
                self.grid.node_to_change = self.state
                # self.grid.grid_visualisation.update_grid()
                # self.states.append(self.grid.node_to_change)
                self.states.append(copy.deepcopy(self.state))
                break

            children = self.grid.getNeighbours(node)
            for child in children:
                if not child.visited:
                    child.parent = node
                    if not child in self.q:
                        self.q.append(child)
                        if child != self.end_node:
                            child.type = self.to_visit
                            # self.grid.node_to_change.append(child)
                            self.state.append(child)
            self.grid.node_to_change = self.state
            # self.grid.grid_visualisation.update_grid()
            self.states.append(copy.deepcopy(self.state))
            self.state = []
            if node != self.start_node:
                node.type = self.visited
                self.state.append(node)
                # self.grid.node_to_change.append(node)
        return self.states
