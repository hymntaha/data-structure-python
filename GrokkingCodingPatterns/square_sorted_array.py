def square_sorted_arr(arr):
    res = [0] * len(arr)
    print(res)
    l, r = 0, len(arr) - 1

    for i in range(len(res) - 1, -1, -1):
        left = arr[l] * arr[l]
        right = arr[r] * arr[r]

        if left > right:
            res[i] = left
            l += 1
        else:
            res[i] = right
            r -= 1

    return res
# 0 0 0 0 0
print(square_sorted_arr([-3, -1, 0, 1, 2]))
