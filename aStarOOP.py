from queue import PriorityQueue
from node import Node
import numpy as np

def a_star(start_state, end_state):
    '''
    A* graph searching algorithm
    '''
    solved = False
    visited = set()
    priority_queue = PriorityQueue()
    start_node = Node(start_state, 0, None, None)
    end_node = Node(end_state, 0, None, None)

    priority_queue.put((start_node.determine_cost(end_node), start_node))
    counter = 0
    while not priority_queue.empty():
        _, current = priority_queue.get()
        if Node.equal_states(current, end_node):
            solved = True
            path = []
            cur_back = current
            while cur_back.parent is not None:
                path.insert(0, cur_back.direction)
                cur_back = cur_back.parent
            print(path)
            print(counter)
            return solved

        else:
            for new_node in current.expand_state():
                if new_node not in visited:
                    priority_queue.put((new_node.determine_cost(end_node), new_node))
                    visited.add(new_node)
                    counter += 1
    return solved


''' Testing arena '''

start = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [2,3,4,1]
]

start_node = np.array(start)

end = [
    [0,0,0,0],
    [0,2,0,0],
    [0,3,0,0],
    [0,4,0,1]
]

end_node = np.array(end)

print(a_star(start_node, end_node))