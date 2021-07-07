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

            curr_level = max( prune_leaves(node.left),  prune_leaves(node.right))

            if curr_level == len(res):
                res.append([])
            res[curr_level].append(node.val)

            return curr_level + 1

        prune_leaves(root)
        return res

root = TreeNode(9)
root.right = TreeNode(3)
root.left.left = TreeNode(3)
root.right.left = TreeNode(1)
root.right.right = TreeNode(5)

solution = Solution()

print(solution.goodNodes(root))
