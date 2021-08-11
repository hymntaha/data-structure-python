def sortColors(col):
    low, high = 0, len(col) - 1
    index = 0

    while index <= high:
        if col[index] == 0:
            col[index], col[low] = col[low], col[index],

            index += 1
            low += 1
        elif col[index] == 1:
            index += 1
        else:
            col[index], col[high] = col[high], col[index],
            index += 1
            high -= 1

    print(col)


n = [2,0,2,1,1,0]
print(sortColors(n))
