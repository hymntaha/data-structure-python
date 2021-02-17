class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root, required_sum):
    allPaths = []
    find_paths_recursive(root, required_sum, [], allPaths)
    return allPaths

def find_paths_recursive(currentNode, required_sum, currentPath, allPaths):
    if currentNode is None:
        return

    # add the current node to the path
    currentPath.append(currentNode.val)

    # if the current node is a leaf and its value is equal to required_sum, save the current path
    if currentNode.val == required_sum and currentNode.left is None and currentNode.right is None:
        allPaths.append(list(currentPath))
    else:
        # traverse the left sub-tree
        find_paths_recursive(currentNode.left, required_sum - currentNode.val, currentPath, allPaths)

        # traverse the right sub-tree
        find_paths_recursive(currentNode.right, required_sum - currentNode.val, currentPath, allPaths)

    # remove the current node from the path to backtrack,
    # we need to remove the current node while we are going up the recursive call stack.
    del currentPath[-1]

def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) +
          ": " + str(find_paths(root, sum)))


main()

"""
TIME COMPLEXITY: O(N^2), where N is the total number of nodes in the tree. This
is due to the fact that we traverse each node once (which will take O(N)), and
for every leaf node, we might have to store its path (by making a copy of
"""
