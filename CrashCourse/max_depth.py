def max_depth(root):
    def dfs(root): # we dont actually need an inner function doing it here just keep consistent other solutions
        # null node adds no depth
        if not root:
            return 0

        # depth of current node's subtree = max depth of the two subtrees + 1 provioded by current node
        return max(dfs(root.left), dfs(root.right)) + 1
    return dfs(root)

# Driver code
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


inputs = ["5 4 3 x x 8 x x 6 x x", "1 x x", "x", "6 x 9 x 11 x 7 x x"]
expected_outputs = [3, 1, 0, 4]

for i in range(len(inputs)):
    root = build_tree(iter(inputs[i].split()))
    print("Get max depth", max_depth(root))
