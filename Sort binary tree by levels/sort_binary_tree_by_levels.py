from collections import deque

class Node:
    """
    Represents a node in a binary tree.
    """
    def __init__(self, L, R, n):
        """
        Initializes a Node instance.
        """
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(root):
    """
    Performs a traversal of a binary tree
    """
    if not root:
        return []

    final = []
    nodes_queue = deque([root])

    while nodes_queue:
        current_node = nodes_queue.popleft()
        final.append(current_node.value)
        if current_node.left:
            nodes_queue.append(current_node.left)
        if current_node.right:
            nodes_queue.append(current_node.right)
    return final
