def max_depth(root):
    return

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
