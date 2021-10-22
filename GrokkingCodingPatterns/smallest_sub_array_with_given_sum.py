import math

def smallest_subarray_with_given_sum(s, arr):
    window_start = 0
    window_sum = 0
    min_length = math.inf

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        while window_sum >= s:
            min_length = min(min_length, window_end-window_start+1)
            window_sum -= arr[window_start]
            window_start += 1

    return min_length


'''
Time complexity: O(N+N) -> O(N)
Space complexity: O(1)
'''
inp = [3, 4, 1, 1, 6]
S = 8
print(smallest_subarray_with_given_sum(S, inp))
