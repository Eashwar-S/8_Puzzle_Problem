import numpy as np
import self as self


class ListNode:
    def __init__(self, node_state_i, node_index_i, parent_node_index_i):
        self.node_state_i = node_state_i
        self.node_index_i = node_index_i + 1
        self.parent_node_index_i = node_index_i
        self.next = None


