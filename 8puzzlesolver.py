'''
An 8 puzzle solver using a depth first search
'''

from queue import Queue
import numpy as np
import collections

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

def findZero(state):
    '''
    Returns the indexes of the 2-d array when an element is equal to 1
    '''
    return [np.where(state == 0)[0][0], np.where(state == 0)[1][0]]

def expandState(state):
    '''
    Returns a dictionary of valid directions to go from current state
    '''
    new_state = {}
    row = findZero(state)[0]
    col = findZero(state)[1]

    if row > 0:
        stateUp = np.copy(state)
        stateUp[row][col] = stateUp[row - 1][col]
        stateUp[row - 1][col] = 0
        new_state['U'] = stateUp

    if row < len(state) - 1:
        stateDn = np.copy(state)
        stateDn[row][col] = stateDn[row + 1][col]
        stateDn[row + 1][col] = 0
        new_state['D'] = stateDn

    if col > 0:
        stateLeft = np.copy(state)
        stateLeft[row][col] = stateLeft[row][col - 1]
        stateLeft[row][col - 1] = 0
        new_state['L'] = stateLeft

    if col < len(state[0]) - 1:
        stateRight = np.copy(state)
        stateRight[row][col] = stateRight[row][col + 1]
        stateRight[row][col + 1] = 0
        new_state['R'] = stateRight
    
    return new_state


def graphSearch(start_node, end_node):
    '''
    Breadth first graph searching algorithm
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


def puzzle_solver():
    '''
    8 puzzle solver. Inputs are space separated and unique values from 0 to 8
    '''
    print("Welcome to the 8 puzzle solver! \nInputs should be space separated and unique values from 0 to 8")

    first_row  = [int(x) for x in input("\nFirst row of three numbers: ").split()]
    second_row  = [int(x) for x in input("Second row of three numbers: ").split()]
    third_row  = [int(x) for x in input("Third row of three numbers: ").split()]

    start = [first_row, second_row, third_row]

    start_node = np.array(start)

    end = [
        [1,2,3],
        [4,5,6],
        [7,8,0]
    ]

    end_node = np.array(end)

    return f'\nSolution: {graphSearch(start_node, end_node)}'

if __name__ == "__main__":
    print(puzzle_solver())