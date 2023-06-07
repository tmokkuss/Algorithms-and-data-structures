class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_lca(root, node1, node2):
    if root is None:
        return None

    if root == node1 or root == node2:
        return root

    left_lca = find_lca(root.left, node1, node2)
    right_lca = find_lca(root.right, node1, node2)

    if left_lca and right_lca:
        return root
    elif left_lca:
        return left_lca
    else:
        return right_lca


root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

node1 = root.left
node2 = root.right
lca = find_lca(root, node1, node2)

if lca:
    print("LCA:", lca.value)
else:
    print("LCA не найден")
