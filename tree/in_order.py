from tree.tree_node import TreeNode


def inorder_traversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if root is None:
        return []

    node_stack = []
    done = False
    current = root

    result = []

    while not done:

        if current is not None:
            node_stack.append(current)
            current = current.left
        else:
            if len(node_stack) > 0:
                current = node_stack.pop()
                result.append(current.val)
                current = current.right
            else:
                done = True

    return result
