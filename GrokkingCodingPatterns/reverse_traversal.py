from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def traverse(root):
    result = deque()

    queue = deque()
    queue.appendleft(root)

    while queue:
        currentLevel = []
        currentSize = len(queue)

        for _ in range(currentSize):
            currentNode = queue.popleft()
            print(currentNode.val)
            currentLevel.append(currentNode.val)

            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

        result.appendleft(currentLevel)
    return result

# [[9,10,5],[7,1],[12]]
'''
Time complexity: O(N)
Space complexity: O(N)
'''
def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Reverse level order traversal: " + str(traverse(root)))


main()
