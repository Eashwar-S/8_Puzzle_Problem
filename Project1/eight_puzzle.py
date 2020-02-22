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
    
    def nodeParentIndex(self,increment):
        self.parent_node_index_i = self.parent_node_index_i + increment

    def nodeIndex(self,increment):
        self.node_index_i = self.node_index_i + increment


def BlankTileLocation(state):
    index = []
    for i in range(0, len(state[0])):
        for j in range(0, len(state[i])):
            if state[i,j] == 0:
                index.append(i)
                index.append(j)
                break
    return index

def actionMoveLeft(node):
    new_node = ListNode(np.zeros((3,3)), 0, 0)
    new_node.node_state_i = node.node_state_i.copy()
    index = BlankTileLocation(node.node_state_i)
    if index[1] == 0:
        return False, node
    else:
        swap = new_node.node_state_i[index[0], index[1] - 1]
        new_node.node_state_i[index[0], index[1] - 1] = new_node.node_state_i[index[0], index[1]]
        new_node.node_state_i[index[0], index[1]] = swap
    return True, new_node
        

def actionMoveRight(node):
    new_node = ListNode(np.zeros((3,3)), 0, 0)
    new_node.node_state_i = node.node_state_i.copy()
    index = BlankTileLocation(node.node_state_i)
    if index[1] == 2:
        return False, node
    else:
        swap = new_node.node_state_i[index[0], index[1] + 1]
        new_node.node_state_i[index[0], index[1] + 1] = new_node.node_state_i[index[0], index[1]]
        new_node.node_state_i[index[0], index[1]] = swap
    return True,new_node

def actionMoveUp(node):
    new_node = ListNode(np.zeros((3,3)), 0, 0)
    new_node.node_state_i = node.node_state_i.copy()
    index = BlankTileLocation(node.node_state_i)
    if index[0] == 0:
        return False, node
    else:
        swap = new_node.node_state_i[index[0] - 1, index[1]]
        new_node.node_state_i[index[0] - 1, index[1]] = new_node.node_state_i[index[0], index[1]]
        new_node.node_state_i[index[0], index[1]] = swap
    return True, new_node

def actionMoveDown(node):
    new_node = ListNode(np.zeros((3,3)), 0, 0)
    new_node.node_state_i = node.node_state_i.copy()
    index = BlankTileLocation(node.node_state_i)
    if index[0] == 2:
        return False, node
    else:
        swap = new_node.node_state_i[index[0] + 1, index[1]]
        new_node.node_state_i[index[0] + 1, index[1]] = new_node.node_state_i[index[0], index[1]]
        new_node.node_state_i[index[0], index[1]] = swap
    return True, new_node

def compare(mat1, mat2):
    for i in range(0, len(mat1[0])):
        for j in range(0, len(mat1[i])):
            if mat1[i,j] != mat2[i,j]:
                return False
    return True

def solvabilityCheck(inputState):
    inversions = 0
    array = []
    for i in range(0,len(inputState[0])): 
        for j in range(0,len(inputState[i])):
            if inputState[i,j] != 0:
                array.append(inputState[i,j])
    for i in range(0,len(array)): 
        for j in range(i+1,len(array)):
            if array[i] > array[j]:
                inversions += 1
    if inversions%2 == 0:
        return True 
    return False 

def nodeNotPresent(node):
    for i in range(0,len(states)):
        if compare(node.node_state_i,states[i]):
            return False
    return True


def addNode(node,nodeindex, parentindex):
    new_node = ListNode(np.zeros((3,3)), 0, 0)
    new_node.node_state_i = node.node_state_i.copy()
    new_node.node_index_i  = nodeindex
    new_node.parent_node_index_i = parentindex
    node_dictionary[new_node.node_index_i] = new_node
    states.append(new_node.node_state_i)
    # nodes = open("./nodes.txt","w")
    # data = stateToData(new_node.node_state_i)
    # for i in range(0, len(data)):
    #     nodes.write(str(int(data[i])) + " ")
    # nodes.write("\n")
    # nodes.close()
    # nodes_info = open('NodesInfo1.txt','w')
    # nodes_info.writelines(str(nodeindex) + " " + str(parentindex))
    # nodes_info.close()

