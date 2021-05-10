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

def build_tree(nodes):
    val = next(nodes)
    if not val or val == 'x': return
    cur = Node(val, [])
    for _ in range(3): cur.children.append(build_tree(nodes))
    return cur

inputs = ["1 2 5 x x x x x 3 x x x 4 x x x", "1 2 3 x x x 4 x x x 7 x x x 5 x x x 6 x x x"]
for i in range(len(inputs)):
    root = build_tree(iter(inputs[i].split()))
    print("Ternary tree path :",ternary_tree_paths(root))
