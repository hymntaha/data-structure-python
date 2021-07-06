class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def goodNodes(self, root: 'TreeNode') -> 'TreeNode':
        def dfs(node, maxVal):
            if not node:
                return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        dfs(root, root.val)
root = TreeNode(9)
root.right = TreeNode(3)
root.left.left = TreeNode(3)
root.right.left = TreeNode(1)
root.right.right = TreeNode(5)

solution = Solution()

print(solution.goodNodes(root))
