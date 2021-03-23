from typing import List

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right: # <= because left and right could point to the same element,  < would miss it
        # double slash for integer division in python 3, we don't have to worry about integer
        # `left + right` overflow since python integers can be arbitrarily large
        mid = (left + right) // 2
        # found target, return its index
        if arr[mid] == target:
            return mid
        # middle less than target, discard left by making left search boundary `mid + 1`
        if arr[mid] < target:
            left = mid + 1
        # middle greater than target, discard right half by making right search boundary `mid - 1`
        else:
            right = mid - 1
    return -1

print("Binary search :", binary_search([1,3,5,7,8], 5))
print("Binary search :", binary_search([1,2,3,4,5,6,7], 0))
print("Binary search :", binary_search([2, 8, 89, 120, 1000], 120))
