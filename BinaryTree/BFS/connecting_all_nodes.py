from __future__ import print_function
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    # tree traversal using 'next' pointer
    def print_tree(self):
        print("Traversal using 'next' pointer: ", end='')
        current = self
        while current:
            print(str(current.val) + " ", end='')
            current = current.next


def connect_all_siblings(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)

    currentNode, previousNode = None, None

    while queue:
        currentNode = queue.popleft()
        if previousNode:
            previousNode.next = currentNode
        previousNode = currentNode

    # insert the children of current node in the queue
    if currentNode.left:
        queue.append(currentNode.left)
    if currentNode.right:
        queue.append(currentNode.right)



def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_all_siblings(root)
    root.print_tree()


main()
""" 
Time complexity: O(N) where N is the total number of nodes in the tree. This is due to the fact that we traverse each node once
Space compleixty: O(N) which is required for the queue. Since we can have a max of N/2 nodes at any level

"""
