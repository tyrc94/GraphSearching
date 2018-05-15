'''
A depth first searching algorithm
'''

from queue import Queue
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

    try:
        stateUp = np.copy(state)
        stateUp[row][col] = stateUp[row - 1][col]
        stateUp[row - 1][col] = 1
        new_state['U'] = stateUp
    except IndexError:
        pass

    try:
        stateDn = np.copy(state)
        stateDn[row][col] = stateDn[row + 1][col]
        stateDn[row + 1][col] = 1
        new_state['D'] = stateDn
    except IndexError:
        pass

    try:
        stateLeft = np.copy(state)
        stateLeft[row][col] = stateLeft[row][col - 1]
        stateLeft[row][col - 1] = 1
        new_state['L'] = stateLeft
    except IndexError:
        pass

    try:
        stateRight = np.copy(state)
        stateRight[row][col] = stateRight[row][col + 1]
        stateRight[row][col + 1] = 1
        new_state['R'] = stateRight
    except IndexError:
        pass
    
    return new_state


def graphSearch(start_node, end_node):
    '''
    Depth first graph searching algorithm
    '''
    solved = False
    pred = {}
    visited = set()
    queue = Queue() 
    queue.put(start_node)
    
    while queue:
        current = queue.get()
        if equalStates(current, end_node):
            solved = True
            path = []
            while not equalStates(current, start_node):
                path.append(pred[np_to_tuple(current)][1])
                current = pred[np_to_tuple(current)][0]
            return path[::-1]
        else:
            for expanded, direction in zip(expandState(current).values(), expandState(current)):
                if np_to_tuple(expanded) not in visited:
                    queue.put(expanded)
                    visited.add(np_to_tuple(expanded))
                    pred[np_to_tuple(expanded)] = [current, direction]


print(graphSearch(start_node, end_node))
