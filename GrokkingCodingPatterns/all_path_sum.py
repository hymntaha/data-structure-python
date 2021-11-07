class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root, sum):
    if not root:
        return []

    def recur(root, sum, path, res):
        path.append(root.val)
        sum -= root.val

        if not root.left and not root.right: # leaf
            if not sum:
                res.append([item for item in path])

        if root.left: recur(root.left, sum, path, res)
        if root.right: recur(root.right, sum, path, res)
        path.pop()
        return

    path, res = [], []
    recur(root, sum, path, res)
    return res
'''
    12
 7     1
4     10 5

'''

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

