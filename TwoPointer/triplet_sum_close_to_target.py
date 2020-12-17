import math

def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()
    smallest_diff = math.inf

    for i in range(len(arr)-2):
        left = i + 1
        right = len(arr) - 1
        while left<right:
            target_diff = target_sum - arr[i] - arr[left] - arr[right]
            if target_diff == 0: # we've found a triplet with an exact sum
                return target_sum - target_diff # return sum of all the numbers

            # the second part of the following 'if' is to handle the smallest sum
            # when we have more than one solution

            if abs(target_sum) < abs(smallest_diff) or (abs(target_diff) == abs(smallest_diff) and target_diff > smallest_diff):
                smallest_diff = target_diff # save the closest and the biggest difference

            if target_diff > 0:
                left += 1 # we need a triplet with a bigger sum
            else:
                right -= 1 # we need a triplet with smaller sum

    return target_sum - smallest_diff


print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))

"""
Sorting the array will take O(N * logN). Overall It will take O(N*logN + N ^ 2) which is asymptotically equivalent to O(N ^ 2)
Space complexity: It is O(N) which is required for sorting
"""
