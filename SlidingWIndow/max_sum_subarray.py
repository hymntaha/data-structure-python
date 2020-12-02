def max_sub_array_of_size_k(k, arr):
    max_sum, window_sum = 0, 0
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end] # add the next element
        # slide the window, we dont need to slide if we've not hit the required window size of 'k'
        if window_end >= k-1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1
    return max_sum

input = [2, 1, 5, 1, 3, 2]
k=3
print(max_sub_array_of_size_k(k, input))
# time complexity is O(N)
# space complexity is O(1) - constant
