from src.tree.tree_node import TreeNode


def peek(stack):
    if len(stack) > 0:
        return stack[-1]


def postorder_traversal(root: TreeNode):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if root is None:
        return []

    stack = []
    result = []

    while True:

        while root:

            if root.right is not None:
                stack.append(root.right)
            stack.append(root)

            root = root.left

        root = stack.pop()

        if root.right is not None and peek(stack) == root.right:
            stack.pop()
            stack.append(root)
            root = root.right
        else:
            result.append(root.val)
            root = None

        if len(stack) <= 0:
            break

    return result
