# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            if not node:
                return 0

            res = 1 if node.val >= maxVal else 0
            print(res)
            print("val")
            print(node.val)
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, root.val)

node1 = TreeNode(3)
node2 = TreeNode(1)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(1)
node6 = TreeNode(5)

node1.left = node2
node1.right = node4
node2.left = node3
node4.left = node5
node4.right = node6

solClass = Solution()
print(solClass.goodNodes(node1))
