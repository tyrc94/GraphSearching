import numpy as np

class Node():

    def __init__(self, state, depth, parent = None, direction = None):
        self.state = state
        self.depth = depth
        self.parent = parent
        self.direction = direction

    def __hash__(self):
        return hash(tuple(map(tuple,self.state)))
    
    def __eq__(self, other):
        return Node.equal_states(self, other)
    
    def __lt__(self, other):
        return True

    @staticmethod
    def equal_states(node1, node2):
        '''
        Returns a boolean to determine the equality of some states
        '''
        return np.array_equal(node1.state, node2.state)
    
    def find_one(self):
        '''
        Returns the indexes of the 2-d array when an element is equal to 1
        '''
        return np.where(self.state == 1)[0][0], np.where(self.state == 1)[1][0]
    
    def expand_state(self):
        '''
        Returns a dictionary of valid directions to go from current state
        '''
        expanded_states = list()
        row, col = self.find_one()

        if row > 0:
            up = np.copy(self.state)
            up[row][col], up[row -1][col] = up[row - 1][col], 1
            expanded_states.append(Node(up, self.depth + 1, self, 'U'))
        
        if row < len(self.state) - 1:
            dn = np.copy(self.state)
            dn[row][col], dn[row + 1][col] = dn[row + 1][col], 1
            expanded_states.append(Node(dn, self.depth + 1, self, 'D'))

        if col > 0:
            left = np.copy(self.state)
            left[row][col], left[row][col - 1] = left[row][col - 1], 1
            expanded_states.append(Node(left, self.depth + 1, self, 'L'))

        if col < len(self.state[0]) - 1:
            right = np.copy(self.state)
            right[row][col], right[row][col + 1] = right[row][col + 1], 1
            expanded_states.append(Node(right, self.depth + 1, self, 'R'))
        
        return expanded_states
    
    @staticmethod
    def taxicab_metric(coord1, coord2):
        '''
        Returns a distance between two coordinate points using the taxicab metric
        '''
        return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

    def determine_cost(self, end_node):
        i = 1
        cost = 0
        while i <= np.amax(self.state):
            cost += Node.taxicab_metric(
                (np.where(self.state == i)[0][0], np.where(self.state == i)[1][0]), 
                (np.where(end_node.state == i)[0][0], np.where(end_node.state == i)[1][0])
                )
            i+= 1
        return self.depth + cost
