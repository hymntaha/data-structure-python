class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Recursive solution
def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    # p and q are both None
    if not p and not q:
        return True
    # one of p and q is None
    if (not q or not p) or (p.val != q.val):
        return False
    return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)

# iterative DFS
def isSameTree(p,q):
    stack =[(p,q)]
    while stack:
        p,q = stack.pop()
        if not p and not q:
            continue
        elif (not p or not q) or (p.val !=q.val):
            return False
        stack.extend([(q.right,p.right),(q.left,p.left)])
    return True
