from collections import deque

def ocean_view(heights):
    m, result = 0, deque()
    for i in range(len(heights)-1, -1, -1):
        if heights[i] > m:
            m = heights[i]
            result.appendleft(i)
    return result

heights = [4,2,3,1]
print(ocean_view(heights))
