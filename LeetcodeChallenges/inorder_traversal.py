def inorderTraversalIterative(root):
    ans = []
    stack = []

    while stack or root:
        if root != None:
            stack.append(root)
            root = root.left
        else:
            tmpNode = stack.pop()
            ans.append(tmpNode.val)
            root = tmpNode.right
    return ans


"""
Time complexity: O(N)
Space complexity: O(h+n)
        10
        / \
       0  -10
      / \   \
     5   6   11

"""
