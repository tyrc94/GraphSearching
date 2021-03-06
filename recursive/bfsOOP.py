from queue import Queue
from node import Node
import numpy as np
    
def breadth_first(start_state, end_state):
    '''
    Breadth first graph searching algorithm
    '''
    solved = False
    visited = set()
    queue = Queue()
    start_node = Node(start_state, 0, None, None)
    end_node = Node(end_state, 0, None, None)

    queue.put(start_node)
    counter = 0
    while not queue.empty():
        current = queue.get()
        if Node.equal_states(current, end_node):
            solved = True
            path = get_route(current)
            print(path)
            return solved

        else:
            for new_node in current.expand_state():
                if new_node not in visited:
                    queue.put(new_node)
                    visited.add(new_node)
                    counter += 1
    return None


def get_route(current, _path = []):
    if current.direction is not None:
        _path.insert(0,current.direction)
        get_route(current.parent, _path)

    return _path

''' Testing arena '''

start = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [2,2,2,1]
]

start_node = np.array(start)

end = [
    [0,0,0,0],
    [0,2,0,0],
    [0,2,0,0],
    [0,2,0,1]
]

end_node = np.array(end)

print(breadth_first(start_node, end_node))