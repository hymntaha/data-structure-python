def canBeEqual(target, arr):
    count = [0] * 1001

    for i in range(len(arr)):
        count[arr[i]] += 1
        count[target[i]] -= 1

    return not any(count)


target = [1,2,3,4]
arr = [2,4,1,3]

print(canBeEqual(target,arr))

def alternativeSolution(target, arr):
    if len(target) != len(arr): return False

    target.sort()
    arr.sort()

    for i in range(len(target)):
        if arr[i] != target[i]:
            return False

    return True
