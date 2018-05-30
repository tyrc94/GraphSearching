import numpy as np

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

def taxicab_metric(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

def determine_cost(start_state, end_state):
    i = 1
    cost = 0
    while i <= np.amax(start_state):
        cost += taxicab_metric(
            (np.where(start_state == i)[0][0], np.where(start_state == i)[1][0]), 
            (np.where(end_state == i)[0][0], np.where(end_state == i)[1][0])
            )
        i+= 1
    return cost

print(determine_cost(start_node, end_node))