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
    return state1 == state2

def findOne(state):
    '''
    Returns the indexes of the 2-d array when an element is equal to 1
    '''
    return [np.where(state == 1)[0][0], np.where(state == 1)[1][0]]

def expandState(state):
    new_state = []
    try:
        pass
    except IndexError:
        pass

def graphSearch(start_node, end_node):
    solved = False
    route = []
    queue = Queue()
    queue.put(start)
    while len(queue) > 0:
        current = queue.get()
        if equalStates(current, end):
            solved = True
            break
        
