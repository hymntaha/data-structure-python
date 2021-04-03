def lca(root, node1, node2):
    return None


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

def find_node(root, target):
    if not root: return
    if root.val == target: return root
    return find_node(root.left, target) or find_node(root.right, target)

inputs = ["6 4 3 x x 5 x x 8 x x", "6 4 3 x x 5 x x 8 x x", "6 4 3 x x 5 x x 8 x x", "x"]
inputs1 = [4, 4, 3, 3]
inputs2 = [8, 6, 5, 2]
for i in range(len(inputs)):
    root = build_tree(iter(inputs[i].split()))
    node1 = find_node(root, inputs1[i])
    node2 = find_node(root, inputs2[i])
    actual_output = lca(root, node1, node2)
    if not actual_output:
        print("Lowest common ancester:",str(None))
    else:
        print("Lowest common ancester:",str(actual_output.val))
