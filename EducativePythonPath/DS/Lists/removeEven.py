def removeEven(arr):
    new_arr = []

    for i in arr:
        if i % 2 != 0:
            new_arr.append(i)
    return new_arr


nums = [1,2,4,5,10,6,3]
"""
1,5,4,2,10,6,3
"""

print(removeEven(nums))


