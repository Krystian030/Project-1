from pathVisualisation.Node import *
import copy


class AStarGrid:
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
        self.start_node.cost = 0
        self.start_node.priority = 0
        first_state = []
        for nodes in self.grid.board:
            for node in nodes:
                first_state.append(copy.deepcopy(node))
        self.states.append(first_state)
        # queue
        self.q = [self.start_node]

    def algorithm(self):
        while len(self.q) > 0:
            self.q.sort(key=lambda node: (node.priority))
            node = self.q.pop(0)

            node.visited = True
            if node != self.start_node:
                node.change_type(self.actual_node)
                self.state.append(node)
            if node == self.end_node:
                self.grid.createPath(node)
                for node in self.grid.path:
                    node.type = self.path
                    self.state.append(node)
                self.grid.node_to_change = self.state
                self.states.append(copy.deepcopy(self.state))
                break

            children = self.grid.get_neighbours(node)
            for child in children:
                if not child.visited:
                    cost = node.cost + self.grid.return_move_cost(child)
                    if cost < child.cost:
                        child.parent = node
                        child.cost = cost
                        child.priority = cost + abs(child.x - self.end_node.x) + abs(child.y - self.end_node.y)
                        if not child in self.q:
                            self.q.append(child)
                            if child != self.end_node:
                                child.change_type(self.to_visit)
                                self.state.append(child)
            self.grid.node_to_change = copy.deepcopy(self.state)
            self.states.append(copy.deepcopy(self.state))
            self.state = []
            if node != self.start_node:
                node.change_type(self.visited)
                self.state.append(node)
            if children is None and self.q is None:
                return None
        return self.states
