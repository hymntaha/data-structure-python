def maxArea(height):
    # Brute force
    # maxWater,l,r = 0,0,1
    # # [4,3,2,1,4]
    # while r < len(height):
    #     minWater = min(height[l],height[r])
    #     length = r - l
    #     maxWater = max(maxWater, minWater * length)
    #
    #     r += 1
    #
    #     if r==len(height):
    #         l += 1
    #         r = l + 1
    # return maxWater


lst = [1,8,6,2,5,4,8,3,7]
print(maxArea(lst))
