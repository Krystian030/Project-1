import sys


class StartNode:
    def __init__(self):
        self.color = "green"


class EndNode:
    def __init__(self):
        self.color = "purple"


class Visited:
    def __init__(self):
        self.color = "blue"


class ToVisit:
    def __init__(self):
        self.color = "orange"


class Actual:
    def __init__(self):
        self.color = "black"


class Path:
    def __init__(self):
        self.color = "green"


class Node:
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.rectId = id
        self.visited = False
        self.parent = None
        self.type = None
        self.cost = sys.maxsize  # Inf
        self.priority = sys.maxsize  # Inf
