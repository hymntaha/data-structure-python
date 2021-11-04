from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def traverse(root):
    result = []

    queue = deque()
    queue.append(root)
    count = 1
    while queue:
        currentLevel = []
        levelSize = len(queue)
        count += 1
        for _ in range(levelSize):

            currentNode = queue.popleft()
            currentLevel.append(currentNode.val)

            if count % 2 == 0:
                if currentNode.right:
                    queue.append(currentNode.right)
                if currentNode.left:
                    queue.append(currentNode.left)
            else:
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)

        result.append(currentLevel)

    return result

# [[12],[1,7],[9,10,5][17,20]]
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
