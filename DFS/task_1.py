class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []


def dfs(root):
    result = []
    if root is None:
        return result

    result.append(root.value)
    for child in root.children:
        result.extend(dfs(child))

    return result

root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

root.children = [node2, node3]
node2.children = [node4, node5]

result = dfs(root)
print(result)
