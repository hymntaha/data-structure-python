def visible_tree_node(root):
    def dfs(root, max_sofar):
        if not root:
            return 0
        total = 0
        if root.val >= max_sofar:
            total += 1

        total += dfs(root.left, max(max_sofar, root.val)) # max_sofar for child node is the larger of previous max and current node val
        total += dfs(root.right, max(max_sofar, root.val))

        return total

    # start max_sofar with the smallest number possible so any value root has is smaller than it
    return dfs(root, -float('inf'))

## Driver Code
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

inputs = ["5 4 3 x x 8 x x 6 x x", "-100 x -500 x -50 x x", "9 8 11 x x 20 x x 6 x x"]
for i in range(len(inputs)):
    root = build_tree(iter(inputs[i].split()))
    print("Visible tree node :",visible_tree_node(root))
