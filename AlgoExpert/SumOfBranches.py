class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSum(root):
    sums = []
    calculateBranchSum(root, 0, sums)
    return sums

def calculateBranchSum(node, runningSum, sums):
    if node is None:
        return

    runningSum = runningSum + node.value
    if node.left is None and node.right is None:
        sums.append(runningSum)
        return
    calculateBranchSum(node.left, runningSum, sums)
    calculateBranchSum(node.right, runningSum, sums)



tree = BinaryTree(1)
tree.left = BinaryTree(2)
tree.right = BinaryTree(3)
tree.left.left = BinaryTree(4)
tree.left.right = BinaryTree(5)
tree.right.left = BinaryTree(6)
tree.right.right = BinaryTree(7)
tree.right.right.left = BinaryTree(8)
tree.right.right.right = BinaryTree(9)

print(branchSum(tree))

