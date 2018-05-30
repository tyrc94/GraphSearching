from queue import LifoQueue
from node import Node
import numpy as np

def depth_limited(start_state, end_state, max_depth):
    '''
    Depth limited first graph searching algorithm
    '''
    solved = False
    visited = set()
    stack = LifoQueue()
    start_node = Node(start_state, 0, None, None)
    end_node = Node(end_state, 0, None, None)

    stack.put(start_node)
    while not stack.empty():
        current = stack.get()
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
            if current.depth < max_depth:
                for new_node in current.expand_state():
                    if new_node not in visited:
                        stack.put(new_node)
                        visited.add(new_node)
            else:
                continue
    return solved



def iterative_deepening(start_node, end_node, max_depth):
    depth = 0
    while depth < max_depth:
        if depth_limited(start_node, end_node, depth):
            break
        else:
            depth += 1
    if depth > max_depth:
        return f"{depth} > {max_depth}: No solution found"
    return depth

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

print(iterative_deepening(start_node, end_node, 2500))