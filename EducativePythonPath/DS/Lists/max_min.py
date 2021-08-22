def max_min(lst):
    result = []

    for i in range(len(lst) // 2):
        # append corresponding last element
        result.append(lst[-(i+1)])

        # append current element
        result.append(lst[i])

    if len(lst) % 2 == 1:
        # if middle value then append
        result.append(lst[len(lst) // 2])

    return result


def min_max2(lst):
    # Return empty list for empty list
    if (len(lst) == 0):
        return []

    maxIdx = len(lst) - 1  # max index
    minIdx = 0  # first index
    maxElem = lst[-1] + 1  # Max element
    # traverse the list
    for i in range(len(lst)):
        # even number means max element to append
        if i % 2 == 0:
            lst[i] += (lst[maxIdx] % maxElem) * maxElem
            maxIdx -= 1
        # odd number means min number
        else:
            lst[i] += (lst[minIdx] % maxElem) * maxElem
            minIdx += 1

    for i in range(len(lst)):
        lst[i] = lst[i] // maxElem
    return lst








# print(max_min([1,2,3,4,5,6,7]))
print(min_max2([1,2,3,4,5,6,7]))
"""
1,2,3
4,5,6,7

"""
