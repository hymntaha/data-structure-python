import math
def smallest_subarray_with_given_sum(s, arr):
    window_sum = 0
    min_length = math.inf
    window_start = 0

    for window_end in range(0, len(arr)):
        window_sum += arr[window_end] # add the next element
        # shrink the window as small s possible until the 'window_sum' is smaller than 's'
        while window_sum >= s:
            min_length = min(min_length, window_end-window_start+1)
            window_sum -= arr[window_start]
            window_start += 1
    if min_length == math.inf:
        return 0
    return min_length


print(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2]))
"""
Time complexity of the algo will be O(N). The outer for loop runs for all elements, and the inner while loop
processes each element only once, therefore, the time complexity of the algo will be O(N+N), which is equivalent to O(N)

Space complexity O(1) constant
"""
