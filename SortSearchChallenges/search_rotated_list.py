def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        # if found target value, return the index
        if nums[mid] == target:
            return mid

        # determine it's left rotated or right rotated
        """
        No rotated:
        1 2 3 4 5 6 7
             mid
             
        left rotated: pivot at the left side of the origin sorted array, A[mid] >= A[left]
        3 4 5 6 7 1 2
             mid
        search in A[left] ~ A [mid] if A[left] <= target < A[mid] else, search right side
        
        right rotated: pivot at the right side of the origin sorted array, A[mid] < A[left]
        6 7 1 2 3 4 5
             mid          
        search in A[mid] ~ A[right] if A[mid] < target <= A[right] else, search left side
        """
        if nums[mid] >= nums[left]: # left rotated
            # in ascending order side
            if nums[left] <= target and target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else: # right rotated
            # in ascending order side
            if nums[mid] < target and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    # cannot find the target value
    return -1

# Driver to test above code
if __name__ == '__main__':

    lst = [6, 7, 8, 9, 10, 0, 1, 2, 3]
    key = 0

    print("Index of the element is : ",
          search(lst, key))

