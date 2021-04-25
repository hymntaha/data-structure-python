def isSymmetric(self,root):
    if not root:
        return True
    return self.dfs(root.left, root.right)

def dfs(self, l, r):
    if l and r:
        return l.val == r.val and self.dfs(l.left, r.right) and self.dfs(l.right, r.left)
    return l == r


def isSymmetricIterative(self, root):
    if not root:
        return True

    stack = [(root.left, root.right)]
    while stack:
        l, r = stack.pop()
        if not l and not r:
            continue
        if not l or not r or (l.val != r.val):
            return False
        stack.append((l.left, r.right))
        stack.append(l.right, r.left)

    return True
