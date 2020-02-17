import numpy as np
import self as self

fname = 'input.txt'
data = np.loadtxt(fname)

state = np.zeros((3,3))
states = []
counter = 1
output = np.array([[1,2,3],[4,5,6],[7,8,0]])


class ListNode:
    def __init__(self, node_state_i, node_index_i, parent_node_index_i):
        self.node_state_i = node_state_i
        self.node_index_i = node_index_i
        self.parent_node_index_i = parent_node_index_i
        self.next = None
    
    def BlankTileLocation(self, state):
        index = []
        for i in range(0, len(state)):
            for j in range(0, len(state[i])):
                if state[i,j] == 0:
                    index.append(i)
                    index.append(j)
                    break
        return index

    def actionMoveLeft(self):
        new_node = ListNode(np.zeros((3,3)), 0, 0)
        new_node.node_state_i = self.node_state_i.copy()
        index = self.BlankTileLocation(self.node_state_i)
        if index[1] == 0:
            return False
        else:
            swap = new_node.node_state_i[index[0], index[1] - 1]
            new_node.node_state_i[index[0], index[1] - 1] = new_node.node_state_i[index[0], index[1]]
            new_node.node_state_i[index[0], index[1]] = swap
            for array in states:
                duplicate = array == new_node.node_state_i
                if duplicate.all() == True:
                    print('dumass')
                    return
            new_node.node_index_i  = self.node_index_i
            new_node.node_index_i += 1
            new_node.parent_node_index_i = self.parent_node_index_i
            node_dictionary[new_node.node_index_i] = new_node
            self.next = new_node
            states.append(new_node.node_state_i)
            print(states)

    def actionMoveRight(self):
        new_node = ListNode(np.zeros((3,3)), 0, 0)
        new_node.node_state_i = self.node_state_i.copy()
        index = self.BlankTileLocation(self.node_state_i)
        if index[1] == 2:
            return
        else:
            swap = new_node.node_state_i[index[0], index[1] + 1]
            new_node.node_state_i[index[0], index[1] + 1] = new_node.node_state_i[index[0], index[1]]
            new_node.node_state_i[index[0], index[1]] = swap
            print(new_node.node_state_i)
            for array in states:
                duplicate = array == new_node.node_state_i
                if duplicate.all() == True:
                    return
            new_node.node_index_i  = self.node_index_i
            new_node.node_index_i += 1
            new_node.parent_node_index_i = self.parent_node_index_i
            node_dictionary[new_node.node_index_i] = new_node
            self.next = new_node
            states.append(new_node.node_state_i)
            print(states)

    def actionMoveUp(self):
        new_node = ListNode(np.zeros((3,3)), 0, 0)
        new_node.node_state_i = self.node_state_i.copy()
        index = self.BlankTileLocation(self.node_state_i)
        if index[0] == 0:
            return
        else:
            swap = new_node.node_state_i[index[0] - 1, index[1]]
            new_node.node_state_i[index[0] - 1, index[1]] = new_node.node_state_i[index[0], index[1]]
            new_node.node_state_i[index[0], index[1]] = swap
            print(new_node.node_state_i)
            for array in states:
                duplicate = array == new_node.node_state_i
                if duplicate.all() == True:
                    return
            new_node.node_index_i  = self.node_index_i
            new_node.node_index_i += 1
            new_node.parent_node_index_i = self.parent_node_index_i
            node_dictionary[new_node.node_index_i] = new_node
            self.next = new_node
            states.append(new_node.node_state_i)
            print(states)

    def actionMoveDown(self):
        new_node = ListNode(np.zeros((3,3)), 0, 0)
        new_node.node_state_i = self.node_state_i.copy()
        index = self.BlankTileLocation(self.node_state_i)
        if index[0] == 2:
            return
        else:
            swap = new_node.node_state_i[index[0] + 1, index[1]]
            new_node.node_state_i[index[0] + 1, index[1]] = new_node.node_state_i[index[0], index[1]]
            new_node.node_state_i[index[0], index[1]] = swap
            print(new_node.node_state_i)
            for array in states:
                duplicate = array == new_node.node_state_i
                if duplicate.all() == True:
                    return
            new_node.node_index_i  = self.node_index_i
            new_node.node_index_i += 1
            new_node.parent_node_index_i = self.parent_node_index_i
            node_dictionary[new_node.node_index_i] = new_node
            self.next = new_node
            states.append(new_node.node_state_i)
            print(states)

    def addNode(self, counter):
            nodes = open('Nodes.txt','w')
            for i in range(0, len(self.node_state_i)):
                for j in range(0, len(self.node_state_i[i])):
                    nodes.write(str(int(self.node_state_i[j,i])) + " ")
            nodes.write("\n")
            nodes.close()
            nodes_info = open('NodesInfo1.txt','w')
            nodes_info.write(str(counter) +" "+ str(self.node_index_i) + " " + str(self.parent_node_index_i) + "\n")
            counter += 1
            nodes_info.close()

def data_to_state(data):
    counter = 0
    while counter <= len(data)/3 - 1: 
        k = 0
        for row in range(counter, len(data), 3):
            state[counter, k] = data[row]
            k += 1
        counter += 1
    return state


input_node = ListNode(data_to_state(data), 1,1)
states.append(input_node.node_state_i)
node_dictionary = {}
node_dictionary[input_node.node_index_i] = input_node  
input_node.addNode()
print(node_dictionary)