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

def addNode(node):
    for i in range(0,len(states)):
        if compare(node.node_state_i,states[i]):
            return False
    else:
        new_node = ListNode(np.zeros((3,3)), 0, 0)
        new_node.node_state_i = node.node_state_i.copy()
        new_node.node_index_i  = node.node_index_i
        new_node.node_index_i += 1
        new_node.parent_node_index_i = node.parent_node_index_i + 1
        node_dictionary[new_node.node_index_i] = new_node
        states.append(new_node.node_state_i)
        print(states)
        nodes = open('nodes.txt','w+')
        data = stateToData(new_node.node_state_i)
        for i in range(0, len(data)):
            nodes.writelines(str(int(data[i])))
        nodes.write("\n")
        nodes.close()
        nodes_info = open('NodesInfo1.txt','w')
        nodes_info.write(str(new_node.node_index_i) + " " + str(new_node.parent_node_index_i) + "\n")
        nodes_info.close()
    return True

def bruteForceSearch(node, goalNode):
    node_list = []
    node_list.append(node)
    index = 0
    count = 0
    if solvabilityCheck(node.node_state_i):
        intialCheck = node.node_state_i == goalNode
        if intialCheck.all() == True:
            print('Input node is goal node.Goal is reached')
            return
        while True:
            index = 0
            statusLeft, new_node_Left = actionMoveLeft(node_list[index])
            if statusLeft == True:
                if(addNode(new_node_Left)):
                    condition = new_node_Left.node_state_i == goalNode
                    if condition.all() == True:
                        print('Goal node is reached')
                        break
                    else:
                        node_list.append(new_node_Left)


            statusRight, new_node_Right = actionMoveRight(node_list[index])
            if statusRight == True:
                if(addNode(new_node_Right)):
                    condition = new_node_Right.node_state_i == goalNode
                    if condition.all() == True:
                        print('Goal node is reached')
                        break
                    else:
                        node_list.append(new_node_Right)

            statusUp, new_node_Up = actionMoveUp(node_list[index])
            if statusUp == True:
                if(addNode(new_node_Up)):
                    condition = new_node_Up.node_state_i == goalNode
                    if condition.all() == True:
                        print('Goal node is reached')
                        break
                    else:
                        node_list.append(new_node_Up)

            statusDown, new_node_Down = actionMoveDown(node_list[index])
            if statusDown == True:
                if(addNode(new_node_Down)):
                    condition = new_node_Down.node_state_i == goalNode
                    if condition.all() == True:
                        print('Goal node is reached')
                        break
                    else:
                        node_list.append(new_node_Down)
            node_list.pop(index)
            print(count)
            count += 1
    else:
        print('Given puzzle is not solvable')
            
        

def stateToData(state):
    data = []
    for i in range(0, len(state)):
        for j in range(0, len(state[0])):
            data.append(state[j,i])
    return data


def main():
    print("Hello, World!")
    if __name__== "__main__" :
        main()
input_node = ListNode(np.array([[1,0,3],[4,2,5],[7,8,6]]), 1,-1)
states.append(input_node.node_state_i)
node_dictionary = {}
node_dictionary[input_node.node_index_i] = input_node  
bruteForceSearch(input_node, goal)
print(node_dictionary)