class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def findClosestValueInBst(tree,target):
    return findClosestValRecursive(tree,target, float('inf'))

'''
Average:
Time: O(log(n))
Space: O(log(n))
Worse:
Time: O(log(n))
Space: O(log(n))
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

'''
Average:
Time: O(log(n))
Space: O(1)
Worse:
Time: O(log(n))
Space: O(1)
'''
def findClosestValIter(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target-closest) > abs(target-currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest
