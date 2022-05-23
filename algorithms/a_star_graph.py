from collections import defaultdict
class A_star_graph:
    def __init__(self,structure):
        self.struct = structure
        self.struct.tovisit.append(self.struct.actual_node)
        self.actualCost = 0
        self.costDict = defaultdict(list)       #[nie spr] = [koszt dojscia, z kąd przychodzimy]
        self.cost_heuristic = defaultdict(list)
        self.struct.labels[0] = str(0)
        self.elementsChecked = []
        self.heuristic_values = [structure.n] * structure.n
        self.heuristic( 0, self.struct.last_node)

    def func(self,graph):
        if len(graph.visited) != graph.n-1:
            if all(elem in self.elementsChecked + graph.visited for elem in graph.graph.neighbors(graph.actual_node)):
                #podmiana węzła akutalnego
                graph.visited.append(graph.actual_node)
                graph.size_map[graph.order.index(graph.actual_node)] = 500
                minValue = min(self.costDict, key=self.costDict.get)
                if (self.costDict.get(minValue)[1], minValue) in graph.width:
                    graph.width[self.costDict.get(minValue)[1], minValue] = 1
                else:
                    graph.width[minValue, self.costDict.get(minValue)[1]] = 1

                graph.actual_node = minValue
                self.actualCost = self.costDict.get(graph.actual_node)[0] - self.heuristic_values[minValue]
                self.elementsChecked = []
                del self.costDict[graph.actual_node]
                graph.actualChecked = -1
                #znalezienei szukanego węzła
                if graph.actual_node == graph.last_node:
                    graph.visited.append(graph.actual_node)
                    graph.size_map[graph.order.index(graph.actual_node)] = 500
                    graph.actual_node = -1
                    graph.actualChecked = -1
                    graph.found = True
            else:
                #Sprawdzanie punktów aktualnego węzła
                for a in graph.graph.neighbors(graph.actual_node):
                    cost = 0
                    if a not in graph.visited + self.elementsChecked:
                        graph.actualChecked = a
                        if a in self.costDict:
                            if (graph.actual_node, a) in graph.edgeLabels:
                                cost = self.actualCost + graph.edgeLabels[graph.actual_node, a] + self.heuristic_values[a]
                            else:
                                cost = self.actualCost + graph.edgeLabels[a, graph.actual_node] + self.heuristic_values[a]
                            if cost < self.costDict.get(a)[0]:
                                self.costDict.get(a)[0]= cost
                                self.costDict.get(a)[1]= graph.actual_node
                        else:
                            if (graph.actual_node, a) in graph.edgeLabels:
                                cost = self.actualCost + graph.edgeLabels[graph.actual_node, a] + self.heuristic_values[a]
                            else:
                                cost = self.actualCost + graph.edgeLabels[a, graph.actual_node] + self.heuristic_values[a]
                            self.costDict[a].append(cost)
                            self.costDict[a].append(graph.actual_node)
                            graph.tovisit.append(a)
                        self.elementsChecked.append(a)
                        graph.labels[a] = str(self.costDict.get(a)[0] - self.heuristic_values[a])

                        break

        else:
            graph.visited.append(graph.actual_node)
            graph.size_map[graph.order.index(graph.actual_node)] = 500
            graph.actual_node = -1
            graph.actualChecked = -1

    #zachłanna heurystyka
    def heuristic(self, value, node):
        self.heuristic_values[node] = value
        for child in self.struct.graph.neighbors(node):
            if value < self.heuristic_values[child]:
                self.heuristic(value+1, child)


