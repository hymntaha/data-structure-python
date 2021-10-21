def maxSubArraySizeK(arr,k):
    maxSum = 0
    windowStart, windowSum = 0,0

    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]

        if windowEnd >= k - 1:
            maxSum = max(maxSum, windowSum)
            windowSum -= arr[windowStart]
            windowStart += 1

    return maxSum




inp = [2, 1, 5, 1, 3, 2]
k = 3
print(maxSubArraySizeK(inp,k))
