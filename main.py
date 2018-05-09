from queue import Queue

start = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [2,2,2,1]
]

end = [
    [0,0,0,0],
    [0,2,0,0],
    [0,2,0,0],
    [0,2,0,1]
]

def equalStates(state1, state2):
    return state1 == state2

def findOne(state):
    for rowCoord in range(len(state)):
        for colCoord in range(len(state[rowCoord])):
            if state[rowCoord][colCoord] == 1:
                return [rowCoord,colCoord]


def expandState(state):
    new_state = []
    try:
        ''' up -- CHANGE THIS CODE '''
        state[findOne(state)[0]][findOne(state)[1]] = 0
        state[findOne(state)[0]-1][findOne(state)[1]] = 1
    except IndexError:
        pass

def graphSearch(start, end):
    solved = False
    route = []
    queue = Queue()
    queue.put(start)
    while len(queue) > 0:
        current = queue.get()
        if equalStates(current, end):
            solved = True
            break
        
