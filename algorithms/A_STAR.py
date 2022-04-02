import sys
def a_star(maze):
    start_node = maze.find_node('S')
    finish_node = maze.find_node('E')
    start_node.cost = 0
    start_node.priority = 0
    pq = [start_node]
    while len(pq) > 0:
        pq.sort(key=lambda x: (x.priority))
        node = pq.pop(0)
        node.visited = True

        if node.type == 'E':
            return path_from(node)

        children = maze.get_possible_movements(node)
        for child in children:
            new_cost = node.cost + maze.move_cost(node,child)
            if new_cost < child.cost:
                child.cost = new_cost
                child.parent = node
                child.priority = new_cost + abs(child.x - finish_node.x) + abs(child.y-finish_node.y)
                pq.append(child)

    return None


maze = Maze.from_file(sys.argv[1])
maze.draw()
maze.path = a_star(maze)
print()
maze.draw()
print('path length: ', len(maze.path))
for node in maze.path:
    print(f'({node.x}, {node.y})', end=' ')
print()
