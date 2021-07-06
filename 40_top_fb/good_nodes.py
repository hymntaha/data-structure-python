class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def goodNodes(self, root: 'TreeNode') -> 'TreeNode':
        cnt = 1
        stack = [(root, root.val)]

        while len(stack) != 0:
            cur, cur_max = stack.pop()
            left = cur.left
            right = cur.right

            if right:
                if right.val < cur_max:
                    stack.append((right, cur_max))
                else:
                    cnt += 1
                    stack.append((right, right.val))

            if left:
                if left.val < cur_max:
                    stack.append((left, cur_max))
                else:
                    cnt += 1
                    stack.append((left, left.val))

        return cnt
[9,null,3,6]
root = TreeNode(9)
root.right = TreeNode(3)
root.left.left = TreeNode(3)
root.right.left = TreeNode(1)
root.right.right = TreeNode(5)

solution = Solution()

print(solution.goodNodes(root))
