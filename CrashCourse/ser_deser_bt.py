def serialize(root):
    res = []
    def dfs(root):
        if not root:
            res.append('x')
            return
        res.append(root.val)
        dfs(root.left)
        dfs(root.right)
    dfs(root)
    return ' '.join(str(v) for v in res)

def deserialize(s):
    def dfs(nodes):
        val = next(nodes)
        if val == 'x': return
        cur = Node(int(val))
        cur.left = dfs(nodes)
        cur.right = dfs(nodes)
        return cur

    # create an iterator that returns a token each time we call next
    return dfs(iter(s.split()))

## Driver code
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
def get_tree(root, arr):
    if not root:
        arr.append("x")
        return
    arr.append(root.val)
    get_tree(root.left, arr)
    get_tree(root.right, arr)

inputs = ["6 4 3 x x 5 x x 8 x x", "1 2 x x 3 x x", "10 86 x x 100 x x", "x"]
for i in range(len(inputs)):
    root = build_tree(iter(inputs[i].split()))
    actual_output = deserialize(serialize(root))
    arr =[]
    get_tree(actual_output, arr)
    print("Serializing and deserializing :",' '.join(str(v) for v in arr))

# Time complexity: O(N)
