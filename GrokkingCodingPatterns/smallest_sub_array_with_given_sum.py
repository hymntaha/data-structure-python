import math


def smallest_subarray_with_given_sum(s, arr):
    minLen = float('inf')
    windowStart, winSum = 0, 0

    for windowEnd in range(len(arr)):
        winSum += arr[windowEnd]

        while winSum >= s:
            minLen = min(minLen, windowEnd-windowStart+1)
            winSum -= arr[windowStart]
            windowStart += 1

    if minLen == math.inf: return 0
    return minLen

'''
Time complexity: O(N+N) -> O(N)
Space complexity: O(1)
'''
inp = [2, 1, 5, 2, 3, 2]
S = 7
print(smallest_subarray_with_given_sum(S, inp))
