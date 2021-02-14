from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def traverse(root):
    result = []
    if root is None:
        return result

    queue = deque()
    queue.append(root)

    leftToRight = True

    while queue:
        levelSize = len(queue)
        currentLevel = deque()

        for _ in range(levelSize):
            currentNode = queue.popleft()

            if leftToRight:
                currentLevel.append(currentNode.val)
            else:
                currentLevel.appendleft(currentNode.val)
        result.append(list(currentLevel))

        leftToRight = not leftToRight

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
