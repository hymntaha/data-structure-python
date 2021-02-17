class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path(root, sum):
    if root is None:
        return False

    # if the current node is a leaf and its value is equal to the sum, we've found a path
    if root.val == sum and root.left is None and root.right is None:
        return True

    # recursively call to traverse the left and right sub-tree
    # return true if any of the two recursive call return true
    return has_path(root.left, sum - root.val) or has_path(root.right, sum - root.val)

def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has path: " + str(has_path(root, 23)))
    # print("Tree has path: " + str(has_path(root, 16)))


main()


"""
Time complexity: O(N)
Space complexity: O(N)
"""
