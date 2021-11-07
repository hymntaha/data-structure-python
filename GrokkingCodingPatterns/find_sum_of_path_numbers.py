class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_sum_of_path_numbers(root):
    def helper(node, num):
        if node is None:
            return 0
        num = num * 10 + node.val
        if node.left is None and node.right is None:
            return num
        return helper(node.left, num) + helper(node.right, num)

    return helper(root, 0)
# 101+116+115
'''
        1
     0     1
   1     6   5
'''


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
