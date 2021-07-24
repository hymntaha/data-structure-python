def duplicateZeroes(arr):
    zeroes = arr.count(0)
    n = len(arr)
    for i in range(n-1, -1, -1):
        if i + zeroes < n:
            arr[i + zeroes] = arr[i]
        if arr[i] == 0:
            zeroes -= 1
            if i + zeroes < n:
                arr[i + zeroes] = 0

arr = [1,0,2,3,0,4,5,0]
# print(duplicateZeroes(arr))

def duplicateZeroesExtraSpace(arr):
    newArray = []
    countZeroes = 0

    for i in range(len(arr) - 1):
        newArray.append(arr[i])
        if arr[i] == 0:
            countZeroes += 1
            newArray.append(arr[i])
            newArray[i+1] = 0
    for _ in range(countZeroes-1):
        newArray.pop()

    return newArray


print(duplicateZeroesExtraSpace(arr))
