import numpy as np

state = np.zeros((3,3))
states = []
counter = 1
goal = np.array([[1,2,3],[4,5,6],[7,8,0]])

class ListNode:
    def __init__(self, node_state_i, node_index_i, parent_node_index_i):
        self.node_state_i = node_state_i
        self.node_index_i = node_index_i
        self.parent_node_index_i = parent_node_index_i
    

    def BlankTileLocation(self, state):
            index = []
            for i in range(0, len(state[0])):
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
            return False, self
        else:
            swap = new_node.node_state_i[index[0], index[1] - 1]
            new_node.node_state_i[index[0], index[1] - 1] = new_node.node_state_i[index[0], index[1]]
            new_node.node_state_i[index[0], index[1]] = swap
        return True, self
            

    def actionMoveRight(self):
        new_node = ListNode(np.zeros((3,3)), 0, 0)
        new_node.node_state_i = self.node_state_i.copy()
        index = self.BlankTileLocation(self.node_state_i)
        if index[1] == 2:
            return False, self
        else:
            swap = new_node.node_state_i[index[0], index[1] + 1]
            new_node.node_state_i[index[0], index[1] + 1] = new_node.node_state_i[index[0], index[1]]
            new_node.node_state_i[index[0], index[1]] = swap
            return True,self

    def actionMoveUp(self):
        new_node = ListNode(np.zeros((3,3)), 0, 0)
        new_node.node_state_i = self.node_state_i.copy()
        index = self.BlankTileLocation(self.node_state_i)
        if index[0] == 0:
            return False, self
        else:
            swap = new_node.node_state_i[index[0] - 1, index[1]]
            new_node.node_state_i[index[0] - 1, index[1]] = new_node.node_state_i[index[0], index[1]]
            new_node.node_state_i[index[0], index[1]] = swap
            return True, self

    def actionMoveDown(self):
        new_node = ListNode(np.zeros((3,3)), 0, 0)
        new_node.node_state_i = self.node_state_i.copy()
        index = self.BlankTileLocation(self.node_state_i)
        if index[0] == 2:
            return False, self
        else:
            swap = new_node.node_state_i[index[0] + 1, index[1]]
            new_node.node_state_i[index[0] + 1, index[1]] = new_node.node_state_i[index[0], index[1]]
            new_node.node_state_i[index[0], index[1]] = swap
            return True, self

    def addNode(self):
        for array in states:
            duplicate = array == self.node_state_i
            if duplicate.all() == True:
                return 
            else:
                if not self.node_state_i in states:
                    new_node = ListNode(np.zeros((3,3)), 0, 0)
                    new_node.node_state_i = self.node_state_i.copy()
                    new_node.node_index_i  = self.node_index_i
                    new_node.node_index_i += 1
                    new_node.parent_node_index_i = self.parent_node_index_i
                    node_dictionary[new_node.node_index_i] = new_node
                    states.append(new_node.node_state_i)
                    nodes = open('Nodes.txt','w')
                    data = stateToData(new_node.node_state_i)
                    for i in range(0, len(data)):
                        nodes.write(str(int(data[i])) + " ")
                    nodes.write("\n")
                    nodes.close()
                    nodes_info = open('NodesInfo1.txt','w')
                    nodes_info.write(str(new_node.node_index_i) + " " + str(new_node.parent_node_index_i) + "\n")
                    nodes_info.close()

    def bruteForceSearch(self, goalNode):
        self.parent_node_index_i = self.parent_node_index_i + 1
        node = ListNode(np.zeros((3,3)), 0, 0)
        node.node_state_i = self.node_state_i.copy()
        node.node_index_i = self.node_index_i
        node.parent_node_index_i = self.parent_node_index_i
        condition = node.node_state_i == goalNode
        while True: 
            status, new_node = node.actionMoveLeft()
            if status == True:
                new_node.addNode()

            status, new_node = node.actionMoveRight()
            if status == True:
                new_node.addNode()

            status, new_node = node.actionMoveUp()
            if status == True:
                new_node.addNode()

            status, new_node = node.actionMoveDown()
            if status == True:
                new_node.addNode()
            counter += 1
            print(counter)
            



def stateToData(state):
    data = []
    for i in range(0, len(state)):
        for j in range(0, len(state[0])):
            data.append(state[j,i])
    return data



input_node = ListNode(np.array([[1,2,3],[5,6,4],[0,8,7]]), 1,-1)
states.append(input_node.node_state_i)
node_dictionary = {}
node_dictionary[input_node.node_index_i] = input_node  
input_node.bruteForceSearch(goal)