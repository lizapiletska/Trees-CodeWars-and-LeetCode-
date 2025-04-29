def add_subtrees(final, left, right):
    """
    Appends the results of subtree.
    """
    final += left
    final += right
    return final

def traverse(node, order):
    """
    Recursively traverses a binary tree.
    """
    if node is None:
        return []

    final = []

    left_res = traverse(node.left, order)
    right_res = traverse(node.right, order)

    if order == "pre_order":
        final.append(node.data)
        final = add_subtrees(final, left_res, right_res)

    elif order == "in_order":
        final = add_subtrees(final, left_res, [])
        final.append(node.data)
        final = add_subtrees(final, [], right_res)

    elif order == "post_order":
        final = add_subtrees(final, left_res, right_res)
        final.append(node.data)

    return final

def pre_order(node):
    """
    Performs a pre-order traversal.
    """
    return traverse(node, "pre_order")

def in_order(node):
    """
    Performs a in_order traversal.
    """
    return traverse(node, "in_order")

def post_order(node):
    """
    Performs a post_order traversal.
    """
    return traverse(node, "post_order")

