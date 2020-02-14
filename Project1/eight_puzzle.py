import numpy as np
import self as self


class ListNode:
    def __init__(self, node_state_i, node_index_i, parent_node_index_i):
        self.node_state_i = node_state_i
        self.node_index_i = node_index_i
        self.parent_node_index_i = parent_node_index_i
        self.next = None


fname = 'input.txt'
data = np.loadtxt(fname)

state = np.zeros((3,3))
states = []
def data_to_state(data):
    counter = 0
    while counter <= len(data)/3 - 1: 
        k = 0
        for row in range(counter, len(data), 3):
            state[counter, k] = data[row]
            k += 1
        counter += 1
    return state

output = np.array([[1,2,3],[4,5,6],[7,8,0]])
input_node = ListNode(data_to_state(data), 1,None)
states.append(input_node.node_state_i)
print(states)

node_dictionary = {}
node_dictionary[input_node.node_index_i] = input_node  
    
def BlankTileLocation(current_node):
    index = []
    for i in range(0, len(current_node.node_state_i)):
        for j in range(0, len(current_node.node_state_i[i])):
            if current_node.node_state_i[i,j] == 0:
                index.append(i)
                index.append(j)
                break
    return index

def actionMoveLeft(current_node):
    new_node = current_node
    index = BlankTileLocation(new_node)
    if index[1] == 0:
        return
    else:
        swap = new_node.node_state_i[index[0], index[1] - 1]
        new_node.node_state_i[index[0], index[1] - 1] = new_node.node_state_i[index[0], index[1]]
        new_node.node_state_i[index[0], index[1]] = swap
        print(current_node.node_state_i)
        for array in states:
            duplicate = array == new_node.node_state_i
            if duplicate.all() == True:
                return
        new_node.node_index_i += 1
        node_dictionary[new_node.node_index_i] = new_node
        current_node.next = new_node
        states.append(new_node.node_state_i)

        
actionMoveLeft(input_node)
