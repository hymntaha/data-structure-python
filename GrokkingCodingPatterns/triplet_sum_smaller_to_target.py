import math

def triplet_sum_smaller_to_target(arr,target):
    arr.sort()
    small_triplets = 0

    for i in range(0, len(arr) - 2):
        if arr[i] == arr[i-1] and i > 0:
            continue

        lower = i + 1
        upper = len(arr) - 1

        while lower < upper:
            s = arr[i] + arr[lower] + arr[upper]

            if s < target:
                small_triplets += upper - lower
                lower += 1
                while arr[lower] == arr[lower-1] and lower < upper:
                    lower += 1
            else:
                upper -= 1

    return small_triplets

'''
Time complexity: O(N * logN + N^2) => N^2
Space complexity: O(N)
'''
# print(triplet_sum_smaller_to_target([-1, 0, 2, 3], 3))
print(triplet_sum_smaller_to_target([-1, 4, 2, 1, 3], 5))
