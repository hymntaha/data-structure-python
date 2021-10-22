def maxSubArraySizeK(arr,k):
    window_start, max_sum = 0, 0
    cur_sum = 0
    for window_end in range(len(arr)):
        cur_sum += arr[window_end]

        if window_end > k - 1:
            cur_sum -= arr[window_start]
            window_start += 1

        max_sum = max(max_sum, cur_sum)

    return max_sum

inp = [2, 3, 4, 1, 5]
k = 2
print(maxSubArraySizeK(inp,k))
