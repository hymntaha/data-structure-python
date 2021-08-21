def right_rotate(lst, k):
    n = len(lst)
    k %= n

    reverse(lst, 0, n - 1)
    reverse(lst, 0, k - 1)
    reverse(lst, k, n - 1)

    return lst

def reverse(nums, start,end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start, end = start + 1, end - 1


print(right_rotate([10,20,30,40,50],3))
# 30,40,50,10,20
