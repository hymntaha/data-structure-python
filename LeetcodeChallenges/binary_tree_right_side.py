def rightSideView(root):
    deque = collections.deque()
    if root:
        deque.append(root)

    res = []
    while deque:
        size, val = len(deque), 0
        for _ in range(size):
            node = deque.popleft()
            val = node.val # store last value in each level
            if node.left:
                deque.append(node.left)
            if node.right:
                deque.append(node.right)

        res.append(val)
    return res
