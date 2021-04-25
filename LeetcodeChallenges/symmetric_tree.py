def isSymmetric(self,root):
    if not root:
        return True
    return self.dfs(root.left, root.right)

def dfs(self, l, r):
    if l and r:
        return l.val == r.val and self.dfs(l.left, r.right) and self.dfs(l.right, r.left)
    return l == r
