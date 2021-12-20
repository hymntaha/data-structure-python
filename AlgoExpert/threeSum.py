def threeNumberSum(arr, target):
    arr.sort()
    res = []

    for i, val in enumerate(arr):
        if i > 0 and val == arr[i-1]:
            continue

        l, r = i + 1, len(arr) - 1

        while l < r:
            total = val + arr[l] + arr[r]

            if total > target:
                r -= 1
            elif total < target:
                l += 1
            else:
                res.append([val, arr[l], arr[r]])
                l += 1
                if arr[l] == arr[l-1] and l < r:
                    l += 1

    return res




print(threeNumberSum([12,3,1,2,-6,5,-8,6], 0))
