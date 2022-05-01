import sys

class Node:
    def __init__(self,x, y, id):
        self.x = x
        self.y = y
        self.rectId = id
        self.visited = False
        self.parent = None
        self.type = None
        self.cost = sys.maxsize  # Inf
        self.priority = sys.maxsize  # Inf

