class BinaryTree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def branchDepthRecursive(root, depth = 0):
    if root is None:
        return 0

    return depth + branchDepthRecursive(root.left, depth + 1) + branchDepthRecursive(root.right, depth+1)

def branchDepthIterative(root):
    sumOfDepth = 0
    stack = [{"node": root, "depth": 0}]
    while len(stack) > 0:
        nodeInfo = stack.pop()
        node,depth = nodeInfo["node"], nodeInfo["depth"],
        if node is None:
            continue
        sumOfDepth += depth
        stack.append({"node": node.left, "depth": depth + 1})
        stack.append({"node": node.right, "depth": depth + 1})

    return sumOfDepth
