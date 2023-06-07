class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorder_traversal(root, result):
    if root is None:
        return

    inorder_traversal(root.left, result)
    result.append(root.value)
    inorder_traversal(root.right, result)


def build_sorted_tree(values):
    if not values:
        return None

    mid = len(values) // 2
    root = TreeNode(values[mid])
    root.left = build_sorted_tree(values[:mid])
    root.right = build_sorted_tree(values[mid+1:])

    return root


def sort_tree(root):
    sorted_values = []
    inorder_traversal(root, sorted_values)
    sorted_tree = build_sorted_tree(sorted_values)
    return sorted_tree


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)


sorted_tree = sort_tree(root)


result = []
inorder_traversal(sorted_tree, result)
print(result)
