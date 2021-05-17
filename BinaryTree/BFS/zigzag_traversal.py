from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def traverse(root):
    result = []

    if root is None:
        return

    deq = deque()
    deq.append(root)
    leftToRight = True
    while deq:
        levelSize = len(deq)
        currentLevel = deque()

        for _ in range(levelSize):
            currentNode = deq.popleft()

            if leftToRight:
                currentLevel.append(currentNode.val)
            else:
                currentLevel.appendleft(currentNode.val)

            if currentNode.left:
                deq.append(currentNode.left)
            if currentNode.right:
                deq.append(currentNode.right)

        result.append(currentLevel)


    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(traverse(root)))


main()