def bruteForceSearch(node, goalNode):
    node_list = []
    node_list.append(node)
    index = 0
    parent = 1
    if solvabilityCheck(node.node_state_i):
        intialCheck = node.node_state_i == goalNode
        if intialCheck.all() == True:
            print('Input node is goal node.Goal is reached')
            return
        while True:
            index = 0
            new_node_Left = ListNode(np.zeros((3,3)), 0, 0)
            statusLeft, new_node_Left = actionMoveLeft(node_list[index])
            if statusLeft == True:
                if(nodeNotPresent(new_node_Left)):
                    nodeindex.append(nodeindex[len(nodeindex)-1] + 1)
                    parentindex.append(parent)
                    condition = compare(new_node_Left.node_state_i, goalNode)
                    if condition == True:
                        states.append(new_node_Left.node_state_i)
                        print('Goal node is reached')
                        break
                    else:
                        addNode(new_node_Left, nodeindex[len(nodeindex)-1], parentindex[len(parentindex)-1])
                        node_list.append(new_node_Left)

            new_node_Right = ListNode(np.zeros((3,3)), 0, 0)
            statusRight, new_node_Right = actionMoveRight(node_list[index])
            if statusRight == True:
                if(nodeNotPresent(new_node_Right)):
                    nodeindex.append(nodeindex[len(nodeindex)-1] + 1)
                    parentindex.append(parent)
                    condition = compare(new_node_Right.node_state_i, goalNode)
                    if condition == True:
                        states.append(new_node_Right.node_state_i)
                        print('Goal node is reached')
                        break
                    else:
                        addNode(new_node_Right, nodeindex[len(nodeindex)-1], parentindex[len(parentindex)-1])
                        node_list.append(new_node_Right)

            new_node_Up = ListNode(np.zeros((3,3)), 0, 0)
            statusUp, new_node_Up = actionMoveUp(node_list[index])
            if statusUp == True:
                if(nodeNotPresent(new_node_Up)):
                    nodeindex.append(nodeindex[len(nodeindex)-1] + 1)
                    parentindex.append(parent)
                    condition = compare(new_node_Up.node_state_i, goalNode)
                    if condition == True:
                        states.append(new_node_Up.node_state_i)
                        print('Goal node is reached')
                        break
                    else:
                        addNode(new_node_Up, nodeindex[len(nodeindex)-1], parentindex[len(parentindex)-1])
                        node_list.append(new_node_Up)

            new_node_Down = ListNode(np.zeros((3,3)), 0, 0)
            statusDown, new_node_Down = actionMoveDown(node_list[index])
            if statusDown == True:
                if(nodeNotPresent(new_node_Down)):
                    nodeindex.append(nodeindex[len(nodeindex)-1] + 1)
                    parentindex.append(parent)
                    condition = compare(new_node_Down.node_state_i, goalNode)
                    if condition == True:
                        states.append(new_node_Down.node_state_i)
                        print('Goal node is reached')
                        break
                    else:
                        addNode(new_node_Down, nodeindex[len(nodeindex)-1], parentindex[len(parentindex)-1])
                        node_list.append(new_node_Down)
            #parentindex.append(parentindex[len(parentindex)-1] +1)
            parent = parentindex[len(parentindex)-1] +1
            node_list.pop(index)
    else:
        print('Given puzzle is not solvable')
            
def backTracking(parent, child):
    parentnode = parent[len(parent) - 1]
    childnode = 0 
    nodePath = []
    nodePath.append(states[len(states) - 1])
    while parentnode != 0:
        childnode = child[parentnode - 1]
        nodePath.append(states[childnode - 1])
        parentnode =  parent[childnode - 1]

    nodePath = nodePath[::-1]
    return nodePath

def stateToData(state):
    data = []
    for i in range(0, len(state)):
        for j in range(0, len(state[0])):
            data.append(state[j,i])
    return data



nodeindex = [1]
parentindex = [0]
input_node = ListNode(np.array([[3,8,0],[4,2,5],[7,1,6]]), 1,0)
states.append(input_node.node_state_i)
node_dictionary = {}
node_dictionary[input_node.node_index_i] = input_node  
bruteForceSearch(input_node, goal)

nodes = open("Nodes.txt","w")
for j in states:
    data = stateToData(j)
    for i in range(0, len(data)):
        nodes.write(str(int(data[i])) + " ")
    nodes.write("\n")
nodes.close()

nodes_info = open('NodesInfo.txt','w')
for i in range(0,len(nodeindex)-1):
    nodes_info.writelines(str(nodeindex[i]) + " " + str(parentindex[i]) + "\n")
nodes_info.close()

nodePath = backTracking(parentindex, nodeindex)
node_path = open('nodePath.txt','w')
for i in nodePath:
    data = stateToData(i)
    for i in range(0, len(data)):
        node_path.write(str(int(data[i])) + " ")
    node_path.write("\n")
node_path.close()