import sys


class Obstacle:
    def __init__(self):
        self.color = "red"


class Ground:
    def __init__(self):
        self.color = "brown"


class River:
    def __init__(self):
        self.color = "lightblue"


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
        self.cost = sys.maxsize
        self.priority = sys.maxsize

    def change_type(self, type_node):
        if type(self.type) != Obstacle and type(self.type) != River and type(self.type) != Ground:
            self.type = type_node
        elif type(self.type) == River:
            self.type.color = "dark blue"
        elif type(self.type) == Ground:
            self.type.color = "dark gray"
            # self.type.color = "dark " + self.type.color
        # self.type = type_node