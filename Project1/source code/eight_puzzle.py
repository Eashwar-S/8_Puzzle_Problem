##############################################################
# Project 1: 8 Puzzle Problem
# Author: Eashwar Sathyamurthy
##############################################################
import numpy as np

##############################################################
# ListNode : A Node class
# @param : node_state_i: 3x3 array denoting present state.
# @param : node_index_i: Index of the state.
# @param : parent_node_index_i: Parent index of the current state.
#############################################################
class ListNode:
    def __init__(self, node_state_i, node_index_i, parent_node_index_i):
        self.node_state_i = node_state_i
        self.node_index_i = node_index_i
        self.parent_node_index_i = parent_node_index_i
    
######################################################
#                Helper Functions
######################################################

# Type: Function
# @description: Locates the index of '0' in 3x3 array.
# @param: 3x3 array
# return: 1x2 vector containing index of '0'.
def BlankTileLocation(state):
    index = []
    for i in range(0, len(state[0])):
        for j in range(0, len(state[i])):
            if state[i,j] == 0:
                index.append(i)
                index.append(j)
                break
    return index

# Type: Function
# @description: Moves the '0' to the left if possible.
# @param: node
# return: status and new node after moving '0' to left
def actionMoveLeft(node):
    new_node = ListNode(np.zeros((3,3)), 0, 0)
    new_node.node_state_i = node.node_state_i.copy()
    index = BlankTileLocation(node.node_state_i)
    if index[1] == 0:
        return False, node
    else:
        #Swaping
        swap = new_node.node_state_i[index[0], index[1] - 1]
        new_node.node_state_i[index[0], index[1] - 1] = new_node.node_state_i[index[0], index[1]]
        new_node.node_state_i[index[0], index[1]] = swap
    return True, new_node
        
# Type: Function
# @description: Moves the '0' to the right if possible.
# @param: node
# return: status and new node after moving '0' to right.
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
    return True, new_node

# Type: Function
# @description: Moves the '0' Up if possible.
# return: status and new node after moving '0' Up.
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

# Type: Function
# @description: Moves the '0' Down if possible.
# return: status and new node after moving '0' Down.
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

# Type: Function
# @description: Compares two 3x3 matrices.
# return: True if equal.
def compare(mat1, mat2):
    for i in range(0, len(mat1[0])):
        for j in range(0, len(mat1[i])):
            if mat1[i,j] != mat2[i,j]:
                return False
    return True

# Type: Function
# @description: Checks whether given puzzle is solvable or not.
# @param : input 3x3 matrix
# return: True or False.
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

# Type: Function
# @description: Checks whether 3x3 matrix is already present.
# @param: node: node to be checked
# return: True or False
def nodeNotPresent(node):
    for i in range(0,len(states)):
        if compare(node.node_state_i,states[i]):
            return False
    return True

# Type: Function
# @description: Adds node to dictionary and new list
# @param: node: current new node not in the node list.
#         nodeindex: node index of the new node.
#         parentindex: parent index of the new node.
# return: status and new node after moving '0' Up.
def addNode(node,nodeindex, parentindex):
    new_node = ListNode(np.zeros((3,3)), 0, 0)
    new_node.node_state_i = node.node_state_i.copy()
    new_node.node_index_i  = nodeindex
    new_node.parent_node_index_i = parentindex
    states.append(new_node.node_state_i)

# Type: Function
# @description: Finds all the possible 3x3 matrices till
#               goal node is reached.
# @param: node: input 3x3 matrix
# @param: goal: final 3x3 matrix.
def bruteForceSearch(node, goalNode):
    node_list = []
    node_list.append(node)
    # Count iterations
    count = 0
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
            parent = parentindex[len(parentindex)-1] +1
            node_list.pop(index)
            count += 1
            print(count)
    else:
        print('Given puzzle is not solvable')

# Type: Function
# @description: Back tracks the way from the goal node
#               to the input node.
# @param: parent: list containing all the parent indexes.
# @param: child: list containing all the node indexes.
# @return: nodePath: Direct path for reaching input to goal state.
def backTracking(parent, child):
    # starting from the last parent node
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

# Type: Function
# @description: Converts 3x3 matrix into row vector
# @param: state: a 3x3 matrix
# @param: data: a 1x9 row vector
def stateToData(state):
    data = []
    for i in range(0, len(state)):
        for j in range(0, len(state[0])):
            data.append(state[j,i])
    return data

################################################################
#                   Initializing
################################################################
# Contains all 3x3 matrices without repetition.
states = []
goal = np.array([[1,2,3],[4,5,6],[7,8,0]])
# list containing all node indexes
nodeindex = [1]
# list containing all parent indexes
parentindex = [0]
# input array for accepting values from the user
input_array = np.zeros((3,3))
print('Enter 9 elements of the puzzle:')
for i in range(0,3):
    for j in range(0,3):
        input_array[i,j] = int(input())
input_node = ListNode(input_array, 1,0)
states.append(input_node.node_state_i)


# Performing brute force search
bruteForceSearch(input_node, goal)

# Writing all explored nodes in text file.
nodes = open("Nodes.txt","w")
for j in states:
    data = stateToData(j)
    for i in range(0, len(data)):
        nodes.write(str(int(data[i])) + " ")
    nodes.write("\n")
nodes.close()

# Writing parent and node indexes in text file.
nodes_info = open('NodesInfo.txt','w')
for i in range(0,len(nodeindex)-1):
    nodes_info.writelines(str(nodeindex[i]) + " " + str(parentindex[i]) + "\n")
nodes_info.close()

# Calling the back tracking function
nodePath = backTracking(parentindex, nodeindex)

# Writing the node path in text file.
node_path = open('nodePath.txt','w')
for i in nodePath:
    data = stateToData(i)
    for i in range(0, len(data)):
        node_path.write(str(int(data[i])) + " ")
    node_path.write("\n")
node_path.close()

# Prints the nodePath file in the form of matrix
def print_matrix(state):
    counter = 0
    for row in range(0, len(state), 3):
        if counter == 0:
            print("-------------")
        for element in range(counter, len(state), 3):
            if element <= counter:
                print("|", end=" ")
            print(int(state[element]), "|", end=" ")
        counter = counter + 1
        print("\n-------------")

for j in range(0,len(nodePath)):
    data = stateToData(nodePath[j])
    if j == 0:
        print("Start Node")
    elif j == len(nodePath) - 1:
        print("Achieved Goal Node")
    else:
        print("Step ", j)
    print_matrix(data)
    print()
    print()
