import math

def triplet_sum_close_to_target(arr,target):
    arr.sort()
    smallest_diff = math.inf

    for i in range(0, len(arr) - 2):
        if arr[i] == arr[i-1] and i > 0:
            continue

        lower = i + 1
        upper = len(arr) - 1

        while lower < upper:
            s = arr[i] + arr[lower] + arr[upper]

            if s == target:
                return s
            if abs(target-s) < abs(target-smallest_diff):
                smallest_diff = s
            if s <= target:
                lower += 1
                while arr[lower] == arr[lower-1] and lower < upper:
                    lower += 1
            else:
                upper -= 1

    return smallest_diff

print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
print(triplet_sum_close_to_target([1, 0, 1, 1], 100))
