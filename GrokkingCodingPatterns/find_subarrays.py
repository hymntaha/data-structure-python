from collections import deque


def find_subarray(arr,target):
    res = []
    prod = 1
    left = 0

    for right in range(len(arr)):
        prod *= arr[right]
        while(prod >= target and left < len(arr)):
            prod /= arr[left]
            left += 1

        tmp_list = deque()
        for i in range(right, left - 1, -1):
            tmp_list.append(arr[i])
            res.append(list(tmp_list))

    return res

nums = [2, 5, 3, 10]
target=32
print(find_subarray(nums,target))
'''
Time complexity: The main for loop managing the sliding window takes O(N)
but creating subarrays can take up to O(N^2) so overall algo will take
O(N^3)

Space complexity: O(N^ 3)

'''
