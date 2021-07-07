class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findLeaves(self, root: 'TreeNode') -> 'TreeNode':
        res = []

        def prune_leaves(node: TreeNode):

            if not node:
                return 0

            print('CURRENT NODE')
            print(node.val)
            curr_level = max( prune_leaves(node.left),  prune_leaves(node.right))
            print('CURRENT LEVEL')
            print(curr_level)
            if curr_level == len(res):
                res.append([])
            res[curr_level].append(node.val)

            return curr_level + 1

        prune_leaves(root)
        return res

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

solution = Solution()

print(solution.findLeaves(root))
