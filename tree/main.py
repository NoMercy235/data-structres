from tree import *

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
# d = TreeNode(3)
# e = TreeNode(3)

a.right = b
b.left = c

print(preorder_traversal(a))
print(inorder_traversal(a))
print(postorder_traversal(a))
