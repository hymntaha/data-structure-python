def zigzagLevelOrder(self, root):
    if root is None:
        return []

    result = [[root.val]]
    parents = [root]
    children= []
    childrenValues = []
    reverse = True

    while len(parents) > 0:
        for i in range(len(parents)):
            if parents[i].left:
                children.append(parents[i].left)
                childrenValues.append(parents[i].left.val)
            if parents[i].right:
                children.append(parents[i].right)
                childrenValues.append(parents[i].right.val)

        if reverse:
            childrenValues = childrenValues[::-1]
        reverse = not reverse
        if len(childrenValues) > 0:
            result.append(childrenValues)

        childrenValues = []

        parents = children
        children = []

    return result

"""
Time complexity: O(N)
Space complexity: O(N)

"""
