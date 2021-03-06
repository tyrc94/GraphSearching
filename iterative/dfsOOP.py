from queue import LifoQueue
from node import Node
import numpy as np

def depth_first(start_state, end_state):
    '''
    Depth first graph searching algorithm
    '''
    solved = False
    visited = set()
    queue = LifoQueue()
    start_node = Node(start_state, 0, None, None)
    end_node = Node(end_state, 0, None, None)

    queue.put(start_node)
    while not queue.empty():
        current = queue.get()
        if Node.equal_states(current, end_node):
            solved = True
            path = []
            cur_back = current
            while cur_back.parent is not None:
                path.insert(0, cur_back.direction)
                cur_back = cur_back.parent
            print(path)
            return solved

        else:
            for new_node in current.expand_state():
                if new_node not in visited:
                    queue.put(new_node)
                    visited.add(new_node)
    return None


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

print(depth_first(start_node, end_node))