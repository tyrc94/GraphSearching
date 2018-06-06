'''
A depth first searching algorithm
'''

from queue import LifoQueue
import numpy as np

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

def equalStates(state1, state2):
    '''
    Returns a boolean to determine the equality of two states
    '''
    return np.array_equal(state1, state2)

def np_to_tuple(array):
    ''' 
    Converts numpy array to a tuple
    '''
    return tuple(map(tuple,array))

def findOne(state):
    '''
    Returns the indexes of the 2-d array when an element is equal to 1
    '''
    return [np.where(state == 1)[0][0], np.where(state == 1)[1][0]]

def expandState(state):
    '''
    Returns a dictionary of valid directions to go from current state
    '''
    new_state = {}
    row = findOne(state)[0]
    col = findOne(state)[1]

    if row > 0:
        stateUp = np.copy(state)
        stateUp[row][col] = stateUp[row - 1][col]
        stateUp[row - 1][col] = 1
        new_state['U'] = stateUp

    if row < len(state) - 1:
        stateDn = np.copy(state)
        stateDn[row][col] = stateDn[row + 1][col]
        stateDn[row + 1][col] = 1
        new_state['D'] = stateDn

    if col > 0:
        stateLeft = np.copy(state)
        stateLeft[row][col] = stateLeft[row][col - 1]
        stateLeft[row][col - 1] = 1
        new_state['L'] = stateLeft

    if col < len(state[0]) - 1:
        stateRight = np.copy(state)
        stateRight[row][col] = stateRight[row][col + 1]
        stateRight[row][col + 1] = 1
        new_state['R'] = stateRight
    
    return new_state


def depthLimited(start_node, end_node, max_depth):
    '''
    Depth limited graph searching algorithm
    '''
    solved = False
    pred = {}
    visited = set()
    stack = LifoQueue() 
    stack.put(start_node)
    path = []

    while not stack.empty():
        current = stack.get()
        if equalStates(current, end_node):
            solved = True
            while not equalStates(current, start_node):
                path.append(pred[np_to_tuple(current)][1])
                current = pred[np_to_tuple(current)][0]
            print(path[::-1])
            return solved
        else:
            depth = 0
            current2 = current
            while not equalStates(current2, start_node):
                depth += 1
                current2 = pred[np_to_tuple(current2)][0]
            if depth < max_depth:
                for expanded, direction in zip(expandState(current).values(), expandState(current)):
                    if np_to_tuple(expanded) not in visited:
                        stack.put(expanded)
                        visited.add(np_to_tuple(expanded))
                        pred[np_to_tuple(expanded)] = [current, direction]
            else:
                continue
    return solved

def iterativeDeep(start_node, end_node, max_depth):
    depth = 0
    while depth <= max_depth:
        if depthLimited(start_node, end_node, depth) == True:
            break
        else:
            depth += 1
    if depth > max_depth:
        return f"{depth} > {max_depth}: No solution found"
    return depth

print(iterativeDeep(start_node, end_node, 2500))
