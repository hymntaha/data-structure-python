def maxDepth(str):
    depthCount = 0
    maxValue = 0
    for i in str:
        if i == '(':
            depthCount += 1
            maxValue = max(maxValue,depthCount)
        if i == ')':
            depthCount -= 1


    return maxValue


print(maxDepth("(1+(2*3)+((8)/4))+1"))

"""Time complexity: O(N)"""

