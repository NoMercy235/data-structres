class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preorder_traversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if root is None:
        return []

    node_stack = [root]

    result = []

    while len(node_stack) > 0:
        node = node_stack.pop()
        result.append(node.val)
        if node.right:
            node_stack.append(node.right)
        if node.left:
            node_stack.append(node.left)

    return result


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)

a.right = b
b.left = c

print(preorder_traversal(a))
