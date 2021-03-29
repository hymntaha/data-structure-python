def dfs(root, target):
    if root is None:
        return None
    if root.val == target:
        return root

    # return non-null return value from the recursive calls
    left = dfs(root.left, target)
    if left is not None:
        return left

    # at this point, we know left is null, and right could be null or non-null
    # we return right child's recursive call result directly because
    # - if it's non-null we should return it
    # - if it's null, then both left and right are null, we want to return null
    return dfs(root.right, target)
    # the code can be shortened to: return dfs(root.left, target) or dfs(root.right.target)

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

inputs = [
    ["5 4 3 x x 8 x x 6 x x", 8],
    ["-100 x -500 x -50 x x", -50],
    ["9 8 11 x x 20 x x 6 x x", 11],
]
expected_outputs = [8, -50, 11]


for i in range(len(inputs)):
    root = build_tree(iter(inputs[i][0].split()))
    print("DFS :",dfs(root,inputs[i][1]).val)

"""
When to use DFS #
Tree #
DFS is essentially pre-order tree traversal.

Traverse and find/create/modify/delete node
Traverse with return value (finding max subtree, detect balanced tree)
Combinatorial problems #
DFS/backtracking and combinatorial problems are a match made in heaven (or silver bullet and werewolf 😅). As we will see in the Combinatorial Search module, combinatorial search problems boil down to searching in trees.

How many ways are there to arrange something
Find all possible combinations of …
Find all solutions to a puzzle
Graph #
Trees are special graphs that have no cycle. We can still use DFS in graphs with cycles. We just have to record the nodes we have visited and avoid re-visiting them and going into an infinite loop.

Find a path from point A to B
Find connected components
Detect cycles
"""
