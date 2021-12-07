class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

'''
'''
def findClosestValRecursive(tree, target, closest):
    if tree is None:
        return closest
    if abs(target-closest) > abs(target - tree.value):
        closest = tree.value

    if target < tree.value:
        return findClosestValRecursive(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValRecursive(tree.right, target, closest)
    else:
        return closest


