def findMin(arr):
    low = float('inf')
    for i in arr:
        if i < low:
            low = i

    return low

print(findMin([4,2,1,5,0]))
print(findMin([9,2,3,5]))
