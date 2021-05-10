def ternary_tree_paths(root):
    # dfs helper function
    def dfs(root, path, res):
        # exit condition, reached leaf node, append paths to results
        if all(c is None for c in root.children):
            res.append('->'.join(path) + '->' + root.val)
            return

        # dfs on each non-null child
        for child in root.children:
            if child is not None:
                dfs(child, path + [root.val], res)

    res = []
    if root:dfs(root, [], res)
    return res

class Node:
    def __init__(self, val, children = []):
        self.val = val
        self.children = children

