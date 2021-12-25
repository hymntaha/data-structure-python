def moveElementToEnd(array, toMove):
    l, r = 0, len(array) - 1

    while l < r:
        while l < r and array[r] == toMove:
            r -= 1
        if array[l] == toMove:
            array[l], array[r] = array[r], array[l]
        l += 1

    return array


array = [2, 4, 2, 5, 6, 2, 2]
toMove = 2

print(moveElementToEnd(array, toMove))
