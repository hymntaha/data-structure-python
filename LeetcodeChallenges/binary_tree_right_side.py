def rightSideView(root):
    view = []
    if root:
        level = [root]
        while level:
            view += level[-1].val,
            level = [kid for node in level for kid in (node.left, node.right) if kid]
    return view
