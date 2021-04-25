def inorderTraversalIterative(root):
    res, stack = [], []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            return res
        node = stack.pop()
        res.append(node.val)
        root = node.right
    return res


"""
Time complexity: O(N)
Space complexity: O(h+n)
        10
        / \
       0  -10
      / \   \
     5   6   11

"""
