class TreeNode(object):
    """
    Definition for a binary tree node.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Contains the solution for the problem
    """
    def deleteNode(self, root, key):
        """
        Deletes the node with the given key.
        """
        if not root:
            return None

        if key < root.val:
            new_left_r = self.deleteNode(root.left, key)
            root.left = new_left_r
        elif key > root.val:
            new_right_r = self.deleteNode(root.right, key)
            root.right = new_right_r
        else:
            if root.left is None:
                replace = root.right
                return replace
            elif root.right is None:
                replace = root.left
                return replace
            else:
                predcess = root.left

                while predcess and predcess.right:
                    predcess = predcess.right
                if predcess:
                    root.val = predcess.val
                    root.left = self.deleteNode(root.left, predcess.val)

        return root

