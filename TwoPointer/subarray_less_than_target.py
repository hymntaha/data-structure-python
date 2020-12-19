def find_subarrays(arr, target):
    result = set()
    start = 0
    next = 1
    for i in range(len(arr)):
        prod = arr[start] * arr[next]
        if prod < target and (arr[start]):
            result.add(arr[start])
            result.add(arr[next])
            result.add((arr[start], arr[next]))
            start += 1
            next += 1
        else:
            if arr[start] < target:
                result.add(arr[start])
                start += 1
            elif arr[next] < target:
                result.add(arr[next])
                next += 1

    return result

arr = [2, 5, 3, 10]
target = 30

print(find_subarrays(arr, target))
