def quicksort(nums, start=0, end=None):
    # print('quicksort', nums, start, end)
    if end is None:
        nums = list(nums)
        end = len(nums) - 1

    if start < end:
        pivot = partition(nums, start, end)
        quicksort(nums, start, pivot-1)
        quicksort(nums, pivot+1, end)

    return nums

def partition(nums, start=0, end=None):
    # print('partition', nums, start, end)
    if end is None:
        end = len(nums) - 1

    # Initialize right and left pointers
    l, r = start, end-1

    # Iterate while they're apart
    while r > l:
        # print('  ', nums, l, r)
        # Increment left pointer if number is less or equal to pivot
        if nums[l] <= nums[end]:
            l += 1

        # Decrement right pointer if number is greater than pivot
        elif nums[r] > nums[end]:
            r -= 1

        # Two out-of-place elements found, swap them
        else:
            nums[l], nums[r] = nums[r], nums[l]
    # print('  ', nums, l, r)
    # Place the pivot between the two parts
    if nums[l] > nums[end]:
        nums[l], nums[end] = nums[end], nums[l]
        return l
    else:
        return end


l1 = [1, 5, 6, 2, 0, 11, 3]
pivot = partition(l1)
print(l1, pivot)
