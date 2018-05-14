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

def findOne(state):
    '''
    Returns the indexes of the 2-d array when an element is equal to 1
    '''
    return [np.where(state == 1)[0][0], np.where(state == 1)[1][0]]

def expandState(state):
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
    solved = False
    route = []
    visited = []

    queue = Queue() 
    queue.put(start_node)
    while not queue.empty():
        current = queue.get()
        if equalStates(current, end_node):
            solved = True
        
            return f"Route taken: {route}"
        else:
            for expanded, direction in zip(expandState(current).values(), expandState(current)):
                if expanded.tolist() not in visited:
                    queue.put(expanded)
                    visited.append(expanded.tolist())
                    route.append(direction)
                else:
                    pass
        
print(graphSearch(start_node, end_node))
