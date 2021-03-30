def valid_bst(root):
    def dfs(root, min_val, max_val):
        # empty nodes are always valid
        if not root:
            return True

        if not (min_val <= root.val <= max_val):
            return False

        return dfs(root.left, min_val, root.val) and dfs(root.right, root.val, max_val)

    return dfs(root, -float('inf'), float('inf')) # root is always valid



class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(nodes):
    val = next(nodes)
    if not val or val == 'x': return
    cur = Node(int(val))
    cur.left = build_tree(nodes)
    cur.right = build_tree(nodes)
    return cur

inputs = ["6 4 3 x x 5 x x 8 x x", "6 4 3 x x 8 x x 8 x x", "1 2 x x 3 x x", "x", "7 7 7 x x x 7 x 7 x x"]
for i in range(len(inputs)):
    root = build_tree(iter(inputs[i].split()))
    print("Valid binary search :", valid_bst(root))

# Time complexity: O(N)
